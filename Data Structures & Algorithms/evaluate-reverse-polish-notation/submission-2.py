class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numst = []
    
        for ch in tokens:
            if ch not in "+-*/":
                numst.append(int(ch))
            else:
                num2 = numst[-1]
                numst.pop()
                num1 = numst[-1]
                numst.pop()
                if ch == "+":
                    numst.append(num1 + num2)
                elif ch == "*":
                    numst.append(num1 * num2)
                elif ch == "-":
                    numst.append(num1 - num2)
                elif ch == "/":
                    numst.append(int(float(num1)/num2))
            
            # print(numst)
                
                        
        return numst[-1]