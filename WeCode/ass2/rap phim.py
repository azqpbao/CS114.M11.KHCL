n,m,a = map(int,input().split())
import math
print(math.ceil(n/a) * math.ceil(m/a))      #Hàm ceil để làm tròn lên. VD: 3.1 -> 4