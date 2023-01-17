"""TRY#1
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        s_list = list(s)
        # 방향 : 아래, 왼쪽 위
        directions = [[0, -1], [1, 1]]
        direction = directions[0] # 처음 향하는 방향은 아래
        zigzag = [["" for _ in range(18)] for __ in range(numRows)]
        
        print(s, numRows)
        
        loc_trgt = [0, numRows-1]
        while s_list:
            cx, cy = loc_trgt
            dx, dy = direction
            
            print(f"cur:({cx},{cy}),dir({dx},{dy}) {s_list}")
            
            zigzag[cy][cx] = s_list.pop(0)
            
            for l in zigzag[::-1]:
                print("  ", l)
            
            # 이동한 y가 위로 갈길이 없을때
            if cy + dy >= numRows:
                direction = directions[0]
                dx, dy = direction
            # 이동한 y가 아래로 갈길이 없을때
            elif cy + dy < 0:
                direction = directions[1]
                dx, dy = direction
            
            
            loc_trgt = [cx + dx, cy + dy]
        
        # print(zigzag)
        return "".join(list(map(lambda x: "".join(x), zigzag))[::-1])
"""

"""TRY#2 Timout.. T.T
   
from collections import deque


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s
        
        s = deque(s) # string to deque<char>
        zigzag = deque()
        
        s_length = len(s)
        # i : s에서 문자를 뽑아올 위치 / num_row_curr : 몇번째 라인을 보고있는지
        i, num_row_curr, max_distance = 0, 0, numRows + numRows - 2
        
        while num_row_curr < numRows:
            # 다음에 뽑아올 위치까지 거리
            if i in (0, numRows-1):
                # print(f"[{num_row_curr, i}] case#1-1")
                distances = (0, max_distance)
            elif 0 < i < numRows-1:
                # print(f"[{num_row_curr, i}] case#2-1")
                distances = (0, max_distance - num_row_curr * 2)
            elif num_row_curr in (0, numRows - 1):
                # print(f"[{num_row_curr, i}] case#1-2")
                distances = (max_distance, max_distance)
            else:
                # print(f"[{num_row_curr, i}] case#2-2")
                distances = (max_distance - (numRows - 1 - num_row_curr) * 2, max_distance - num_row_curr * 2)
            
            # zigzag 기록
            if i + distances[0] < s_length:
                i += distances[0]
                zigzag.append(s[i])
            
            if i + distances[1] < s_length:
                i += distances[1]
                zigzag.append(s[i])
            
            # print(f"distances:{distances}, zigzag:{''.join(zigzag)}")
            
            # zigzag 기록할때 line을 벗어나면 다음 line으로 이동
            if i + distances[0] >= s_length:
                i = num_row_curr = num_row_curr + 1
                # print(f"  [{num_row_curr}] next line")
            
        return "".join(zigzag)
""" 
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        wherewillyou = list(range(numRows)) + list(range(numRows-2, 0, -1))
        print(wherewillyou)
        
        zigzag = [[] for _ in range(numRows)]
        # print(zigzag)
        
        for i, char in enumerate(s):
            # print(i, char, i % numRows)
            zigzag[wherewillyou[i%len(wherewillyou)]].append(char)
            
        return "".join(map(lambda x: "".join(x), zigzag))