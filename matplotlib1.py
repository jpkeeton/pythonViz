import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Stanford', 'Washington', 'Penn State', 'Nebraska', 'Hawaii', 'UCLA')
y_pos = np.arange(len(objects))
performance = [1, 8, 15, 12, 7, 9]

plt.bar(y_pos, performance, align='center', alpha=0.9)
plt.xticks(y_pos, objects)
plt.ylabel('Wins')
plt.title('NCAA Women\'s Volleyball Champs')

plt.show()
# plt.