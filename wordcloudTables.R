library(tidyverse) 
library(janitor)

library(tidytext)
library(wordcloud)
library(textdata)

# Put in your actual path where the text files are saved
mypath = "~/git/Blog-Election-Pundits/trump_speeches"
setwd(mypath)

# Create list of text files
txt_files_ls = list.files(path=mypath, pattern="*.txt") 
# Read the files in, assuming comma separator
txt_files_df <- lapply(txt_files_ls, 
                       function(x) {data.frame(title=substr(x,1,nchar(x)-4), 
                                               text=read_file(x))})
# Combine them
speeches_df <- do.call("rbind", lapply(txt_files_df, as.data.frame))
write.csv(speeches_df,
          "~/git/Blog-Election-Pundits/trump_speeches/trump_speeches_wordcloud.csv")


