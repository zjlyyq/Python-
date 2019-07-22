import json

params = {
    'name': 'zjl',
    'age': 12,
    'school': 'zjgsu',
    'friends':['yyq','zyq']
}

json_str = json.dumps(params)

print('type of json_str is {},json_str is {}'.format(type(json_str),json_str))


json_obj = json.loads(json_str)
for key in json_obj:
     print(json_obj[key])


