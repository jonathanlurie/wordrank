# Counting the most used words in English

One of takeaways of [this video](https://www.youtube.com/embed/95NgtNgmnWA) on Youtube is that learning a new foreign laguage goes by remembering the most common words. That make quite a lot of sense, even though one that grammar (and in some languages, grammatical cases) are going to distord this a little, but let's focus on the easy part: **dumb statistics**.

Here we are going to focus on the English language (which is not my mother tongue, personnaly) and it's commonly said that you'll need roughly **3000 words** in your brain storage to be "fluent" (which in itself is an extremely vague concept).  
I'm sure there is a way to find "what are the 3000 most common words in English" but:
1. that's not a fun way to get/build a list
2. will it be reliable? Based on what source?

*Note:* In this little 2-evenings project, I will assume that *spoken* English and *witten* English are using the same words, which I now is not exactely true.

There are freely available large bodies of text online but I don't feel like the integral of Shakespear and Tom Sawyer are reflecting the English people are using nowadays, this is why I've decided that my sample of text is going to be from **Wikipedia** and in particular from the [Multiyear ranking of most viewed pages](https://en.wikipedia.org/wiki/Wikipedia:Multiyear_ranking_of_most_viewed_pages).

Thos articles are very popular, with section made by a wide range of contributors, so they may (hopefuly) reflect some sort of language diversity.

The script [count.py](count.py) fetches all the raw text of all the articles from the list. Then, it removes the title (since they always contain the same kinds of word, that's a small bias less), then removes the numbers and puctuation. In the end, about **1 million** words remains.

The output is in the file [ranking.json](ranking.json) and contains the total count followed by the ranking in ascending order, for which the number is the number of occurences. I have not manually currated this output, thus it contains:
- some single-letter words due to the splitting of words like *"doesn't"*
- some number intervals that are not flagged as "numbers" by my way to simple method, such as in *"25–31"*
- some proper nouns, those are tough to flag but a naive method could do some ok job
- some numbers with a currency, such as in *"£296"*. A naive method could also be good enough

But in the end, these unwanted words are way less than 1% of the total so it's probably acceptable.

**Note:** I know this contains many biases, this is only an experiment.

# Results
- about 1 million words in the sample
- about 44000 unique words
- top word is *"the"* with 75864 occurences
- second is *"of"* with already half of that! (34004 occurences)
- most of the first words are preopositions, pronouns and things like that
- the **first** word (hishest ranking) to actually carry a meaning is **first** (3106 occurences, 25th position)
- the words on rank 3000 (and you *must* all the ones with a higher ranking) is *"citizen"* with only 41 occurence, so a frenquency of about 0.0041%
- *"televangelist"* is used only once in a million so maybe don't make it your job (or maybe do, I don't know actually)