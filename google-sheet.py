from googlesearch import search
import pandas
import re

excel_data_df = pandas.read_excel('input_googlesearch.xlsx')

key = excel_data_df['Name'].tolist()

print(key)


print("Đang tìm")

ketqua = []
tukhoa = []

for i in range(len(key)):
      for j in search(key[i], tld="co.in", num=5, stop=5, pause=3):
        print(key[i]+": " +j)
        ketqua.append(j+"+"+key[i])
   
# print(ketqua)

# names = ['mixi', 'game']
# texts = ['game24.com', 'mixiqiqw','gameqwqw']

matched = {n: [] for n in key}

for text in ketqua:
    for name in key:
        if name in text:
            matched[name].append(text)
      
# print (matched)

df_data = pandas.DataFrame(matched)


df_data.to_excel('ketquatimkiem.xlsx')  
print('Save to Excel file successfully.')