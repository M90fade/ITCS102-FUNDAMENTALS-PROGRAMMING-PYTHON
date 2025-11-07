#append
utang = ['candy', 'asukal', 'pancit canton', 'toyo', 'suka', 'bigas']

utang.append('asin')
print(utang)
utang.pop()
print(utang)
utang.append('paminta')
print(utang)

for u in utang:
    print(f"{u}, pang hanap buhay")

fullname = 'Moses D. Faderagao'

another = list(fullname)
#another reverse
print(another)