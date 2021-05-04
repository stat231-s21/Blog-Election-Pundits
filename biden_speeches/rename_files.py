import os

file_names = os.listdir(".")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_nums = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

for file_name in file_names:
    parts = file_name.split(" ")
    if parts[0] not in months: # not a speech file
        continue
    month_index = months.index(parts[0])
    month_num = month_nums[month_index]
    year = parts[2].split(".")[0]
    year_abbr = year[2:]
    day = parts[1][:-1]
    new_name = month_num + "-" + day + "-" + year_abbr + ".txt"
    os.rename(file_name, new_name)
