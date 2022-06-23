def displayPathtoPrincess(n,grid):


    for i in range(0,n):
        for j in range(0,n):
            if grid[i][j] == 'p':
                if [i,j] == [0,n-1] or [i,j] ==[0,0] or [i,j] == [n-1,0] or [i,j]== [n-1,n-1]:
                    princesspos = [i, j]
                else:
                    return
                print(princesspos)
            if grid[i][j]=='m':
                botpos= [i,j]
                print(botpos)

    leftdifference = princesspos[0]-botpos[0]
    rightdifference = princesspos[1]-botpos[1]
    list =[]
    for i in range(abs(leftdifference)):
        if princesspos[0]> botpos[0]:
            list.append("DOWN")
        else:
            list.append("UP")
    for i in range(abs(rightdifference)):
        if princesspos[1]> botpos[1]:
            list.append("RIGHT")
        else:
            list.append("LEFT")
    for i in list:
        print(i)







n = 3
grid = [['-','-','-'],['-','m','-'],['-','-','p']]
displayPathtoPrincess(n,grid)