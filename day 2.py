#length = int(input('how long is the list: '))
#list_1 = []
#for i in range(1, length + 1):
#    item = int(input())
#    list_1.append(item)
#list_2 = list_1
#print(last_item)
#for i in range(len(list_1) - 1):
#    if i == len(list_1) - 1:
#        list_2[i], list_2[0] = list_1[i - 1], list_1[i]
#        print(list_2)
#    else:
#        list_2[i], list_2[i + 1] = list_1[i - 1], list_1[i]
#        print(list_2)
#print(list_2)

length = int(input('how long is the list: '))
list_1 = []
for i in range(1, length + 1):
    item = input()
    list_1[i] = item
    print(list_1)
list_1 = [1, 2, 3, 4, 5]
list_2 = list_1[:]
print(list_1)
for i in range(0, len(list_1)):
    list_2[i] = list_1[i - 1]
    print('list 1:', list_1)
    print('list 2:', list_2)
print('Final answer', list_2)
