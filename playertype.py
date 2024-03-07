from Characteristics import HP, Statset

class Warrior(HP, Statset):
    HPGROWTH = 19
    SHIELDHPGROWTH = 19
    BASESTR = 20
    BASEINT = 3
    BASEMP = 10
    BASEDEX = 8
    BASEC = 0
    BASEL = 3

    def __init__(self):
        HP.__init__(self, self.HPGROWTH, self.SHIELDHPGROWTH)
        Statset.__init__(self, self.BASESTR, self.BASEINT, self.BASEDEX, self.BASEMP, self.BASEC, self.BASEL)



class Support(HP, Statset):
    HPGROWTH = 9
    SHIELDHPGROWTH = 19
    BASESTR = 9
    BASEINT = 19
    BASEMP = 18
    BASEDEX = 8
    BASEC = 1
    BASEL = 5

    def __init__(self):
        HP.__init__(self, self.HPGROWTH, self.SHIELDHPGROWTH)
        Statset.__init__(self, self.BASESTR, self.BASEINT, self.BASEDEX, self.BASEMP, self.BASEC, self.BASEL)



class Assassin(HP, Statset):
    HPGROWTH = 19
    SHIELDHPGROWTH = 8
    BASESTR = 19
    BASEINT = 15
    BASEMP = 1
    BASEDEX = 19
    BASEC = 19
    BASEL = 5

    def __init__(self):
        HP.__init__(self, self.HPGROWTH, self.SHIELDHPGROWTH)
        Statset.__init__(self, self.BASESTR, self.BASEINT, self.BASEDEX, self.BASEMP, self.BASEC, self.BASEL)



class Tank(HP, Statset):
    HPGROWTH = 15
    SHIELDHPGROWTH = 19
    BASESTR = 14
    BASEINT = 10
    BASEMP = 10
    BASEDEX = 5
    BASEC = 0
    BASEL = 1

    def __init__(self):
        HP.__init__(self, self.HPGROWTH, self.SHIELDHPGROWTH)
        Statset.__init__(self, self.BASESTR, self.BASEINT, self.BASEDEX, self.BASEMP, self.BASEC, self.BASEL)



class Thief(HP, Statset):
    HPGROWTH = 9
    SHIELDHPGROWTH = 5
    BASESTR = 20
    BASEINT = 3
    BASEMP = 10
    BASEDEX = 8
    BASEC = 0
    BASEL = 19

    def __init__(self):
        HP.__init__(self, self.HPGROWTH, self.SHIELDHPGROWTH)
        Statset.__init__(self, self.BASESTR, self.BASEINT, self.BASEDEX, self.BASEMP, self.BASEC, self.BASEL)
