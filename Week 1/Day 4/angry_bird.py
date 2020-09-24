class AngryBird:
    def __init__(self):
        super().__init__()
        self._x = 0
        self._y = 0

    def move_up_by(self, delta):
        self._y += delta

bird = AngryBird()
print(bird)
print(bird._y)
bird.move_up_by(40)
print(bird._y)