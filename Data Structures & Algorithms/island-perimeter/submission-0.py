
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.answer=0
        self.visited=set()
        def dfs(i,j):
            if i>len(grid)-1 or i<0 or j<0 or j>len(grid[0])-1 or (i,j) in self.visited or grid[i][j]==0:
                return 
            dirs=[(-1,0),(1,0),(0,-1),(0,1)]
            self.visited.add((i,j))
            for x,y in dirs:
                if i+x<len(grid) and i+x>-1 and j+y>-1 and j+y<len(grid[0]) and grid[x+i][y+j]==0:
                    self.answer+=1
                    continue
                elif i+x>len(grid)-1 or i+x<0 or j+y<0 or j+y>len(grid[0])-1:
                    self.answer+=1
                    continue

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in self.visited:
                    dfs(i,j)
        return self.answer
