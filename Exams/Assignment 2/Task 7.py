from math import pi, tan, sin, cos
from matplotlib import pyplot as plt

def line_from_segment(seg):
    p1 = seg[0]
    p2 = seg[1]
    a = p1[0]
    b = p1[1]
    c = p2[0]
    d = p2[1]
    return [d-b, a-c, b*c-a*d]

def line_from_ray(ray):
    point = ray[0]
    angle = ray[1]
    if angle == pi/2 or angle == 3*pi/2:
        line = [1,0,-1*point[0]]
    else:
        line = [tan(angle), -1, point[1] - point[0]*tan(angle)]
    return line
        
def lines_intersect(line1, line2):
    a = line1[0]
    b = line1[1]
    c = line1[2]
    d = line2[0]
    e = line2[1]
    f = line2[2]
    if b*d != a*e:
        x = (c*e - b*f) / (b*d - a*e)
        y = (a*f - c*d) / (b*d - a*e)
        return [x,y]

def point_on_segment(point, seg):
    seg1 = seg[0]
    seg2 = seg[1]
    v1 = [seg1[0] - point[0], seg1[1] - point[1]]
    v2 = [seg2[0] - point[0], seg2[1] - point[1]]
    dotpdct = v1[0]*v2[0] + v1[1]*v2[1]
    return dotpdct <= 0

def point_on_ray(point, ray):
    raypoint = ray[0]
    rayangle = ray[1]
    x = point[0]
    y = point[1]
    v1 = [x - raypoint[0], y - raypoint[1]]
    v2 = [(x**2 + y**2)**(1/2)*cos(rayangle), (x**2 + y**2)**(1/2)*sin(rayangle)]
    dotpdct = v1[0]*v2[0] + v1[1]*v2[1]
    return dotpdct >= 0
    
    

def ray_segment_intersect(ray, seg):
    line1 = line_from_ray(ray)
    line2 = line_from_segment(seg)
    point = lines_intersect(line1, line2)
    if point != None:
        if point_on_segment(point, seg) and point_on_ray(point, ray):
            return point


def draw_directed_segment(dirseg, col):
    pt1 = dirseg [0]
    pt2 = dirseg [1]
    dx = pt2 [0] - pt1 [0]
    dy = pt2 [1] - pt1 [1]
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color=col)
    plt.quiver(
        pt1[0], pt1[1], dx, dy,
        scale_units='xy', angles='xy', scale=1,
        width=.005,
        color=col
    )
        

def draw_ray_in_window(ray, window, col):
    windowx = window[0]
    windowy = window[1]
    x1 = windowx[0]
    x2 = windowx[1]
    y1 = windowy[0]
    y2 = windowy[1]
    
    p1 = ray_segment_intersect(ray, [[x1,y1], [x1,y2]])
    p2 = ray_segment_intersect(ray, [[x1,y2], [x2,y2]])
    p3 = ray_segment_intersect(ray, [[x2,y1], [x2,y2]])
    p4 = ray_segment_intersect(ray, [[x1,y1], [x2,y1]])
    
    ray1 = []
    if p1 != None:
        if point_on_segment(p1, [[x1, y1], [x1, y2]]):
            ray1.append(p1)
    if p2 != None:
        if point_on_segment(p2, [[x1, y2], [x2, y2]]):
            ray1.append(p2)
    if p3 != None:
        if point_on_segment(p3, [[x2, y1], [x2, y2]]):
            ray1.append(p3)
    if p4 != None:
        if point_on_segment(p4, [[x1, y1], [x2, y1]]):
            ray1.append(p4)
            
    if len(ray1) == 2:
      draw_directed_segment([ray1[0], ray1[1]], col)
    if len(ray1) == 1:
        draw_directed_segment([ray[0],ray1[0]], col)

win = [[-1,1], [0, 1]]
ray = [[-0.5, 0.3], pi/4]
ray2 = [[-1.8, 2.1], -pi/4]
draw_ray_in_window(ray, win, 'blue')
draw_ray_in_window(ray2, win, 'pink')
plt.show()

    
    