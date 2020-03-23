import pandas
import numpy as np
import io

emp_df = pandas.read_csv('FinaleDataUTF.csv', usecols=['id','text_x', 'text_y'])

for index, row in emp_df.iterrows():
    # print(row['text_x'], row['text_y'])
    if index == 1438:
       continue
    text_y = '\n\n'.join(row['text_y'].split('.'))
    text_x = '\n\n@highlight\n\n' + row['text_x']
    text_x = '\n\n@highlight\n\n'.join(text_x.split('.'))
    # print(text_y)
    output_text =  text_y + text_x
    # print(output_text)
    path = "arabicTestStories\\"
    file1 = io.open(path+row['id']+".story","w" , encoding="utf-8")
    file1.write(output_text)
    print("file written  :" + str(index))
    
    
