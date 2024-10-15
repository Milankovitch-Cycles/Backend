import io
from fastapi import Response

def get_image(plt):
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()  
    
    return Response(content=buffer.getvalue(), media_type="image/png")