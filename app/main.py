import os
import sys
import asyncio
import logging

import cv2

from contextlib import asynccontextmanager
from fastapi import FastAPI

from .frames import Frames

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
sys.path.append(dname)
os.chdir(dname)

logger = logging.getLogger('uvicorn.error')

last_frames = Frames()

cap = cv2.VideoCapture(0)

fps = 12
size = (640, 480)
cap.set(cv2.CAP_PROP_FPS, fps)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])


async def bg_worker():

    while True:
        success, img = cap.read()
        cv2.imshow("image?", img)
        cv2.waitKey(1)

        if success:
            last_frames.set_last_frames(img)
            
        else:
            logger.info("camera error, it doesn't read")
        await asyncio.sleep(0.01)


@asynccontextmanager
async def lifespan(app: FastAPI):
    bg_task = asyncio.create_task(bg_worker())
    yield
    bg_task.cancel()

app = FastAPI(lifespan=lifespan)

@app.get("/last_frames")
def get_last_frames():

    return last_frames.get_last_frames()
