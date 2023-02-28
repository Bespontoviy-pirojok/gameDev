print("Введите последовательнсоть для сравнения:")
a = list(map(int, input().split()))
print("Последовательность для сравнения:", a)


print("Введите последовательность для сортировки:")
b = list(map(int, input().split()))
N = len(b)
for i in range(1, N):
    for j in range(i, 0, -1):
        if b[j] < b[j-1]:
            b[j],b[j-1]= b[j-1],b[j]
        else:
            break

print("Последовательность после сортировки:", b)

if a == b:
   print('Списки идентичны!')
else:
   print('Списки не идентичны!')
   result = list(set(a) ^ set(b))
   print("Симметричное отличие: ",result)

