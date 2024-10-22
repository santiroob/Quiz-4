#Quicksort Tests
import random
import time
import QuickSort


Tiempos = []

for i in range (10):
    array = [random.randint(1,100000) for _ in range(5000)]
    for num in array:
        print(num)
    start = time.time()
    QuickSort.quickSort(array,0,4999)
    end = (time.time())*(1)
    length = (end - start)
    Tiempos.append(length)

sum = 0
for tiempo in Tiempos:
    print(tiempo)
    sum += tiempo
prom = sum/10
print("El promedio de timepo de ejecucion fue de:")
print(prom)