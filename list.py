# 列表解析
import os

for item in range(1,21):
    print(item)

arr = range(1,1000000)
#for item in arr:
#    print(item)

print(sum(arr))

js = range(1,20,2)
#for item in js:
#    print(item)

for item in range(3,31,3):
    print(item)

squre = [value**3 for value in range(1,10)]
print(squre)

files = [file for file in os.listdir('./') if file.endswith('.py')]
print(files)


num = [1,3,5,2,351,452,135,1245,2,45,1123,1235,1]
num.sort(reverse=True)
print(num[:3])