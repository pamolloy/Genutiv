# Genutiv #
Genutiv aims to test the accuracy of patterns commonly cited in educational literature to help guess the gender of German nouns. The application currently consists of four scripts that download, crawl, compare and analyze data from the German Wikitionary.

## Background ##
The most difficult task when learning German as a native English speaker is the tedious acquisition of new words. That process becomes particularly difficult with nouns, which require the memorization of a complementary trait, the grammatical gender.

German nouns are each assigned one of the three grammatical genders: masculine, feminine or neuter. The gender helps determine how a noun is declined according to the number (i.e. single or plural) and case: nominative, accusative, dative and gentive. Fortunately, a noun's gender is often related to its morphology or semantics. These patterns can expedite the acquisition of new nouns by averting the memorization of an additional trait alongside the definition of a noun. Unfortunately, few patterns are accurate in every case, so that exceptions need to be memorized nevertheless.

For further information about collections of German nouns and grammatical caveats see: *[Guessing German Noun Gender](http://pamolloy.dyndns.org/blog/2011/08/16/gender/)*

The decisions behind how the scripts function is explained in the *[Genutiv](http://pamolloy.dyndns.org/project/genutiv/)* article.

## TODO ##
A general list of modifications to be made to more than one file. Edits to individual files are contained in the commented header of each file.

### Code ###
*   Add progress output for slow functions

### Grammar ###
*   Foreign proper nouns may be removed from the collection of nouns to be analyzed
*   The gender and plural ending of compound nouns are governed by the last word in the compound. Therefore it is not necessary to learn the gender of a compound noun and compound nouns should be removed from analysis. For more information see [German Compound Words](http://german.about.com/od/nounsandcases/a/German-Compound-Words.html)
*   Some German nouns have a different meaning depending on the gender (e.g. [Band](http://www.dict.cc/?s=Band)

