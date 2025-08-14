import math

print(math.pi)

def calculate_theta(x1,y1,x2,y2):
    a = x2 - x1
    b = y2 + y1
    tan_theta = a/b
    theta = math.atan(tan_theta)
    return theta

x1, y1 = 1.0,2.0
x2,y2 = 5.0,1.0

alpha = calculate_theta(x1,y1,x2,y2)

print(alpha)
print(math.degrees(alpha))
#
# v = 내 공의 속도
# 목적구의 이동거리리# s = (v*math.cos(math.radians(theta)))**2 / (2*mu*9.81)
