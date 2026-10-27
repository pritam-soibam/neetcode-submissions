class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        opening = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        closing = []
        for bracket in s:
            if bracket not in opening:
                if not closing:
                    return False
                if closing.pop() != bracket:
                    return False
            else:
                closing.append(opening[bracket])
        
        return False if closing else True