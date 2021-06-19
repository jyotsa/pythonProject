word_count=input('Enter a word')
count_dic=dict()

for char in word_count:
    if char in count_dic.keys():
        count_dic[char]+=1
    else:
        count_dic[char]=1
print(count_dic)


