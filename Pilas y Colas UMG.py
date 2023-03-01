import timeit
import random
import queue

numbers = [random.randint(-10000000, 10000000) for _ in range(1000000)]

def process_stack(numbers):
    stack = []
    for number in numbers:
        stack.append(number)

    while len(stack) > 0:
        number = stack.pop()

def process_queue(numbers):
    q = queue.Queue()
    for number in numbers:
        q.put(number)

    while not q.empty():
        number = q.get()

stack_time = timeit.timeit(lambda: process_stack(numbers), number=1)
queue_time = timeit.timeit(lambda: process_queue(numbers), number=1)

print("Tiempo de ejecución de la función de pila:", stack_time)
print("Tiempo de ejecución de la función de cola:", queue_time)
