import random #Модуль random управляет генерацией случайных чисел
mat = [-15, -4, -2 , -7, 0, 3, 5, 12, 7] #список
width = random.randint(4,8) #размер по ширине
height = random.randint(4,8) #размер по высоте
arr = []
for i in range(width):
    row =[]
    
 
    for a in range(height):
          row.append(random.choice(mat))
    arr.append(row)
        
    
print("матрица ")
for row in arr:
    for numb in row:
        print(f"{numb:4} " , end= "")
        print()
sum = 0
for row in arr:
    for value in row:
        if value%2 !=0:
            sum+=numb
print("ссума нечетных чисел ")

