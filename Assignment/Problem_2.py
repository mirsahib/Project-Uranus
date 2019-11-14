try:
    import Queue as Q
except:
    import queue as Q

class node(object):
    def __init__(self,nodeID,row,col,g_value,h_value,f_value,visited):
        self.nodeID = nodeID
        self.row = row
        self.col = col
        self.g_value = g_value
        self.h_value =  h_value
        self.f_value = f_value
        self.nodeCost = 0
        self.visited = visited
        self.predecessorCell = []
    def getNodeCost(self):
        return self.nodeCost
    def setNodeCost(self,cost):
        self.nodeCost = cost
    def getRow(self):
        return self.row
    def getCol(self):
        return self.col
    def setPredecessor(self,row,col):
        self.predecessorCell = [row,col]
    def getPredecessorCell(self):
        return self.predecessorCell
    def setVisited(self,visited):
        self.visited = visited
    def __lt__(self,other):
        return self.f_value<other.f_value
    def isVisited(self):
        return self.visited
    def __str__(self):
        return str(self.nodeID)+" "+str(self.row)+" "+str(self.col)+" "+str(self.g_value)+" "+str(self.h_value)+" "+str(self.f_value)+" "+str(self.visited)+" || "


class Graph(object):
    node_matrix = []
    q = Q.PriorityQueue()
    def __init__(self):
        self.rowAndColString = input("Enter row and col: ").split()
        self.rowAndColCell = list(map(int,self.rowAndColString))#[5,6]
        self.sourceInput = input("Enter source cell number: ").split()
        self.sourceCell = list(map(int,self.sourceInput))#[3,1]
        self.destinationInput = input("Enter destination cell number: ").split()
        self.destinationCell = list(map(int,self.destinationInput))#[3,4]
        self.blockLimit = int(input("Enter number of cell to be blocked: "))
        self.blockList = []#[[2,2],[4,2],[2,3],[3,3],[3,5],[4,5]]
        while self.blockLimit:
            cellInput = input("Enter cell number: ").split()
            cellInput = list(map(int,cellInput))
            self.blockList.append(cellInput)
            self.blockLimit=self.blockLimit-1
        self.nodeIdCount = 1
        #initializing the node matrix
        for i in range(0,self.rowAndColCell[0]):
            node_row = []
            for j in range(0,self.rowAndColCell[1]):
                hVal = abs(self.destinationCell[0]-1-i)*2 + abs(self.destinationCell[1]-1-j)*1 #l1 norm between destination to current cell
                gVal = abs(self.sourceCell[0]-1-i)*2 + abs(self.sourceCell[1]-1-j)*1#l1 norm between source to current cell
                fVal = gVal+hVal#total priority cost of the cell
                temp = node(self.nodeIdCount,i,j,gVal,hVal,fVal,False)# making a node cell
                node_row.append(temp)#inserting cell into 1d array
                self.nodeIdCount = self.nodeIdCount+1 #increament nodeID
            self.node_matrix.append(node_row)#inserting row into the matrix
        self.blockCell()#mark the block cell as visited
    
    def traverse(self):
        sourceCellRow = self.sourceCell[0]-1
        sourceCellCol = self.sourceCell[1]-1
        self.q.put(self.node_matrix[sourceCellRow][sourceCellCol])#insert the source cell to the priority queue
        while not self.q.empty():
            temp = self.q.get() #get current cell
            row = temp.getRow() #current cell row
            col = temp.getCol() #curent cell col
            #if the current cell is the destination cell then stop
            if row==self.destinationCell[0]-1 and col==self.destinationCell[1]-1:
                print("Searching ....")
                return
            if row-1>=0 and not self.node_matrix[row-1][col].isVisited():# if top cell exist and not visisted
                # top cell
                temp1 = self.node_matrix[row-1][col]
                self.node_matrix[row-1][col].setPredecessor(row,col)
                preNodeCost = self.node_matrix[row][col].getNodeCost()
                self.node_matrix[row-1][col].setNodeCost(preNodeCost+2)
                self.q.put(self.node_matrix[row-1][col])
                #if bottom cell exist and not visited
            if row+1<=self.rowAndColCell[0]-1 and not self.node_matrix[row+1][col].isVisited():
                #bottom cell
                temp1 = self.node_matrix[row+1][col]
                self.node_matrix[row+1][col].setPredecessor(row,col)
                preNodeCost = self.node_matrix[row][col].getNodeCost()
                self.node_matrix[row+1][col].setNodeCost(preNodeCost+2)
                self.q.put(self.node_matrix[row+1][col])
                #if left cell exits and not visited
            if col-1>=0 and not self.node_matrix[row][col-1].isVisited():
                #left cell
                temp1 = self.node_matrix[row][col-1]
                self.node_matrix[row][col-1].setPredecessor(row,col)
                preNodeCost = self.node_matrix[row][col].getNodeCost()
                self.node_matrix[row][col-1].setNodeCost(preNodeCost+1)
                self.q.put(self.node_matrix[row][col-1])
                #if right cell exist and not visited
            if col+1<=self.rowAndColCell[1]-1 and not self.node_matrix[row][col+1].isVisited():
                #right cell
                temp1 = self.node_matrix[row][col+1]
                self.node_matrix[row][col+1].setPredecessor(row,col)
                preNodeCost = self.node_matrix[row][col].getNodeCost()
                self.node_matrix[row][col-1].setNodeCost(preNodeCost+1)
                self.q.put(self.node_matrix[row][col+1])
            self.node_matrix[row][col].setVisited(True)
    
    def printNodeMatrix(self):#optional utility funtion not necessary,trying to see what's inside each cell
        for i in range(0,self.rowAndColCell[0]):
            for j in range(0,self.rowAndColCell[1]):
                print(self.node_matrix[i][j],end = ' ')
            print("\n")
    #mark the block cell as visited
    #loop through the blocklist array and mark the coordinate as visited
    def blockCell(self):
        for i in range(0,len(self.blockList)):
            blockRow = self.blockList[i][0]
            blockCol = self.blockList[i][1]
            self.node_matrix[blockRow-1][blockCol-1].setVisited(True)
    def printPath(self):
        destRow = self.destinationCell[0]-1 #get destination cell row
        destCol = self.destinationCell[1]-1 #get destination cell col
        destinationCost = self.node_matrix[destRow][destCol].getNodeCost() #not necessary redundant code
        Predecessor = [-1,-1] #initialize predecessor list
        sourceRow = self.sourceCell[0] #get source cell row
        sourceCol = self.sourceCell[1] #get source cell col
        pathList = [[destRow,destCol]] # store all the predecessor of the destination cell
        # the loop is started from the destination cell and will end when it reach the source cell
        #that is why we are calculating the l1 norm between the current cell to source cell
        # the loop will stop when we reached source cell
        while self.distance(Predecessor):#if distance is not equal to zero
            Predecessor = self.node_matrix[destRow][destCol].getPredecessorCell()
            destRow = Predecessor[0]
            destCol = Predecessor[1]
            pathList.append(Predecessor)
        l = len(pathList)-1
        print("Path:")
        for i in range(l,0,-1):
            print("Cell("+str(pathList[i][0]+1)+","+str(pathList[i][1]+1)+")->",end="")
        print("Cell("+str(pathList[0][0]+1)+","+str(pathList[0][1]+1)+")")
        print("Cost is: "+str(self.totalCost(pathList)))
        
    #calculating the total cost using the pathList array which contain all the cell coordinate that are travel to find a path between source to destination
    def totalCost(self,pathList):
        result = 0
        l = int(len(pathList))
        for i in range(0,l-1):
            x = pathList[i][0]
            x1 = pathList[i+1][0]
            y = pathList[i][1]
            y1=pathList[i+1][1]
            temp = abs(x - x1)*2 + abs(y-y1)*1 # change in x mean cost =2 and change in y mean cost =1
            result = result + temp
        return result

    def distance(self,pre):
        return abs(pre[0]-(self.sourceCell[0]-1)) + abs(pre[1]-(self.sourceCell[1]-1))




        



g = Graph()
g.traverse()
g.printPath()
#g.printNodeMatrix()






