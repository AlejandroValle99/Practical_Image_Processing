import matplotlib.pyplot as plt

def display_image(plotName, image, cmap = None):
    plt.figure(figsize=(10,5))
    plt.subplot(1,1,1)
    plt.imshow(image, cmap=cmap)
    plt.title(plotName)
    