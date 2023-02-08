class Solution:
    def myAtoi(self, s: str) -> int:
        """
        문자열 --> 무조건 탐색 중단
        
        부호-부호 --> 0
        
        부호-숫자 --> 정상
        
        부호-
        
        
        """
        
        sign = None
        digit = None
        
        for i in range(len(s)):
            
            # 3. 숫자나 부호를 찾은 뒤에는 " ", "+", "-" 모두 문자로 인식
            if (sign or digit or digit == 0) and not s[i].isdigit():
                break
            # 1. 공백 건너뛰기
            elif s[i] == " ":
                continue
            # 2. "-", "+"이면 저장 / sign이 저장되어있는데 한번더 만나면 종료
            elif s[i] in ("-", "+"):
                sign = 1 if s[i] == "+" else -1
                # if sign:
                #     break
                # elif digit is not None and digit >= 0:
                #     break
                # else:
                #     sign = 1 if s[i] == "+" else -1
            # 3. 문자가 나오는 경우 탐색 중단
            elif not s[i].isdigit():
                break
            # 1,2,3 조건에 부합하지 않는 경우 저장
            else:
                if not digit:
                    digit = 0
                digit = digit * 10 + int(s[i])
            print(sign, digit)
        
        if not sign:
            sign = 1
        if not digit:
            digit = 0
        
        if sign > 0 and digit > 2147483647:
            digit = 2147483647
        elif sign < 0 and digit * sign < -2147483648:
            digit = 2147483648
        
        return digit * sign
                