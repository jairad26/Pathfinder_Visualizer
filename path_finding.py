
import time
import random
import pygame
import sys
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

screen = pygame.display.set_mode((800, 800))


class spot:
    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self.obs = False
        self.closed = False
        self.value = 1

    def show(self, color, st):
        if self.closed == False :
            pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
            pygame.display.update()

    def path(self, color, st):
        pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
        pygame.display.update()

    def addNeighbors(self, grid):
        i = self.i
        j = self.j
        if i < cols-1 and grid[self.i + 1][j].obs == False:
            self.neighbors.append(grid[self.i + 1][j])
        if i > 0 and grid[self.i - 1][j].obs == False:
            self.neighbors.append(grid[self.i - 1][j])
        if j < row-1 and grid[self.i][j + 1].obs == False:
            self.neighbors.append(grid[self.i][j + 1])
        if j > 0 and grid[self.i][j - 1].obs == False:
            self.neighbors.append(grid[self.i][j - 1])


cols = 50
grid = [0 for i in range(cols)]
row = 50
openSet = []
closedSet = []
newSet = []
raiseSet = []
lowerSet = []
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
w = 800 / cols
h = 800 / row
stack = []
visited = []

# create 2d array
for i in range(cols):
    grid[i] = [0 for i in range(row)]

# Create Spots
for i in range(cols):
    for j in range(row):
        grid[i][j] = spot(i, j)


# Set start and end node
start = grid[12][5]
end = grid[3][6]
# SHOW RECT
for i in range(cols):
    for j in range(row):
        grid[i][j].show((255, 255, 255), 1)

for i in range(0,row):
    grid[0][i].show(grey, 0)
    grid[0][i].obs = True
    grid[cols-1][i].obs = True
    grid[cols-1][i].show(grey, 0)
    grid[i][row-1].show(grey, 0)
    grid[i][0].show(grey, 0)
    grid[i][0].obs = True
    grid[i][row-1].obs = True

def onsubmit():
    global start
    global end
    global algName
    algName = algMenu.get()
    st = startBox.get().split(',')
    ed = endBox.get().split(',')
    start = grid[int(st[0])][int(st[1])]
    end = grid[int(ed[0])][int(ed[1])]
    window.quit()
    window.destroy()





window = Tk()
label = Label(window, text='Start(x,y): ')
startBox = Entry(window)
label1 = Label(window, text='End(x,y): ')
endBox = Entry(window)
var = IntVar()
showPath = ttk.Checkbutton(window, text='Show Steps :', onvalue=1, offvalue=0, variable=var)

selected_alg = StringVar()
Label(window, text = "Algorithm: ", bg = 'white').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
algMenu = ttk.Combobox(window, textvariable = selected_alg, values = ['A*', 'Best-First', 'Djikstras'])
algMenu.grid(row=0, column = 1, padx = 5, pady = 5)
algMenu.current(0)

submit = Button(window, text='Submit', command=onsubmit)



showPath.grid(columnspan=2, row=3)
submit.grid(columnspan=2, row=4)
label1.grid(row=2, pady=3)
endBox.grid(row=2, column=1, pady=3)
startBox.grid(row=1, column=1, pady=3)
label.grid(row=1, pady=3)

window.update()
mainloop()

pygame.init()
openSet.append(start)


def push_right(x):
    g1 = x.i+1
    g2 = x.j
    if(g1 > 0 and g1 < row-2 and g2 > 0 and g2 < cols-2):
        acess = grid[g1][g2]
        if acess != start and acess != end:
            if acess.obs == False:
                acess.obs = True
                acess.show((255, 255, 255), 0)

def push_left(x):
    g1 = x.i+1
    g2 = x.j
    if(g1 > 0 and g1 < row-2 and g2 > 0 and g2 < cols-2):
        acess = grid[g1][g2]
        if acess != start and acess != end:
            if acess.obs == False:
                acess.obs = True
                acess.show((255, 255, 255), 0)

def push_up(x):
    g1 = x.i
    g2 = x.j+1
    if(g1 > 0 and g1 < row-2 and g2 > 0 and g2 < cols-2):
        acess = grid[g1][g2]
        if acess != start and acess != end:
            if acess.obs == False:
                acess.obs = True
                acess.show((255, 255, 255), 0)

