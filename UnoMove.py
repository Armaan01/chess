class Move():
    def __init__(self):
        self.whose_move='white'
    def change_move(self):
        self.whose_move='white' if self.whose_move=='black' else 'white'