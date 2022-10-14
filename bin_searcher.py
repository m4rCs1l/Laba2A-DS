# Вариант с составлением случайного массива:
from random import randint
arr1 = []
for i in range(randint(5, 15)):
    arr1.append(randint(-50, 50))

# Вариант с фиксированнным массивом:
#arr = [13, 6, 3, 4, 5, 2, 7, 8, 9, 10, 11, 12, 1]

arr1.sort()

# Счетчик шагов:
flag = 0
flag1 = True

print(arr1)

num = int(input('Введите искомое число: '))


arr = arr1
while len(arr) != 1:

    if arr[len(arr) % 2 + len(arr) // 2 - 1] == num:
        flag += 1
        break
    if arr[len(arr) % 2 + len(arr) // 2 - 1] < num:
        arr = arr[(len(arr) % 2 + len(arr) // 2):]
        flag += 1
    if arr[len(arr) % 2 + len(arr) // 2 - 1] > num:
        arr = arr[:(len(arr) % 2 + len(arr) // 2)]
        flag += 1

else:

    if arr[0] == num:
        flag + 1
    else:
        print('Элемент не содержится в массиве')
        flag1 = False

if flag1:
    print(f'Элемент найден через шагов: {flag}')



