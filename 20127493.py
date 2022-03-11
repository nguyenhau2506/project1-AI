from ast import arguments
import imp
import turtle                    # import turtle library
import time
import sys
from sys import maxsize
import collections
from collections import deque
import heapq

grid5=[]
grill=[]
start=0
goal=0
# ve array
def creatArray(x,y):
    matrix = []
    for i in range(x+1):
        matrix.append([])
        if i==0 or i==x:  
            for j in range(y+1):
                matrix[i].append('+')
        else :
            for j in range(y+1):
                if j==0 or j==y:
                    matrix[i].append('+')
                else:
                    matrix[i].append(' ')

    return matrix

def bfs(grid, start,goal,width,height):
    wall='#'
    #clear=' '
    queue = collections.deque([[start]])
    seen = set([start])

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if y==goal[1] and x==goal[0]:
            return path

        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1),(x+1,y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
        #print(seen)

def readFile(filename):
        #obstacles_list=[]
        with open(filename) as rf:

            tmp=tuple(rf.readline().rstrip().split(' '))# lay dai va rong
            width=tmp[0]
            height=tmp[1]
            grill=creatArray(int(tmp[1]),int(tmp[0]))

            tmp=tuple(rf.readline().rstrip().split(' '))# lay diem bat dau va diem dich
            grill[int(tmp[1])][int(tmp[0])]='s'
            grill[int(tmp[3])][int(tmp[2])]='e'

            n = int(rf.readline().rstrip())# lay so lương cac da giac

            for i in range(0,n):
                tmp=tuple(rf.readline().rstrip().split(' '))

                for z in range(0,len(tmp)-2,2):
                    path=bfs(grill,(int(tmp[z]),int(tmp[z+1])),(int(tmp[z+2]),int(tmp[z+3])),int(width),int(height))#tim dg di ngan nhat
                    for cell in path:#bo vao array
                        grill[cell[1]][cell[0]]='+'
                path=bfs(grill,(int(tmp[0]),int(tmp[1])),((int(tmp[len(tmp)-2])),int(tmp[len(tmp)-1])),int(width),int(height))
                for cell in path:
                    grill[cell[1]][cell[0]]='+'
            return grill
                    
           
        

    

    

# Me cung
class Maze(turtle.Turtle):              # Dinh nghia Me cung
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # Hinh dang Me Cung Turtle
        self.color("white")             # Mau cua me Cung Turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)

# this is the class for the finish line - green square in the maze
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)





def setup_maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = -588 + (x * 24)         # move to the x location on the screen staring at -588
            screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

            if character == "+":
                maze.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                maze.stamp()                          # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))    # add coordinate to walls list

            if character == " " or character == "e":
                path.append((screen_x, screen_y))     # add " " and e to path list

            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)       # send green sprite to screen location
                end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()
class BFS:
    def search(x,y):
        frontier.append((x, y))
        solution[x,y] = x,y

        while len(frontier) > 0:          # exit while loop when frontier queue equals zero
            #sorted(frontier)              #note thử
            time.sleep(0)
            x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

            if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
                cell = (x - 24, y)
                solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
                #blue.goto(cell)        # identify frontier cells
                #blue.stamp()
                frontier.append(cell)   # add cell to frontier list
                visited.add((x-24, y))  # add cell to visited list

            if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
                cell = (x, y - 24)
                solution[cell] = x, y
                #blue.goto(cell)
                #blue.stamp()
                frontier.append(cell)
                visited.add((x, y - 24))
                #print(solution)

            if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
                cell = (x + 24, y)
                solution[cell] = x, y
                #blue.goto(cell)
                #blue.stamp()
                frontier.append(cell)
                visited.add((x +24, y))

            if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
                cell = (x, y + 24)
                solution[cell] = x, y
                #blue.goto(cell)
                #blue.stamp()
                frontier.append(cell)
                visited.add((x, y + 24))
            green.goto(x,y)
            green.stamp()
    def backRoute(x, y):
        yellow.goto(x, y)
        yellow.stamp()
        count=1
        while (x, y) != (start_x, start_y): 
            yellow.goto(solution[x, y])
            yellow.stamp()
            x, y = solution[x, y]
            count=count+1
        turtle.goto(100,100)
        turtle.color('white')
        style = ('Courier', 15, 'italic')
        turtle.write('cost:'+str(count), font=style, align='center')
        


