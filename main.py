import random
import time
import BubbleSort
import QuickSort


Tiempos = []

for i in range (10):
    array = [random.randint(1,10000) for _ in range(10000)]
    for num in array:
        print(num)
    start = time.time()
    BubbleSort.bubbleSort(array)
    end = time.time()
    length = end - start
    Tiempos.append(length)

sum = 0
for tiempo in Tiempos:
    print(tiempo)
    sum += tiempo
prom = sum/10
print("El promedio de timepo de ejecucion fue de:")
print(prom)