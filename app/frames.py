class Frames:
    def __init__(self):
        self.data=[]

    data: list[list[list[int, int, int]]] = []
    def set_last_frames(self, frames: list[list[list[int, int, int]]]):
        self.data = frames
    def get_last_frames(self):
        return self.data
    