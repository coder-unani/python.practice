x = [2, 3, 5, 7, 11]
y = x
y[2] = 4
print(x) # [2, 3, 4, 7, 11]
print(y) # [2, 3, 4, 7, 11]
# x와 y가 같은 리스트를 가리키고 있기 때문에, y의 값을 변경하면 x의 값도 변경됩니다.

x = [2, 3, 5, 7, 11]
y = x.copy()
y[2] = 4
print(x) # [2, 3, 5, 7, 11]
print(y) # [2, 3, 4, 7, 11]
# x.copy()를 사용하여 x의 복사본을 만들어 y에 할당하면, x와 y는 다른 리스트를 가리키게 됩니다. 
# 따라서 y의 값을 변경해도 x의 값은 변하지 않습니다.

x = [2, 3, 5, 7, 11]
y = list(x)
y[2] = 4
print(x) # [2, 3, 5, 7, 11]
print(y) # [2, 3, 4, 7, 11]