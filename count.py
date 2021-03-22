import wikipedia
import string
import json
import time

# links from
# https://en.wikipedia.org/wiki/Wikipedia:Multiyear_ranking_of_most_viewed_pages

top_pages = [
  "Donald Trump",
  "Barack Obama",
  "United States",
  "India",
  "Elizabeth II",
  "World War II",
  "Michael Jackson",
  "United Kingdom",
  "Lady Gaga",
  "Eminem",
  "Sex",
  "Adolf Hitler",
  "Cristiano Ronaldo",
  "Game of Thrones",
  "World War I",
  "The Beatles",
  "Justin Bieber",
  "Canada",
  "Steve Jobs",
  "Freddie Mercury",
  "Kim Kardashian",
  "The Big Bang Theory",
  "List of Presidents of the United States",
  "Australia",
  "Michael Jordan",
  "Lionel Messi",
  "Stephen Hawking",
  "Dwayne Johnson",
  "Darth Vader",
  "List of highest-grossing films",
  "Taylor Swift",
  "Star Wars",
  "China",
  "Miley Cyrus",
  "Academy Awards",
  "Lil Wayne",
  "Abraham Lincoln",
  "Elon Musk",
  "Japan",
  "Germany",
  "Johnny Depp",
  "Harry Potter",
  "New York City",
  "Selena Gomez",
  "Kobe Bryant",
  "How I Met Your Mother",
  "September 11 attack",
  "Rihanna",
  "LeBron James",
  "Albert Einstein",
  "Russia",
  "The Walking Dead (TV series)",
  "Leonardo DiCaprio",
  "Kanye West",
  "Tupac Shakur",
  "Angelina Jolie",
  "France",
  "John F. Kennedy",
  "Chernobyl disaster",
  "Scarlett Johansson",
  "Breaking Bad",
  "Tom Cruise",
  "Mila Kunis",
  "Vietnam War",
  "Jennifer Aniston",
  "Arnold Schwarzenegger",
  "Pablo Escobar",
  "Earth",
  "Joe Biden",
  "Ariana Grande",
  "William Shakespeare",
  "Mark Zuckerberg",
  "List of Marvel Cinematic Universe films",
  "Queen Victoria",
  "Bill Gates",
  "Will Smith",
  "Nicki Minaj",
  "Ted Bundy",
  "Keanu Reeves",
  "Muhammad Ali",
  "Glee (TV series)",
  "Charles Manson",
  "John Cena",
  "Singapore",
  "Bruce Lee",
  "Elvis Presley",
  "Katy Perry",
  "Israel",
  "Sexual intercourse",
  "Marilyn Monroe",
  "Illuminati",
  "Winston Churchill",
  "London",
  "Brad Pitt",
  "Periodic Table",
  "Jay-Z",
  "Doctor Who",
  "Diana, Princess of Wales",
  "Prince (musician)",
  "David Bowie",
  "Adele",
  "Heath Ledger",
  "American Civil War"
]

unique_words = {}
all_text = ""
total_nb_words = 0
# to remove punctuation
translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))


for page_title in top_pages:
  print(page_title, " ...")

  try:
    page = wikipedia.page(page_title, auto_suggest = False)
  except wikipedia.exceptions.DisambiguationError as e:
    print(e)
    continue

  for l in page.content.split("\n"):
    if l.startswith("="):
      continue

    no_punctuation = l.translate(translator)
    lower_case = no_punctuation.lower()
    all_text += " " + lower_case

    paragraph_words = lower_case.split()
    for word in paragraph_words:

      try:
        float(word)
      except ValueError as e:
        if word not in unique_words:
          unique_words[word] = 0
        unique_words[word] += 1
        total_nb_words += 1

sorted_ranking = {k: v for k, v in sorted(unique_words.items(), key=lambda item: item[1])}

out = {
  "total": total_nb_words,
  "ranking": sorted_ranking
}

output_ranking = open("ranking.json","w") 
output_ranking.write(json.dumps(out, indent=2, ensure_ascii=False))
