import pandas as pd
file_name = "reports.xls"

df = pd.read_excel(io=file_name)

title = []
url = []
src = []
platform = []
sequence = []

for elem in df["title"]:
    title.append(elem)
for elem in df["url"]:
    url.append(str(elem))
for elem in df["src"]:
    res = str(int(elem))
    src.append("/assets/reports/"+ res +".jpg")
    print(res)
for elem in df["platform"]:
    platform.append(elem)

for i in range(6):
    write_to_file = "report_" + str(i+1) + ".md"
    file = open(write_to_file, 'w+')
    file.write("---\n")
    
    file.write("title: " + title[i] + '\n')
    file.write("url: " + url[i] + '\n')
    file.write("src: "+ src[i] +'\n')
    file.write("platform: " + platform[i] + '\n')
    file.write("sequence: " + str(i+1) + '\n')
    file.write("---" + '\n')
    file.close()