class UCS:# same bfs beacause the maze is unweight
    def search(x,y):
        heapq.heappush(Pfrontier,(0,(x,y))) #priority queue  0  distance start
        #frontier.append((x, y))
        solution[x,y] = x,y

        while len(Pfrontier) > 0:          
            time.sleep(0)
            dis,(x, y) = heapq.heappop(Pfrontier)
            if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
                cell = (x - 24, y)
                solution[cell] = x, y
                blue.goto(cell)      
                blue.stamp()
               
                heapq.heappush(Pfrontier,(dis+1,cell))
                visited.add((x-24, y)) 

            if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
                cell = (x, y - 24)
                solution[cell] = x, y
                blue.goto(cell)
                blue.stamp()
                heapq.heappush(Pfrontier,(dis+1,cell))
                
                visited.add((x, y - 24))
                #print(solution)

            if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
                cell = (x + 24, y)
                solution[cell] = x, y
                blue.goto(cell)
                blue.stamp()
                #frontier.append(cell)
                heapq.heappush(Pfrontier,(dis+1,cell))
                visited.add((x +24, y))

            if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
                cell = (x, y + 24)
                solution[cell] = x, y
                blue.goto(cell)
                blue.stamp()
                #frontier.append(cell)
                heapq.heappush(Pfrontier,(dis+1,cell))
                visited.add((x, y + 24))
            green.goto(x,y)
            green.stamp()
    def backRoute(x, y):
        yellow.goto(x, y)
        yellow.stamp()
        count=1
        while (x, y) != (start_x, start_y):
            yellow.goto(solution[x, y])
            yellow.stamp()
            x, y = solution[x, y]
            count=count+1
        turtle.goto(100,100)
        turtle.color('white')
        style = ('Courier', 15, 'italic')
        turtle.write('cost:'+str(count), font=style, align='center')


class IDS:
    def BFS(grid,x,y,maxdedth):
        if (x,y) == (end_x, end_y): 
                yellow.stamp()            
        
        frontier.append((maxdedth,(x, y)))           
        visited=[]
        solution.clear()
        solution[x, y] = x, y                                
        while len(frontier) > 0:                           
            (lev,(x, y)) = frontier.pop()            
            time.sleep(0)
            current = (x,y)
            if (x,y)==(end_x,end_y):
                return True
            if lev==0:
                continue
            if(x - 24, y) in path and (x - 24, y) not in visited:  # check left
                #print("check left")
                cellleft = (x - 24, y)
                solution[cellleft] = x, y  
                blue.goto(cellleft)  
                blue.stamp()               
                frontier.append((lev-1,cellleft)) 

            if (x, y - 24) in path and (x, y - 24) not in visited:  # check down
                #print("check down")
                celldown = (x, y - 24)
                solution[celldown] = x, y 
                blue.goto(celldown)
                blue.stamp()
                frontier.append((lev-1,celldown))

            if(x + 24, y) in path and (x + 24, y) not in visited:   # check right
                
                cellright = (x + 24, y)
                solution[cellright] = x, y 
                blue.goto(cellright)
                blue.stamp()
                frontier.append((lev-1,cellright))

            if(x, y + 24) in path and (x, y + 24) not in visited:  # check up
           
                cellup = (x, y + 24)
                solution[cellup] = x, y  
                blue.goto(cellup)
                blue.stamp()
                frontier.append((lev-1,cellup))
            

            visited.append(current)
            green.goto(x,y)
            green.stamp()
            if (x,y) == (end_x, end_y):
                yellow.stamp()        
            if (x,y) == (start_x, start_y): 
                red.stamp()                 
    def search(G, x,y):
        found = False
        depth=0
        
        while not found :
            depth =depth+10
            found = IDS.BFS(G,x,y,depth)       
    def backRoute(x, y):

        red.goto(x, y)                      
        count=1
        yellow.stamp()

        while (x, y) != (start_x, start_y):
            yellow.goto(solution[x, y])
            yellow.stamp()
            x, y = solution[x, y]
            count=count+1

        turtle.goto(100,100)
        turtle.color('white')
        style = ('Courier', 15, 'italic')
        turtle.write('cost:'+str(count), font=style, align='center')

