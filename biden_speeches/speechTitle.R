library(rvest)
library(purrr)

url_base <- "https://www.rev.com/blog/transcript-tag/joe-biden-transcripts/page/"

map_df(1:21, function(i) {
  
  # simple but effective progress indicator
  cat(".")
  
  # identify webpage URL you want to scrape
  sept_bac_url <- paste0(url_base,i)
  
  cat("Speech_Titles", file = '~/git/Stat231/Joe Biden speeches/titles.txt', sep = "\n", append = TRUE)
  
  # scrape text from the page
  # note that the html nodes argument is "div p" instead of "table"
  # and the addition of html_text
  sept_bac_text <- (sept_bac_url %>%               
                      read_html() %>%
                      html_nodes(".fl-post-grid")%>%   
                      html_text)[1] %>%
    strsplit(split = "\n") %>%
    unlist() %>%
    .[. != ""] %>%
    str_remove_all(pattern = "\t") %>%
    str_remove_all(pattern = "  ") %>%
    str_remove_all(pattern = "1 week ago") %>%
    str_remove_all(pattern = "2 weeks ago") %>%
    str_remove_all(pattern = "3 weeks ago") %>%
    str_remove_all(pattern = "4 weeks ago") %>%
    str_remove_all(pattern = "1 day ago") %>%
    str_remove_all(pattern = "2 days ago") %>%
    str_remove_all(pattern = "3 days ago") %>%
    str_remove_all(pattern = "4 days ago") %>%
    str_remove_all(pattern = "5 days ago") %>%
    str_remove_all(pattern = "6 days ago") %>%
    str_remove_all(pattern = "1 month ago") %>%
    str_remove_all(pattern = "2 months ago") %>%
    str_remove_all(pattern = "3 months ago") %>%
    str_remove_all(pattern = "4 months ago") %>%
    str_remove_all(pattern = "5 months ago") %>%
    str_remove_all(pattern = "6 months ago") %>%
    str_remove_all(pattern = "7 months ago") %>%
    str_remove_all(pattern = "8 months ago") %>%
    str_remove_all(pattern = "9 months ago") %>%
    str_remove_all(pattern = "10 months ago") %>%
    str_remove_all(pattern = "11 months ago") %>%
    str_remove_all(pattern = "12 months ago") %>%
    str_remove_all(pattern = "1 year ago") %>%
    str_remove_all(pattern = "2 years ago")
  # str_replace_all(pattern = "\t", replacement = NA_character_) %>%
  # str_replace_all(pattern = "  \t", replacement = NA_character_)
  # str_replace_all(pattern = "   ", replacement = NA_character_)
  
  
  sept_bac_text
  cat(sept_bac_text, file = '~/git/Stat231/Joe Biden speeches/titles.txt', sep = "\n", append = TRUE)
  # cat(sept_bac_text)
  
}) -> titles