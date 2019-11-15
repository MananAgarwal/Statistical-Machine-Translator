# Statistical Machine Translator

As part of the Information Retrieval Course (BITS CS F469) we have built a lexical cross-language translator. It uses Statistical Machine Translation model heavily inspired by the IBM Model 1. Statistical Machine Translation is an empirical machine translation technique using which translations are generated on the basis of statistical models trained on bilingual text corpora. Our model can translate a document between Dutch and English.

## To translate a document and test the model's performance

1. Download the repository
2. Open the terminal/command prompt and cd to the downloaded repository
3. Run the python script "testing.py"
        """ python testing.py """
        NOTE: Use Python3
4. The interactive command line would give you the further instructions
5. On completion this will give you
        - Total number of word pairs
        - Cosine similarity
        - Jaccard coefficient


## Improvement of IBM Model
IBM Model would create a dictionary of all possible pairs of English and Dutch words. But this will consume a lot of space and time to compute. For reference traditional IBM model was creating 1,39,54,090 words pairs when trained on only 1000 lines but my optimised model creates only 1,10,15,619 even when trained on 1,00,000 lines.

I am only considering those English-Dutch word pairs that occur in some sentence pair. This does not affect the accuracy of the model because the eliminated word pairs would have had a translation probability of 0 anyways.