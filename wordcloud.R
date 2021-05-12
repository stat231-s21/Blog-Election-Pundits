library(tidyverse) 
library(janitor)
library(wordcloud2)

library(tidytext)
library(wordcloud)
library(textdata)

# even using the URLs embedded in the HTML code, some did not work
# remove the poems for which we don't have the text

trump_data <- "trump_speeches/trump_speeches_wordcloud.csv"
biden_data <- "biden_speeches/biden_speeches_wordcloud.csv"


# Create a list of custom stopwords that should be added
word <- c("i’ve", "it’s", "i’m", "he’s", "let’s",
          "won’t", "we’re", "you’re", "that’s","we’ve", "don’t", "you’ve")
lexicon <-  rep("custom", times=length(word))

# Create a dataframe from the two vectors above
mystopwords <- data.frame(word, lexicon)
names(mystopwords) <- c("word", "lexicon")

# Add the dataframe to stop_words df that exists in the library stopwords
stop_words2 <-  dplyr::bind_rows(stop_words, mystopwords) %>%
  mutate(word = str_replace_all(word, "'","’"))

# function to draw word cloud
dscore<-function(data){
  speeches <- read_csv(data) %>%
    filter(text != "Missing")
  
  word_frequencies <- speeches %>%
    unnest_tokens(output = word, input = text) %>%
    anti_join(stop_words2, by="word") %>%
    count(word, sort = TRUE)
  
  wordcloud2(word_frequencies, shape = "star")

}

dscore(trump_data)
dscore(biden_data)
