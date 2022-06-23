



def checkgrid(grid):
    toggle = "YES"
    n = len(grid)
    for i in range(n):
        grid[i] = sorted(grid[i])
    print(grid)
    for i in range(n-1):
        if grid[i]<= grid[i+1]:
            toggle = "YES"
        else:
            toggle = "NO"
            break


#grid = ['hcd','awc','shm']
#grid = ['sur','eyy','gxy']
grid = ['nyx','ynx','xyt']

#grid = ['mpxz','abcd','wlmf']
#grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = checkgrid(grid)

