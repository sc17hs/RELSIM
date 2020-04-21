import csv
import os

#all_files = os.listdir(str(versenum))

#print(len(all_files))

def convert(versenum):
        pages=[]
        verses = ''
        for i in range(1):
                file =  open(str(versenum)+'.txt',"r",encoding="utf-8")
                for lines in file:
                        result = ''.join([i for i in lines if not i.isdigit()])
                        result.replace('|','')
                        pages.append(result)
                file.close()
        
        with open('quran2.csv','w',newline='')as f:
            mywriter = csv.writer(f)
            mywriter.writerow(['text'])

            for x in pages:
                mywriter.writerow([x])
        f.close()

convert(2)

