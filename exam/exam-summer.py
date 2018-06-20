import os 
location = os.listdir("C:\\Users\\Дурдом\\Desktop\\exam\\news")
counter = 0 
xhtmlfiles = [] 

for file in os.listdir(location):
    try:
        if file.endswith(".xthml"):
            print ("xtml file found:\t"), file
            csvfiles.append(str(file))
            counter = counter+1
    except BufferError:

        for filename in os.listdir(news):
            with open("filename.xhtml", "r", encoding='windows-125') as f:
                text = f.read()
                text = re.sub("^[А-Яа-я.,?!-'], "",text")
