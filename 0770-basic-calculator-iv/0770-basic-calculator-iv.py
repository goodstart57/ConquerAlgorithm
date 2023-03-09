class Solution:
    def get_dvar(self, var):
        curr_num, curr_vars = 1, []
        for v in var.split("*"):
            if v.isdigit():
                curr_num *= int(v)
            elif v in self.evalvars:
                curr_num *= self.val_of_var.get(v)
            else:
                curr_vars.append(v)
        return {"*".join(sorted(curr_vars)): curr_num}
    
    def get_dexp(self, lexp):
        # print(f"  get_dexp : {lexp}")
        ldexp = []
        for v in lexp:
            if v in ("+", "-", "*"):
                ldexp.append(v)
            elif type(v) == str:
                ldexp.append(self.get_dvar(v))
            else:
                ldexp.append(v)
        # print("    ldexp : ", ldexp)
        
        i, ldexp2 = 0, []
        while i < len(ldexp):
            if ldexp[i] == "*":
                ldexp2.append(self.multiply(ldexp2.pop(), ldexp.pop(i+1)))
            else:
                ldexp2.append(ldexp[i])
            i += 1
        # print("    ldexp2 : ", ldexp2)
        
        i, dexp = 1, ldexp2[0]
        while i < len(ldexp2):
            if ldexp2[i] == "+":
                dexp = self.add(dexp, ldexp2[i+1])
            elif ldexp2[i] == "-":
                dexp = self.substract(dexp, ldexp2[i+1])
            i += 1
        # print("    dexp : ", dexp)
        return dexp
    
    def get_lexp(self, exp):
        stack = []
        i = 0
        while i < len(exp):
            if exp[i] in "(":
                stack.append(i)
            elif exp[i] in ")":
                si = stack.pop()
                exp = exp[:si] + [self.get_dexp(exp[si+1:i])] + exp[i+1:]
                i = si
            elif exp[i] not in ("+", "-", "*"):
                exp[i] = self.get_dvar(exp[i])
            i += 1
        
        exp = self.get_dexp(exp)
        
        return exp
    
    def add(self, l, r):
        dexp = {}
        for k, v in l.items():
            if dexp.get(k):
                dexp[k] += v
            else:
                dexp[k] = v
        for k, v in r.items():
            if dexp.get(k):
                dexp[k] += v
            else:
                dexp[k] = v
        return dexp
    
    def substract(self, l, r):
        dexp = {}
        for k, v in l.items():
            if dexp.get(k):
                dexp[k] += v * 1
            else:
                dexp[k] = v * 1
        for k, v in r.items():
            if dexp.get(k):
                dexp[k] += v * -1
            else:
                dexp[k] = v * -1
        return dexp
    
    def multiply(self, l, r):
        # print(f"      multiply({l}, {r})")
        dexp = {}
        for k1, v1 in l.items():
            for k2, v2 in r.items():
                nk, nv = "*".join(sorted((k1+"*"+k2).split("*"))).strip("*"), v1 * v2
                # print(f"        nk: {nk} / nv: {nv}")
                if dexp.get(nk):
                    dexp[nk] += nv
                else:
                    dexp[nk] = nv
        # print(f"        dexp: {dexp}")
        return dexp
        
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        result = []
        expression = expression.replace("(", "( ").replace(")", " )")
        expression = expression.split()
        # print(expression)
        self.evalvars = evalvars
        self.val_of_var = dict(zip(evalvars, evalints))
        # print(self.val_of_var)
        # 식 정리
        lexp = self.get_lexp(expression)
        # print(lexp)
        # lexp = self.multiply(lexp)
        
        # 결과 layout으로 정리
        for k, v in sorted(lexp.items(), key=lambda x: (-len(x[0].split("*")), x[0] == "", x[0])):
            if v != 0:
                result.append(str(v) + ("*"+k if k else ""))
        
        return result