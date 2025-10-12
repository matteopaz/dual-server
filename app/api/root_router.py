"""Application API routes."""

from pkgutil import get_data
from fastapi import APIRouter
from fastapi import WebSocket
from PIL import Image
import math

root_router = APIRouter()

# Counter for requests
request_counter = 0

@root_router.get("/ping", summary="Service health probe")
async def pong() -> dict[str, str]:
    """Return a simple heartbeat response."""
    return {"message": "pong"}

@root_router.websocket("/stream")
async def stream(websocket: WebSocket):
    """Stream data from the client."""
    global request_counter
    
    await websocket.accept()
    print("WebSocket connection accepted")
    
    try:
        while True:
            data = await websocket.receive_bytes()
            request_counter += 1
            
            # Process the received bytes of uncompressed BGRA data
            print(f"Received {len(data)} bytes of data (request #{request_counter})")
            
            # Save image every 100 requests
            if request_counter % 100 == 0:
                try:
                    # Calculate image dimensions assuming square or common aspect ratio
                    # BGRA = 4 bytes per pixel
                    num_pixels = len(data) // 4
                    
                    # Try to determine width and height (assuming 16:9 or square)
                    # For now, let's assume square image or you can adjust based on your known dimensions
                    height = 982
                    width = num_pixels // height
                    
                    # Create image from BGRA data
                    # PIL expects RGBA, so we'll convert BGRA to RGBA
                    img = Image.frombytes('RGBA', (width, height), data, 'raw', 'BGRA')
                    img.save('incoming.png')
                    print(f"Saved image to incoming.png (request #{request_counter})")
                except Exception as img_error:
                    print(f"Error saving image: {img_error}")

            await websocket.send_text(f"Received {len(data)} bytes of data")  # Echo back the data for demonstration

    except Exception as e:
        print(f"WebSocket connection closed: {e}")
        await websocket.close()
