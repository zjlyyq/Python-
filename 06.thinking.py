# 尝试书写超大txt文档词评统计

import re
import time

def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w]',' ',text)
    #转化为小写
    text = text.lower()
    # 生成所有单词的列表
    word_list_sub = text.split(' ')
    # 去除空白单词
    word_list_sub = filter(None,word_list_sub)
    print(word_list_sub)
    for word in word_list_sub:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1

startTime = time.perf_counter()
word_count = {}
with open('The Elephant Man and Other Reminiscences.txt','r',encoding='UTF-8') as file:
    for line in file:
        parse(line)
    sorted_word_count = sorted(word_count.items(),key=lambda kv:kv[1],reverse=True)
    word_frequent =  sorted_word_count



with open('out.txt','w') as file_out:
        for word,frequent in word_frequent:
            file_out.write(word + ' ' + str(frequent) + '\n')

endTime = time.perf_counter()
print('运行时长：{}秒'.format((endTime-startTime)/1000))