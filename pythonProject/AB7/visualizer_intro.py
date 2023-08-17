import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot3D([2, 3], [4, 5], [1, 5], "-xk")
ax.plot3D([3, 6], [5, 1], [5, 0], "-xk")
ax.plot3D([6, 2], [1, 4], [0, 1], "-xk")
plt.show()

