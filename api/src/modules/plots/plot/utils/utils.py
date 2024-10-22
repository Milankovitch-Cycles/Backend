import os
from matplotlib import pyplot as plt

def create_image(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    plt.savefig(path)
    plt.clf()
    
    return path
