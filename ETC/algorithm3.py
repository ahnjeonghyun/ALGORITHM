# 양수로 이루어진 m x n 그리드를 인자로 드립니다. 상단 왼쪽에서 시작하여, 하단 오른쪽까지 가는 길의 요소를 다 더했을 때,가장 작은 합을 찾아서 return 해주세요.

# 한 지점에서 우측이나 아래로만 이동할 수 있습니다.

# Input: [    [1,3,1],    [1,5,1],    [4,2,1] ]

# Output: 7

# 설명: 1→3→1→1→1 의 합이 제일 작음

def min_path_sum(grid):
    x = len(grid)   
    y = len(grid[0])

    for i in range(1,x):
        grid[0][i] += grid[0][i-1]
        grid[i][0] += grid[i-1][0]

    for i in range(1,x):
        for j in range(1,y):
            grid[i][j] += min(grid[i][j-1], grid[i-1][j])
    
    return grid[-1][-1]
min_path_sum([[1,1,3,1],[1,1,5,1],[1,4,2,1],[1,2,3,4]])
