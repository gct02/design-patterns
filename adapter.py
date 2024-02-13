class RoundHole:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        self._radius = radius

    def fits(self, round_peg):
        return True if round_peg.radius <= self.radius else False

class RoundPeg:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        self._radius = radius

class SquarePeg:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side
    
    @side.setter
    def radius(self, side):
        self._side = side

class SquarePegAdapter(RoundPeg):
    def __init__(self, square_peg):
        self.__square_peg = square_peg
        super().__init__(square_peg.side / 2)

if __name__ == "__main__":
    round_role = RoundHole(4)

    small_round_peg = RoundPeg(2)
    large_round_peg = RoundPeg(5)

    small_square_peg = SquarePeg(4)
    large_square_peg = SquarePeg(10)

    small_square_peg_adapter = SquarePegAdapter(small_square_peg)
    large_square_peg_adapter = SquarePegAdapter(large_square_peg)

    assert(round_role.fits(small_round_peg) == round_role.fits(small_square_peg_adapter))
    assert(round_role.fits(large_round_peg) == round_role.fits(large_square_peg_adapter))