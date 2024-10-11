from random import randint

class Die():
    '''表⽰⼀个骰⼦的类。'''

    def __init__(self, num_sides=6):
        '''骰⼦默认为6⾯。'''
        self.num_sides = num_sides

    def roll(self):
        '''返回⼀个位于1和骰⼦⾯数之间的随机值。'''
        return randint(1, self.num_sides)

