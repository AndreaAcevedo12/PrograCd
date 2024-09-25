#Slicing y for
l1 = [0,1,2,3,4,5,6,7,8,9]
x = 3
if x == 5:
    print("El valor es cinco")
else:
    print("El valor no es cinco :(")

    print(l1)   #aa

for elemento in l1:
    print("Elemento: ",elemento)

for i in range(10):# (0,.....,9)
    print("Elemento: ",i)

for i in range(3,7):# (3,.....,6)
    print("Elemento: ",i)

for i in range(0,10,2):# (3,.....,6)
    print("Elemento: ",i)

print (len(l1))

for i in range(9,-1,-2): #(9,9,7,6,5,4,3,2,1,0)
    print("Elemento: ",i)

print(l1[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] OMG, como va brincando de -1, ya sabe que inicia en el último (-1 :O)

print(l1[-2::-2]) #[8, 6, 4, 2, 0]

print(l1[-2::-3]) #[8, 5, 2]

print(l1[2::3]) #[2, 5, 8]

print(l1[-1::-4]) #[9, 5, 1]

print(l1[-2:-7:-2]) #[8, 6, 4]

for i in range(10):# (0,.....,9)
    print("Elemento: ",i)
else:
    print("TERMINOOOOÓ") #Escribe "Terminó cuando acaba, watefac"
#CUANDO ya NO se cumple la condición del for, ejecuta el else
#Solo puede servir para claridad en el codigo tho, sale igual poner el codigo inmediatamente despues del for y ya

