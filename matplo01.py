import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Line Graph

#x = np.arange(0,10,0.1)
#y = np.sin(x)

#plt.plot(x,y)
#plt.title("Sine Wave Example")
#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
#plt.show()

#print("Done")

# x = np.random.randn(100) #array of 100 random elements

# Scatter Plot

# y = x * 0.5 + np.random.randn(100) * 0.2
# plt.scatter(x,y)
# plt.title("Scatter Plot Example")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# Bar Plot

# categories = ['A', 'B', 'C']
# values = [10, 25, 7]
# plt.bar(categories, values)
# plt.title("Bar Plot Example")
# plt.ylabel("Count")
# plt.show()

# Histogram

# data = np.random.randn(1000)
# plt.hist(data, bins=30) # bins is sub divisions
# plt.title("Histogram Example")
# plt.xlabel("Values")
# plt.ylabel("Frequencies")
# plt.show()

# Sub Plots

x = np.random.randn(100)
y = x * 0.5 + np.random.randn(100) * 0.2
data = np.random.randn(1000)

fig, axs = plt.subplots(1,2, figsize=(10,4))

axs[0].scatter(x,y)
axs[0].set_title("Scatter Plot")

axs[1].hist(data, bins = 20)
axs[1].set_title("Histogram")

plt.tight_layout()
plt.show()