def push_down(x):
    g1 = x.i
    g2 = x.j-1
    if(g1 > 0 and g1 < row-2 and g2 > 0 and g2 < cols-2):
        acess = grid[g1][g2]
        if acess != start and acess != end:
            if acess.obs == False:
                acess.obs = True
                acess.show((255, 255, 255), 0)

def single_cell(x):
    g1 = x.i
    g2 = x.j
    if(g1 > 0 and g1 < row-2 and g2 > 0 and g2 < cols-2):
        acess = grid[g1][g2]
        if acess != start and acess != end:
            if acess.obs == False:
                acess.obs = True
                acess.show((255, 255, 255), 0)

def backtracking_cell(x):
    g1 = x.i
    g2 = x.j
    if(g1 > 0 and g1 < row-2 and g2 > 0 and g2 < cols-2):
        acess = grid[g1][g2]
        if acess != start and acess != end:
            if acess.obs == False:
                acess.obs = True
                acess.show((255, 255, 0), 0)


def carve_out_maze(x):
    single_cell(x)
    stack.append(x)
    visited.append(x)
    g1 = x.i
    g2 = x.j
    if(g1 > 0 and g1 < row-6 and g2 > 0 and g2 < cols-6):
        acess = grid[g1][g2]
        while len(stack) < 10000:
            cell = []
            if(grid[g1+1][g2] not in visited):
                cell.append("right")
            if(grid[g1-1][g2] not in visited):
                cell.append("left")
            if(grid[g1][g2+1] not in visited):
                cell.append("up")
            if(grid[g1][g2-1] not in visited):
                cell.append("down")
            if len(cell) > 0:
                cell_chosen = random.choice(cell)
                ranchoice = random.choice([3,4])
                if cell_chosen == "right":
                    push_right(x)
                    x.i = x.i + ranchoice
                    visited.append(x)
                    stack.append(x)
                elif cell_chosen == "left":
                    push_left(x)
                    x.i = x.i - ranchoice
                    visited.append(x)
                    stack.append(x)
                elif cell_chosen == "up":
                    push_up(x)
                    x.j = x.j + ranchoice
                    visited.append(x)
                    stack.append(x)
                elif cell_chosen == "down":
                    push_down(x)
                    x.j = x.j - ranchoice
                    visited.append(x)
                    stack.append(x)
            else:
                print("wegothere")
                x = stack.pop()
                single_cell(x)
                backtracking_cell(x)



def mousePress(x):
    t = x[0]
    w = x[1]
    g1 = t // (800 // cols)
    g2 = w // (800 // row)
    acess = grid[g1][g2]
    if acess != start and acess != end:
        if acess.obs == False:
            acess.obs = True
            acess.show((255, 255, 255), 0)

def oppMousePress(x):
    t = x[0]
    w = x[1]
    g1 = t // (800 // cols)
    g2 = w // (800 // row)
    acess = grid[g1][g2]
    if acess != start and acess != end:
        if acess.obs == True:
            acess.obs = False
            acess.show((0, 0, 0), 0)
            acess.show((255, 255, 255), 1)

end.show((255, 8, 127), 0)
start.show((255, 8, 127), 0)

afterstart = grid[24][24]

loop = True
while loop:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress(pos)
            except AttributeError:
                pass
        if pygame.mouse.get_pressed()[2]:
            try:
                pos = pygame.mouse.get_pos()
                oppMousePress(pos)
            except AttributeError:
                pass

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                loop = False
                break
            elif event.key == pygame.K_m:
                carve_out_maze(afterstart)
                print("finished")


for i in range(cols):
    for j in range(row):
        if(grid[i][j] != afterstart):
            grid[i][j].addNeighbors(grid)

def heurisitic(n, e):
    #d = math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)
    d = abs(n.i - e.i) + abs(n.j - e.j)
    return d * min(n.value, e.value)


