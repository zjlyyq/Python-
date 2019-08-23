d = {'mike': 10, 'lucy': 2, 'ben': 30}
print(d.items())
print(sorted(d.items(),key=lambda x:x[1],reverse=True))
xs=range(1000000)
print(xs)