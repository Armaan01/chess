class King():
    '''
        describing king`s properties
        self.x x coords
        self.y y coords
        colour - black or white
        '''
    def __init__(self,col):
        self.colour=col
        self.hitx=[]
        self.hity = []
        self.movex=self.hitx
        self.movey=self.hity
        if self.colour!='black':
            self.x=4
            self.y='A'
        else:
            self.x=4
            self.y='H'
    def update_pos(self,x,y,listhitx,listhity):
        self.x=x
        self.y=y
        self.hity=listhity
        self.hitx=listhitx
    def fixwith(self,x,y):
        self.x=x
        self.y=y

class Queen():
    '''
        describing queen`s properties
        self.x x coords
        self.y y coords
        colour - black or white
    '''
    def __init__(self,col):
        self.colour=col
        self.hitx = []
        self.hity = []
        self.movex=self.hitx
        self.movey=self.hity
        if self.colour!='black':
            self.x=5
            self.y='A'
        else:
            self.x=5
            self.y='H'
    def fixwith(self,x,y):
        self.x=x
        self.y=y
class Rock():
    '''
        describing rock`s properties
        self.x x coords
        self.y y coords
        colour - black or white
    '''
    def __init__(self,col,num):
        self.colour=col
        self.hitx = []
        self.hity = []
        self.movex=self.hitx
        self.movey=self.hity
        if self.colour!='black' and num==0:
            self.x=3
            self.y='A'
        elif num==1 and col!='black':
            self.x=6
            self.y='A'
        elif num==0:
            self.x=3
            self.y='H'
        else:
            self.x=6
            self.y='H'
    def fixwith(self,x,y):
        self.x=x
        self.y=y

class Knight():
    '''
        describing knight`s properties
        self.x x coords
        self.y y coords
        colour - black or white
    '''
    def __init__(self,col,num):
        self.colour=col
        self.hitx = []
        self.hity = []
        self.movex=self.hitx
        self.movey=self.hity
        if self.colour!='black' and num==0:
            self.x=2
            self.y='A'
            self.hity=[1,3]
            self.hitx=['C','C']
        elif num==1 and col!='black':
            self.x=7
            self.y='A'
            self.hity=[6,8]
            self.hitx=['C','C']
        elif num==0:
            self.x=2
            self.y='H'
            self.hity=[1,3]
            self.hitx=['F','F']
        else:
            self.x=7
            self.y='H'
            self.hity=[6,8]
            self.hitx=['F','F']
    def fixwith(self,x,y):
        self.x=x
        self.y=y
class Bishop():
    '''
        describing bishop`s properties
        self.x x coords
        self.y y coords
        colour - black or white
    '''
    def __init__(self,col,num):
        self.colour=col
        self.hitx = []
        self.hity = []
        self.movex = self.hitx
        self.movey = self.hity
        if self.colour!='black' and num==0:
            self.x=1
            self.y='A'
        elif num==1 and col!='black':
            self.x=8
            self.y='A'
        elif num==0:
            self.x=1
            self.y='H'
        else:
            self.x=8
            self.y='H'
    def fixwith(self,x,y):
        self.x=x
        self.y=y
class Pawn():
    '''
    describing pawn`s properties
    self.x x coords
    self.y y coords
    colour - black or white
    '''
    def __init__(self,col,num):
        self.colour=col
        self.hitx = []
        self.hity = []
        self.movex=[]
        self.movey=[num+1,num+1]
        self.moved=0
        if self.colour=='black':
            self.y='G'
            self.movex=['G','G']
            self.hity.append('F')
        else:
            self.y='B'
            self.movex=['B','B']
            self.hity.append('C')
        self.x=num+1
        if num==0:
            self.hitx.append(2)
        elif num==7:
            self.hitx.append(7)
        else:
            self.hitx.append(num)
            self.hitx.append(num+2)
            l=self.hity[0]
            self.hity.append(l)
    def fixwith(self,x,y):
        self.x=x
        self.y=y