
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('x_y_coordinates.txt', sep=',', header=None, names=['x', 'y'])

print("Data structure:", dataset.columns.tolist())
figure, ax = plt.subplots()
ax.scatter(dataset['x'], dataset['y'])
ax.set_title('Coordinate Scatter Plot')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.grid(True)
plt.show()
