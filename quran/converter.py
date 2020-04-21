import csv
import os

all_files = os.listdir(".")

print(len(all_files))
pages=[]
quran = ''
def convert(versenum):
        full = ''
        file =  open(str(versenum)+'.txt',"r",encoding="utf-8")
        for lines in file:
                result = ''.join([i for i in lines if not i.isdigit()])
                #print(type(result))
                result = result[2::]
                full = full + result
        pages.append(full)
        file.close()
                


for x in range(1,115):
        print("converting" ,x)
        convert(x)
        
with open('religioustexts.csv','w',newline='')as f:
        mywriter = csv.writer(f)
        mywriter.writerow(['text'])

        for x in pages:
                quran = quran + x
        print(quran)
        mywriter.writerow([quran])
        f.close()


