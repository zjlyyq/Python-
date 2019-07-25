# 以书写pythonic代码为荣


attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], 
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# expected outout:
[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}, 
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'}, 
{'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]



# 传统实现
for item in values:
    l = []
    index = 0
    for v in item:
            d = {}
            d[attributes[index]] = v
            l.append(d)
            index += 1
    print(l)
        

# pythonic实现
for item in values:
        l = [{p:v} for p in attributes for v in item if attributes.index(p) == item.index(v)]
        print(l)