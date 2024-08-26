def dist2(x1, y1, x2, y2):
    dx = x1-x2
    dy = y1-y2
    dist = (dx**2+dy**2)**0.5
    return dist

def perimeter4(x1, y1, x2, y2, x3, y3, x4, y4):
    l12 = dist2(x1, y1, x2, y2)
    l23 = dist2(x2, y2, x3, y3)
    l34 = dist2(x3, y3, x4, y4)
    l41 = dist2(x4, y4, x1, y1)
    total = l12 + l23 + l34 + l41
    return total
print(perimeter4(0, 0, 3, 0, 3, 1, 0, 5))

 