class gbfs:


    def mahattan(point):# tinh trong so
        data=tuple(point)
        return abs(end_x-data[0])+abs(end_y-data[1])


    def search(grid,x,y):
        heapq.heappush(Pfrontier,(maxsize,(x,y)))
        visited=[]
        solution[x, y] = x, y
        
        while len(Pfrontier)> 0:
            if(x,y)==(end_x,end_y):
                break

            tmp,(x,y)=heapq.heappop(Pfrontier)
            time.sleep(0)
            current = (x,y)

            if(x - 24, y) in path and (x - 24, y) not in visited:  # check left
                #print("check left")
                check =False
                cellleft = (x - 24, y)
                solution[cellleft] = x, y
                blue.goto(cellleft)
                blue.stamp()
                distance=gbfs.mahattan(cellleft)

                for i in Pfrontier:
                    #print("test 2")
                    dis,cell=i
                    if(celldown==cell):
                        #print("test3")
                        if(distance<=dis):
                            #print("test4")
                            Pfrontier.remove(i)
                            heapq.heappush(Pfrontier,(distance,cellleft))
                            check=True   
                if(check==False):
                    heapq.heappush(Pfrontier,(distance,cellleft))
        
            if (x, y - 24) in path and (x, y - 24) not in visited:  # check down
                #print("check down")
                check =False
                celldown = (x, y - 24)
                solution[celldown] = x, y 
                blue.goto(celldown)
                blue.stamp()
               
                distance=gbfs.mahattan(celldown)
                for i in Pfrontier:
                    #print("test 2")
                    dis,cell=i
                    if(celldown==cell):
                        #print("test3")
                        if(distance<=dis):
                            #print("test4")
                            Pfrontier.remove(i)
                            heapq.heappush(Pfrontier,(distance,celldown))
                            check=True   
                if(check==False):
                    heapq.heappush(Pfrontier,(distance,celldown))

            if(x + 24, y) in path and (x + 24, y) not in visited:   # check right
                #print('check right')
                check =False
                cellright = (x + 24, y)
                solution[cellright] = x, y 
                blue.goto(cellright)
                blue.stamp()
                
                distance=gbfs.mahattan(cellright)
                for i in Pfrontier:
                        #print("test 2")
                        dis,cell=i
                        if(celldown==cell):
                            #print("test3")
                            if(distance<=dis):
                                #print("test4")
                                Pfrontier.remove(i)
                                heapq.heappush(Pfrontier,(distance,cellright))
                                check=True   
                if(check==False):
                        heapq.heappush(Pfrontier,(distance,cellright))

            if(x, y + 24) in path and (x, y + 24) not in visited:  # check up
                #print('check up')
                check =False
                cellup = (x, y + 24)
                solution[cellup] = x, y 
                blue.goto(cellup)
                blue.stamp()
                
                distance=gbfs.mahattan(cellup)
                for i in Pfrontier:
                    #print("test 2")
                    dis,cell=i
                    if(celldown==cell):
                    
                        if(distance<=dis):
                            #print("test4")
                            Pfrontier.remove(i)
                            heapq.heappush(Pfrontier,(distance,cellup))
                            check=True   
                if(check==False):
                    heapq.heappush(Pfrontier,(distance,cellup))

            visited.append(current)
            green.goto(x,y)
            green.stamp()
            if (x,y) == (end_x, end_y):
                yellow.stamp()
            if (x,y) == (start_x, start_y):
                red.stamp() 

    def backRoute(x, y):
       
        red.goto(x, y)                      
        yellow.stamp()
        count=1
        while (x, y) != (start_x, start_y):
            yellow.goto(solution[x, y])
            yellow.stamp()
            x, y = solution[x, y]
            count=count+1
        turtle.goto(100,100)
        turtle.color('white')
        style = ('Courier', 15, 'italic')
        turtle.write('cost:'+str(count), font=style, align='center')
