class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        s_list = list(s)
        # 방향 : 아래, 왼쪽 위
        directions = [[0, -1], [1, 1]]
        direction = directions[0] # 처음 향하는 방향은 아래
        zigzag = [["" for _ in range(1000)] for __ in range(numRows)]
        
        # print(s, numRows)
        
        loc_trgt = [0, numRows-1]
        while s_list:
            cx, cy = loc_trgt
            dx, dy = direction
            
            # print(f"cur:({cx},{cy}),dir({dx},{dy}) {s_list}")
            
            zigzag[cy][cx] = s_list.pop(0)
            
            # for l in zigzag[::-1]:
            #     print("  ", l)
            
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
            