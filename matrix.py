global lx,ly,size,temp,result
x=int(input("Enter matrix size: "))
size=x
lx=[]
ly=[]
temp=[0,0]
result=[]
def inputme(x):
	print("Enter the first Matrix: ")
	for i in range (x):
		y=input("")
		minl=y.split(' ')
		lx.append(minl)

	print("Enter the Second matrix: ")
	for j in range (x):
		y=input("")
		mink=y.split(" ")
		ly.append(mink)

def genaratex(lx,loc):
	temp[0]=(lx[loc])


def genaratey(ly,loc):
	sec=[]
	for i in ly:
		sec.append(i[loc])
	temp[1]=(sec)

def emptygen():
        global result
        result = [[0 for i in range(size)] for j in range(size)]

def calculator(temp,raw,column,size):
	valuem=0
	for i in range(size):
		valuem=valuem+(int(temp[0][i])*int(temp[1][i]))
	result[raw][column]=valuem

def printme(result):
        for i in result:
                print (i)

def caller(size):
	inputme(size)
	emptygen()
	for i in range(size):
		genaratex(lx,i)
		for j in range(size):
			genaratey(ly,j)
			calculator(temp,i,j,size)

caller(size)
printme(result)




