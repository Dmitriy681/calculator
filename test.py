
n = int(input())
l = []

srav = -1000

for i in range(n):
    x = input().split()
    l.append(x)

#левая часть
print('левая часть')
for i in range(n):
    for j in range(n):
        if int(i >= j) and int(i <= n - 1 -j):
            print(l[i][j])

print('правая часть')
#правая часть
for i in range(n):
    for j in range(n):
        if int(i <= j) and int(i >= n - 1 -j):
            print(l[i][j])

print('верхняя часть')
#верхняя часть
for i in range(n):
    for j in range(n):
        if int(i <= j) and int(i <= n - 1 -j):
            print(l[i][j])

print('нижняя часть')
#нижняя часть
for i in range(n):
    for j in range(n):
        if int(i >= j) and int(i >= n - 1 -j):
            print(l[i][j])