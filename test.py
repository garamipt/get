import numpy as np
import matplotlib.pyplot as plt
with open('settings.txt') as file2:
    sett = np.array(list(map(float, file2.read().split())))
with open('data.txt') as file1:
    data = np.array(list(map(int, file1.read().split()))) * sett[1]


time = sett[0] * np.arange(len(data))
#
fig, ax = plt.subplots()
#
# ax.plot(time, data)


ax.plot(time, data)
ax.legend(['V(t)'])
ax.scatter(time[::15], data[::15])

ax.minorticks_on()

ax.grid(which='major', lw=0.7)
ax.grid(which='minor', ls='--', lw=0.5)
ax.set_xlabel("Время, с")
ax.set_ylabel("Напряжение, В")
ax.set_title("Процесс разряда и заряда конденсатора в RC-цепочке")
#
# ax.legend(['V(t)', None])

ax.set_xlim([0, 12])
ax.set_ylim([0, 2.8])
ax.text(7, 2, "Время заряда = {:.4}c".format(str(time[data.argmax()])))
ax.text(7, 1.5, "Время разряда = {:.4}c".format(str(time.max() - time[data.argmax()])))
plt.show()