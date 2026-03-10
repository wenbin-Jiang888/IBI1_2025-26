a = 5.08
b = 5.33
c = 5.55
d = b - a
e = c - b
print(f"Population change between 2004 and 2014: {d} million")
print(f"Population change between 2014 and 2024: {e} million")
if d > e:
    print("Population growth is decelerating")
if d < e:
    print("Population growth is accelerating")
if d == e:
    print("Population growth rate remains unchanged")
#Population change between 2004 and 2014: 0.25 million
#Population change between 2014 and 2024: 0.21999999999999975 million
#Population growth is decelerating

X = True  
Y = False 
W = X or Y
print(f"X = {X}, Y = {Y}, W (X or Y) = {W}")
X = True  
Y = True
W = X or Y
print(f"X = {X}, Y = {Y}, W (X or Y) = {W}")
X = False  
Y = False 
W = X or Y
print(f"X = {X}, Y = {Y}, W (X or Y) = {W}")
X = False  
Y = True 
W = X or Y
print(f"X = {X}, Y = {Y}, W (X or Y) = {W}")

#| X     | Y     | W (X or Y) |
#|-------|-------|------------|
#| True  | True  | True       |
#| True  | False | True       |
#| False | True  | True       |
#| False | False | False      |

