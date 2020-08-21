names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

print(names1)
print(names2)
print(names3)

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
        print('Alice: '+str(sum))
    if ls[1] == 'Bob':
        sum += 10
        print('Bob: '+str(sum))

print (sum)

# 19) What is the output, Suppose list1 is [1, 3, 2], What is list1 * 2?

list1 = [1,3,2]
print(list1*2)

# 20) What is the output when we execute list(“hello”)?

list2 = ("hello")
print(list2)