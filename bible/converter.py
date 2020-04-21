import csv
import os
versenum = 54
all_files = os.listdir(str(versenum))

print(len(all_files))
print(csv)

pages=[]
verses = ''
for i in range(len(all_files)):
        file =  open(str(versenum)+"/"+all_files[i],encoding="utf-8")
        verse = file.readlines()
        pages.append(verse)
        file.close()
        
with open('verse'+str(versenum)+'.csv','w',newline='')as f:
    mywriter = csv.writer(f)
    mywriter.writerow(['text'])

    for x in pages:
        mywriter.writerow([x])



#print(pages[0])
sentences = str(pages[0])
sentences.replace('\n','')
sentences.replace(',','')
#print(type(sentences))
f.close()
