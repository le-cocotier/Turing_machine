import os

def open_file(name):
    file = open(name + '.txt', 'r')
    read_file = file.read()
    prgm = []
    decoupage = read_file.split('\n')
    for i in range(len(decoupage)):
        prgm.append(decoupage[i].split(' '))
    file.close()    
    return prgm


class Run:
    def __init__(self):
        self.head_pos = 0
        self.entree = list(input("Initial tape: "))
        self.state = input('Initial state: ')

    def read(self, letter):
        if letter == '_':
            if self.entree[self.head_pos] != ' ':
                return False
        elif letter == '*':
            if self.entree[self.head_pos] == ' ':
                return False
        elif letter != self.entree[self.head_pos]:
            return False
        return True

    def write(self, letter):
        if letter == '_':
            self.entree[self.head_pos] == ' '
        elif letter != '*':
            self.entree[self.head_pos] = letter

    def move(self, direction):
        if direction == 'r':
            if self.head_pos < (len(self.entree) - 1):
                self.head_pos += 1
            else:
                self.entree += ' '
                self.head_pos += 1
        if direction == 'l':
            if self.head_pos > 0:
                self.head_pos -= 1
            else:
                self.entree.insert(0, ' ')

    def mod_state(self, state):
        if state == 'halt':
            print("Final tape: {}".format(''.join(self.entree)))
            quit()
        else:
            self.state = state

    def line(self, prgm):
        while 1:
            for i in range(len(prgm)):
                if prgm[i][0] == self.state:
                    lecture = self.read(prgm[i][1])
                    if lecture:
                        self.write(prgm[i][2])
                        self.move(prgm[i][3])
                        self.mod_state(prgm[i][4])
                        

program = open_file('prgm')
run = Run()
run.line(program)