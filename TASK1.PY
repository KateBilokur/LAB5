def fibonacci(n):
  
  fib_list = [0, 1]
  while len(fib_list) < n:
    fib_list.append(fib_list[-1] + fib_list[-2])
  return fib_list

# Вводимо кількість елементів з клавіатури
n = int(input("Введіть кількість елементів послідовності Фібоначчі: "))

# Генеруємо послідовність Фібоначчі
fibonacci_sequence = fibonacci(n)

# Виводимо результат
print("Послідовність Фібоначчі:", fibonacci_sequence)
