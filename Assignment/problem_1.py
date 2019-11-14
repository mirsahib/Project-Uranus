try:
    import Queue as Q
except:
    import queue as Q

class node(object):
    nodeChar = ''
    nodeID=-1
    cost=-1
    priorityCost = -1
    visited=False
    def __init__(self):
        self.predecessor = []
    def __str__(self):
        return self.nodeChar +" "+ str(self.nodeID)+" "+str(self.cost)+" "+str(self.visited)
    def __lt__(self,other):
        return self.priorityCost<other.priorityCost
    def isVisited(self):
        return self.visited
    def insertPredecessor(self,char):
        self.predecessor.append(char)
    def getPredecessor(self):
        return self.predecessor
    def clearPredecessorList(self):
        self.predecessor.clear()



class Graph(object):
    matrix = []
    node_array = []
    row = 8
    col = 8
    q = Q.PriorityQueue()
    heuristic_value = {} #dictionary to store heuristic value
    charMap = {}#store the corresponding char value for node
    #node value is in numerical form but output should be in char
    #eg: s-d '''
    def __init__(self):
        #initializing the matrix
        self.matrix = [[1,3,0,0,4,0,0,0],
                [3,1,4,0,5,0,0,0],
                [0,4,1,4,0,5,0,0],
                [0,0,4,1,0,0,0,0],
                [4,5,0,0,1,2,0,0],
                [0,0,5,0,2,1,4,0],
                [0,0,0,0,0,4,1,3.5],
                [0,0,0,0,0,0,3.5,1]
                ]
        #initialing the heuristic dictionary
        self.heuristic_value = {0:11.5,1:10.1,2:5.8,3:3.4,4:9.2,5:7.2,6:3.5,7:0}
        #initializing the charmap dictionary which will be used to convert
        #the numerical nodeID to char'''
        self.charMap = {0:'s',1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g'}
        #this is used to avoid if statement inside the for loop
        sourceNode = node()#instanciating the source node
        sourceNode.nodeID = 0 # set source node id to zero
        sourceNode.nodeChar = 's' #set source node char (possible duplicate line sel.charmap[0] could be used)
        self.node_array.append(sourceNode)
        #initialize the node array with there corresponding id and character
        for i in range(1,8):
            temp = node()
            temp.nodeID = i
            temp.nodeChar=chr(96+i)
            self.node_array.append(temp)
    def traverse(self):
        self.node_array[0].priorityCost=self.heuristic_value[0]#set heuristic value for source node
        self.node_array[0].cost = 0 #set cost of the source node
        self.q.put(self.node_array[0]) #insert the source node into the priority queue
        while not self.q.empty(): #repeat the loop untill the priority queue is empty
            temp = self.q.get() #pop the head node of the priority queue
            index = temp.nodeID #get the nodeID of the pop node
            if index == 7: #if the nodeID is equal to the destination nodeID then stop
                print("destination reached")
                return
            for i in range(0,self.col): #search the row 
                if self.matrix[index][i]!=0 and self.matrix[index][i]!=1: #if the edge exit(i.e not equal to 0) or not a self edge(i.e not equal to 1)
                    if not self.node_array[i].isVisited():
                        self.relaxEdge(index,i)
            self.node_array[index].visited=True #mark the current node as visited
    def relaxEdge(self,index,i):
        edgeCost = self.matrix[index][i] #store the edge cost
        parentCost = self.node_array[index].cost #store the parent node cost
        childCost = self.node_array[i].cost #store the child node cost 
        #(it may happen if the child node is already explored by another node than the child node cost will not equal to zero)
        childPriorityCost = self.heuristic_value[i] #store the child node heuristic value
        if childCost==-1: #if the child node is not yet explored
            self.node_array[i].cost = edgeCost+parentCost
            self.node_array[i].priorityCost = edgeCost+parentCost+childPriorityCost
            p = self.node_array[index].getPredecessor()# get all the predecessor for the current node
            #insert the predecessor list to the child node
            if p:
                for k in range(0,len(p)):
                    self.node_array[i].insertPredecessor(p[k])#insert all the k th predecessor
            currentNodeChar = self.charMap[index] # current node char
            self.node_array[i].insertPredecessor(currentNodeChar) #insert the current node char as the child node predecessor
            self.printPath(parentCost,edgeCost,childPriorityCost,i)#print path/frontier
            self.q.put(self.node_array[i])# insert the child node into the priority queue
        else:
            #if the child node is explored
            if childCost>parentCost+edgeCost:#check if the child node cost is greater than the parent node cost + edge cost
                #remove the existing child node from the priority queue
                q_list = []
                while not self.q.empty():
                    temp = self.q.get()
                    if temp.nodeID!=i:
                        q_list.append(temp)
                self.node_array[i].cost = parentCost+edgeCost #update the child node cost
                self.node_array[i].priorityCost = edgeCost+parentCost+childPriorityCost# update
                p = self.node_array[index].getPredecessor()
                if p:
                    #clear current node predecessor list
                    self.node_array[i].clearPredecessorList()
                    for k in range(0,len(p)):
                        self.node_array[i].insertPredecessor(p[k])#insert all the k th predecessor
                currentNodeChar = self.charMap[index]     
                self.node_array[i].insertPredecessor(currentNodeChar)
                for j in range(0,len(q_list)):
                    self.q.put(q_list[j])
                #insert updated node
                self.printPath(parentCost,edgeCost,childPriorityCost,i)
                self.q.put(self.node_array[i])
    def printPath(self,parentCost,edgeCost,childPriorityCost,i):
        predecessorList =self.node_array[i].getPredecessor()#predecessor list from current node
        currentNodeChar = self.node_array[i].nodeChar
        totalNodeCost = parentCost+edgeCost
        totalPriorityCost = totalNodeCost+childPriorityCost
        for i in range(0,len(predecessorList)):
            print(predecessorList[i],end='->')
        print(currentNodeChar+":f = "+str(totalNodeCost) +" + "+str(childPriorityCost)+" = " +str(totalPriorityCost))
        print("\n")
    def printNodeArray(self):
        for i in range(0,8):
            print(self.node_array[i])


g = Graph()
g.traverse()
#g.printNodeArray()