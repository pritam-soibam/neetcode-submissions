class Solution:
    def isValid(self, s: str) -> bool:
        opening = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        closing = []
        for bracket in s:
            if bracket in opening:
                closing.append(opening[bracket])
            else:
                if not closing:
                    return False
                if closing.pop() != bracket:
                    return False
        return False if closing else True