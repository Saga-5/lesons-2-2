import matplotlib.pyplot as plt
# библиотека matplotlib помогает создать график по указанным координатам
x = [-1, 2, 3, 4, 5]
y = [2, 3, 5, 7, -1]

plt.plot(x, y, label="Простая линия", color='red', marker='1')

plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title("Пример графика")

plt.legend()

plt.show()
