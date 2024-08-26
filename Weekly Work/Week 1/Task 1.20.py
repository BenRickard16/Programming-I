def dist2(x1, y1, x2, y2):
    dx = x1-x2
    dy = y1-y2
    dist = (dx**2+dy**2)**0.5
    return dist

def area3(x1, y1, x2, y2, x3, y3):
    l12 = dist2(x1, y1, x2, y2)
    l13 = dist2(x1, y1, x3, y3)
    l23 = dist2(x2, y2, x3, y3)
    s = (l12 + l13 + l23)/2
    area = (s*(s - l12)*(s - l13)*(s - l23))**(1/2)
    return area

print(area3(0, 0, 2, 5, 8, 0))
