import numpy

from Cell import CellFactory


class Player:
    __slots__ = "board", "mine", "oppo"

    def __init__(self, player):
        self.mine = colour
        self.oppo = "@" if colour == "O" else "O"

        # initialise of board
        self.board = numpy.full((8, 8), CellFactory.create('-'), numpy.object)
        self.board[[(0, 0), (0, 7), (7, 0), (7, 7)]] = CellFactory.create('X')

        # maximum 12 pieces
        self.pieces = {'O': [None] * 12, '@': [None] * 12}
        self.num_pieces = {'O': 0, '@': 0}

        # for board shrinking
        self.turn = 0
        self.border = 0

    def _check_elim(self, row, col):
        pass

    def _delete_rec(self, row, col):
        p = self.board[(row, col)]
        self.pieces[p.sym][p.num] = None
        self.num_pieces[p.sym] -= 1

    def _shrink(self):
        for i in range(self.border, 8 - self.border):
            numpy.apply_over_axes
        self.border += 1

    def action(self, turns):
        pass

    def update(self, action):
        pass
