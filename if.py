arr = ["Apple", "name", "Hanmeiei"]

print('name' in arr)  # True

if 'apple' not in arr:
    print('apple not exist')  #apple not exist

brr = ['2']
if brr:
    print('true')
else:
    print('flase')

alines = {'lili': 'js', 'lilei': 'python', 'hanmeimei': 'php'}

print(alines)

for key, values in alines.items():
    print(values)

print(alines.keys())

i = 0
while (i <= 5):
    if (i == 4):
        print(i)
        break  # break退出循环
    i += 1

message = int(input('Say something please?\n'))
print(str(message) + '的二次方为:' + str(message**2))
