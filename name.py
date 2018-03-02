name = "maliluya yamadie"
print(name.title())
print("\t" + name) #制表符
print("\n" + name) #换行符

age = 23
print("Happy imp"+str(age)+"rd Birthday")

arr = ["Apple","Cat","Biger","Animal","User","Dog","Money"]
print(arr)
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)
print(sorted(arr))

for item in arr:
    print(item)

numbers = range(1,10)
for item in numbers:
    print(item)

print(list(numbers))