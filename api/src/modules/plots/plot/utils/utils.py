import base64
import io
from matplotlib import pyplot as plt

def create_image():
    buffer = io.BytesIO()
    
    with plt.ioff():
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        
    plt.close()
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return image_base64