def astar():
    end.show((255, 8, 127), 0)
    start.show((255, 8, 127), 0)
    if len(openSet) > 0:
        lowestIndex = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[lowestIndex].f:
                lowestIndex = i

        current = openSet[lowestIndex]
        if current == end:
            print('done', current.f)
            start.show((255,8,127),0)
            temp = current.f
            for i in range(round(current.f)):
                current.closed = False
                current.show((0,0,255), 0)
                current = current.previous
            end.show((255, 8, 127), 0)

            Tk().wm_withdraw()
            result = messagebox.askokcancel('Program Finished', ('The program finished, the shortest distance \n to the path is ' + str(temp) + ' blocks away.'))
            
            pygame.quit()

        openSet.pop(lowestIndex)
        closedSet.append(current)

        neighbors = current.neighbors
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if neighbor not in closedSet:
                tempG = current.g + current.value
                if neighbor in openSet:
                    if neighbor.g > tempG:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    openSet.append(neighbor)

            neighbor.h = heurisitic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h

            if neighbor.previous == None:
                neighbor.previous = current
    if var.get():
        for i in range(len(openSet)):
            openSet[i].show(green, 0)

        for i in range(len(closedSet)):
            if closedSet[i] != start:
                closedSet[i].show(red, 0)
    current.closed = True

def heurisiticbf(n, e):
    d = math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)
    return d * min(n.value, e.value)


def bestFirst(): 
    end.show((255, 8, 127), 0)
    start.show((255, 8, 127), 0)
    if len(openSet) > 0:
        lowestIndex = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[lowestIndex].f:
                lowestIndex = i

        current = openSet[lowestIndex]
        if current == end:
            print('done', current.g)
            start.show((255,8,127),0)
            temp = current.g
            for i in range(round(current.g)):
                current.closed = False
                current.show((0,0,255), 0)
                current = current.previous
            end.show((255, 8, 127), 0)

            Tk().wm_withdraw()
            result = messagebox.askokcancel('Program Finished', ('The program finished, the shortest distance \n to the path is ' + str(temp) + ' blocks away.'))
            
            pygame.quit()

        openSet.pop(lowestIndex)
        closedSet.append(current)

        neighbors = current.neighbors
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if neighbor not in closedSet:
                tempG = current.g + current.value
                if neighbor in openSet:
                    if neighbor.g > tempG:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    openSet.append(neighbor)

            neighbor.h = heurisiticbf(neighbor, end)
            neighbor.f = neighbor.h

            if neighbor.previous == None:
                neighbor.previous = current
    if var.get():
        for i in range(len(openSet)):
            openSet[i].show(green, 0)

        for i in range(len(closedSet)):
            if closedSet[i] != start:
                closedSet[i].show(red, 0)
    current.closed = True


def dijkstra(): 
    end.show((255, 8, 127), 0)
    start.show((255, 8, 127), 0)
    if len(openSet) > 0:
        lowestIndex = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[lowestIndex].f:
                lowestIndex = i

        current = openSet[lowestIndex]
        if current == end:
            print('done', current.f)
            start.show((255,8,127),0)
            temp = current.f
            for i in range(round(current.f)):
                current.closed = False
                current.show((0,0,255), 0)
                current = current.previous
            end.show((255, 8, 127), 0)

            Tk().wm_withdraw()
            result = messagebox.askokcancel('Program Finished', ('The program finished, the shortest distance \n to the path is ' + str(temp) + ' blocks away.'))
            
            pygame.quit()

        openSet.pop(lowestIndex)
        closedSet.append(current)

        neighbors = current.neighbors
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if neighbor not in closedSet:
                tempG = current.g + current.value
                if neighbor in openSet:
                    if neighbor.g > tempG:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    openSet.append(neighbor)

            neighbor.f = neighbor.g

            if neighbor.previous == None:
                neighbor.previous = current
    if var.get():
        for i in range(len(openSet)):
            openSet[i].show(green, 0)

        for i in range(len(closedSet)):
            if closedSet[i] != start:
                closedSet[i].show(red, 0)
    current.closed = True
    
   
def main():
    if(algName == 'A*'):
        astar()
    elif(algName == 'Djikstras'):
        dijkstra()
    elif(algName == 'Best-First'):
        bestFirst()



while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()
    main()