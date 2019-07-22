import re

def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w]',' ',text)
    #转化为小写
    text = text.lower()
    # 生成所有单词的列表
    word_list = text.split(' ')
    # 去除空白单词
    word_list = filter(None,word_list)
    print(word_list)
    word_count = {}
    for word in word_list:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    # print(word_count)
    print(word_count.items())
    sorted_word_count = sorted(word_count.items(),key=lambda kv:kv[1],reverse=True)
    return sorted_word_count

    
with open('in.txt','r') as file:
    text = file.read()

word_frequent = parse(text)

with open('out.txt','w') as file_out:
        for word,frequent in word_frequent:
            file_out.write(word + ' ' + str(frequent) + '\n')