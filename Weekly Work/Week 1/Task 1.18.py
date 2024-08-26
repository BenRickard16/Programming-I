def dist2(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return (dx**2 + dy**2)**0.5

print(dist2(1, 3, 4, -1))
print(dist2(2, 1, 7, 13))