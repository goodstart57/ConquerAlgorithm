class Solution:
    def multiply(self, l, r):
        result = []
        for lv in l:
            for rv in r:
                result.append(lv+rv)
        return result
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        result = [""]
        dletter = {
            "2" : ("a","b","c"),
            "3" : ("d","e","f"),
            "4" : ("g","h","i"),
            "5" : ("j","k","l"),
            "6" : ("m","n","o"),
            "7" : ("p","q","r","s"),
            "8" : ("t","u","v"),
            "9" : ("w","x","y","z"),
        }
        
        for digit in digits:
            result = self.multiply(result, dletter.get(digit))
        
        return result