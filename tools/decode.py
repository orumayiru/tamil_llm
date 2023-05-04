with open('hindu_scrape.json','r',encoding ='utf-8') as f:
    data = f.readlines()
print(data)
decoded_text = []
for i in data:
    decoded_text.append(i.encode().decode('unicode-escape'))
print(decoded_text)
with open('hindu_scrape1.json','w',encoding ='utf-16') as f:
    f.writelines(decoded_text)