library(rvest)
library(purrr)

  url_base <- "https://www.rev.com/blog/transcript-tag/joe-biden-transcripts/page/"
  
  speechTitles <- read_csv("~/git/Stat231/Joe Biden speeches/titles.txt") %>%
    mutate(first_line = str_replace_all(tolower(Speech_Titles), " ", "-"),
           first_url = paste0("https://www.rev.com/blog/transcripts/", first_line))
  speechTitles
  
  write_csv(speechTitles, "speechTitles.csv")
  
  speechTitles <- read_csv("speechTitles.csv")
 
   map_df(80:255, function(i) {
        
         # simple but effective progress indicator
         cat(".")
         
           # identify webpage URL you want to scrape
           sept_bac_url <- speechTitles$first_url[i]
           
           date <- (sept_bac_url %>%               
                      read_html() %>%
                      html_nodes("div p")%>%   
                      html_text)[1] 
           sept_bac_text <- (sept_bac_url %>%               
                               read_html() %>%
                               html_nodes(".fl-callout-text")%>%   
                               html_text)[1] %>%
             strsplit(split = "\n") %>%
             unlist() %>%
             .[. != ""]
           # str_replace_all(pattern = "\t", replacement = NA_character_) %>%
           # str_replace_all(pattern = "  \t", replacement = NA_character_)
           # str_replace_all(pattern = "   ", replacement = NA_character_)
           
           
           sept_bac_text
           # date
           cat(sept_bac_text, file = paste0("~/git/Stat231/Joe Biden speeches/", date,".txt"))
           # cat(sept_bac_text)
              
             }) -> titles