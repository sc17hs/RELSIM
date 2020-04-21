import csv
import os

all_files = os.listdir("files")                  #change file directory name as appropriate
pages=[]
verse = ''
bible = ''

for i in range(len(all_files)):
        verse = ''
        print(all_files[i])
        file =  open('files/'+str(all_files[i]),encoding = "utf-8")            #changes directory name as appropriate
        for lines in file:
                if lines.startswith("Chapter"):                                #removes the new chapter lines as this is not relevant. 
                        pass
                else:
                        verse = verse + lines
        pages.append(verse)
        file.close()
        
#print(len(pages))
for x in pages:
        bible = bible + x
        
with open('example.csv','w',newline='')as f:                                   #change filename as appropriate. 
    mywriter = csv.writer(f)
    mywriter.writerow(['text'])
    for x in pages:
            mywriter.writerow([x])


f.close()
