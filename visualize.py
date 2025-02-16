import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

visualizationData = np.load("data/visualization.npz")
y = visualizationData["y"]
latentSpaces = visualizationData["latent3d"]

labelsTitles = ["T-shirt","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]
unique_labels = np.unique(y)
colors = ["blue", "orange", "green", "red", "purple", "brown", "pink", "gray", "yellow", "cyan"]


#Describin the data
plt.subplot(1, 3, 1)
plt.hist(latentSpaces[:, 0], bins=30)
print(np.mean(latentSpaces[:, 0]))
plt.subplot(1, 3, 2)
plt.hist(latentSpaces[:, 1], bins=30)
print(np.mean(latentSpaces[:, 1]))
plt.subplot(1, 3, 3)
plt.hist(latentSpaces[:, 2], bins=30)
print(np.mean(latentSpaces[:, 2]))
plt.tight_layout()
plt.show()


for stage in range(10):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    for i, label in enumerate(unique_labels):
        if i > stage: break
        mask = (y == label)
        ax.scatter(latentSpaces[mask, 0], latentSpaces[mask, 1], latentSpaces[mask, 2],
                    color=colors[i], label=labelsTitles[label], alpha=0.5)
    ax.legend()
    plt.show()