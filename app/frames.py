import cv2

class Frames:
    def __init__(self):
        self.data=None

    data = None
    def set_last_frames(self, data):
        self.data = data
    def get_last_frames(self) -> list[list[list[int, int, int]]]:
        if(self.data is None):
            return []
        
        frames = cv2.cvtColor(self.data, cv2.COLOR_BGR2RGB).tolist()
        return frames
        
    