class AStart:

    def mahattan(point):
        data=tuple(point)
        return abs(end_x-data[0])+abs(end_y-data[1])


    def search(grid,x,y):
        heapq.heappush(Pfrontier,(0,maxsize,(x,y)))# priority queue
        visited=[]
        solution[x, y] = x, y 
        
        while len(Pfrontier)> 0:                           # loop until the Pfrontier list is empty
            if(x,y)==(end_x,end_y):
                break

            tmp,dis,(x,y)=heapq.heappop(Pfrontier)
            time.sleep(0)
            current = (x,y)

            if(x - 24, y) in path and (x - 24, y) not in visited:  # check left
                #print("check left")
                check =False
                cellleft = (x - 24, y)
                solution[cellleft] = x, y
                blue.goto(cellleft)
                blue.stamp()            
                distance=tmp+AStart.mahattan(cellleft)
                #print(distance)

                for i in Pfrontier:
                    #print("test 2")
                    temp,dis,cell=i
                    if(cellleft==cell):
                        #print("test3")
                        if(distance<=dis):
                            #print("test4")
                            Pfrontier.remove(i)
                            heapq.heappush(Pfrontier,(tmp+1,distance,cellleft))
                            check=True   
                if(check==False):
                    heapq.heappush(Pfrontier,(tmp+1,distance,cellleft))


            if (x, y - 24) in path and (x, y - 24) not in visited:  # check down
                #print("check down")
                check =False
                celldown = (x, y - 24)
                solution[celldown] = x, y  
                blue.goto(celldown)
                blue.stamp()
               
                distance=tmp+AStart.mahattan(celldown)
                for i in Pfrontier:
                    #print("test 2")
                    temp,dis,cell=i
                    if(celldown==cell):
                        #print("test3")
                        if(distance<=dis):
                            #print("test4")
                            Pfrontier.remove(i)
                            heapq.heappush(Pfrontier,(tmp+1,distance,celldown))
                            check=True   
                if(check==False):
                    heapq.heappush(Pfrontier,(tmp+1,distance,celldown))
            if(x + 24, y) in path and (x + 24, y) not in visited:   # check right
                #print('check right')
                check =False
                cellright = (x + 24, y)
                solution[cellright] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
                blue.goto(cellright)
                blue.stamp()
                
                distance=tmp+AStart.mahattan(cellright)
                for i in Pfrontier:
                    #print("test 2")
                    temp,dis,cell=i
                    if(cellright==cell):
                        #print("test3")
                        if(distance<=dis):
                            #print("test4")
                            Pfrontier.remove(i)
                            heapq.heappush(Pfrontier,(tmp+1,distance,cellright))
                            check=True   
                if(check==False):
                    heapq.heappush(Pfrontier,(tmp+1,distance,cellright))

            if(x, y + 24) in path and (x, y + 24) not in visited:  # check up
                #print('check up')
                check =False
                cellup = (x, y + 24)
                solution[cellup] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
                blue.goto(cellup)
                blue.stamp()
                
                distance=tmp+AStart.mahattan(cellup)
                for i in Pfrontier:
                    #print("test 2")
                    temp,dis,cell=i
                    if(cellup==cell):
                        #print("test3")
                        if(distance<=dis):
                            #print("test4")
                            Pfrontier.remove(i)
                            heapq.heappush(Pfrontier,(tmp+1,distance,cellup))
                            check=True   
                if(check==False):
                    heapq.heappush(Pfrontier,(tmp+1,distance,cellup))
            #i=i+1
            #maxdedth=maxdedth-1
            #print("i = "+str(i))

            visited.append(current)
            green.goto(x,y)
            green.stamp()
            if (x,y) == (end_x, end_y):
                yellow.stamp() 
            if (x,y) == (start_x, start_y):
                red.stamp()     

    def backRoute(x, y):              
       
        red.goto(x, y)                      
        count=1
        yellow.stamp()
        while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
            yellow.goto(solution[x, y])        # move the yellow turtle to the key value of solution ()
            yellow.stamp()                     # create solution path
            x, y = solution[x, y]              # "key value" now becomes the new key
            count=count+1
        turtle.goto(100,100)
        turtle.color('white')
        style = ('Courier', 15, 'italic')
        turtle.write('cost:'+str(count), font=style, align='center')

# ho tro 

def menu(grid5,val):
    if val==1:
        #print("1")
        BFS.search(start_x,start_y)
        BFS.backRoute(end_x,end_y)
    elif val==2:
        #print("2")
        UCS.search(start_x,start_y)
        UCS.backRoute(end_x, end_y)
    elif val==3:
        #print("3")
        IDS.search(grid5,start_x,start_y)
        IDS.backRoute(end_x, end_y)
    elif val==4:
        #print("4")
        gbfs.search(grid5,start_x,start_y)
        gbfs.backRoute(end_x,end_y)
    elif val==5:
        AStart.search(grid5,start_x,start_y)
        AStart.backRoute(end_x,end_y)

#input file
filename = input('Enter filename: ')
grid5=readFile(filename)

#
print("1.Breadth-first search\n")
print("2.Uniform-cost search\n")
print("3.Iterative deepening search\n")
print("4.Greedy-best first search \n")
print("5.Graph-search A*\n")
print("------------------&&---------------------")
val_=input(" please input the option do you want(1-5):")
val=int(val_)

#draw screen 
wn = turtle.Screen()               # Dinh nghia man hinh Turtle
wn.bgcolor("black")                # Chinh mau nen
wn.title("a maze with search")
wn.setup(1300,700)                 # Tao man hinh setup


# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
Pfrontier=[]
# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}                           # solution dictionary


# main program starts here ####
setup_maze(grid5)
menu(grid5,val)
wn.exitonclick()