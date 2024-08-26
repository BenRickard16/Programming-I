from matplotlib import pyplot as plt
from math import pi, sin, cos, tan, acos

#Task1
#Plots a singular point
def draw_point(pt, col):
    plt.plot(pt[0], pt[1], 'o', color = col)


#Plots a segment
def draw_segment(seg, col):
    pt1 = seg [0]
    pt2 = seg[1]
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color = col)


#Plots a directed segment (arrow)
def draw_directed_segment(dirseg, col):
    pt1 = dirseg [0]
    pt2 = dirseg [1]
    dx = pt2 [0] - pt1 [0]
    dy = pt2 [1] - pt1 [1]
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color=col)
    plt.quiver(
        pt1[0], pt1[1], dx, dy,
        scale_units='xy', angles='xy', scale=1,
        width=.004,
        color=col)


#Plots path - sequence of directed segments
def draw_path(path, col):
    for i in range(len(path)-1):
        draw_directed_segment([path[i], path[i+1]], col)
        

#Plots a window
def draw_window(win, col):
    xrange = win[0]
    yrange = win[1]
    draw_segment([[xrange[0], yrange[0]], [xrange[0], yrange[1]]], col)
    draw_segment([[xrange[1], yrange[0]], [xrange[1], yrange[1]]], col)
    draw_segment([[xrange[0], yrange[0]], [xrange[1], yrange[0]]], col)
    draw_segment([[xrange[0], yrange[1]], [xrange[1], yrange[1]]], col)
    

#Task2
#Returns point of intersection of 2 lines
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


#Task 3a
#Gives line equation of which the segment lies on
def line_from_segment(seg):
    p1 = seg[0]
    p2 = seg[1]
    a = p1[0]
    b = p1[1]
    c = p2[0]
    d = p2[1]
    return [d-b, a-c, b*c-a*d]


#Task 3b
#Determines if point is on a segment
def point_on_segment(point, seg):
    seg1 = seg[0]
    seg2 = seg[1]
    v1 = [seg1[0] - point[0], seg1[1] - point[1]]
    v2 = [seg2[0] - point[0], seg2[1] - point[1]]
    dotpdct = v1[0]*v2[0] + v1[1]*v2[1]
    return dotpdct < 0


#Task 3c
#Gives point of intersection of 2 segments (if it exists)
def segments_intersect(seg1, seg2):
    line1 = line_from_segment(seg1)
    line2 = line_from_segment(seg2)
    point = lines_intersect(line1, line2)
    if point_on_segment(point, seg1) and point_on_segment(point, seg2):
        return point
    

#Task 4
#Gives equation of line it lies on
def line_from_ray(ray):
    point = ray[0]
    angle = ray[1]
    if angle == pi/2 or angle == 3*pi/2:
        line = [1,0,-1*point[0]]
    else:
        line = [tan(angle), -1, point[1] - point[0]*tan(angle)]
    return line
        

#Determine if a point lies on ray
def point_on_ray(point, ray):
    raypoint = ray[0]
    rayangle = ray[1]
    x = point[0]
    y = point[1]
    v1 = [x - raypoint[0], y - raypoint[1]]
    v2 = [cos(rayangle), sin(rayangle)]
    dotpdct = v1[0]*v2[0] + v1[1]*v2[1]
    return dotpdct >= 0
    
    
#Gives point of intersection of a ray and a segment
def ray_segment_intersect(ray, seg):
    line1 = line_from_ray(ray)
    line2 = line_from_segment(seg)
    point = lines_intersect(line1, line2)
    if point != None:
        if point_on_segment(point, seg) and point_on_ray(point, ray):
            return point
        

#Task 5
#Draws portion of line that appears in window
def draw_line_in_window(line, window, col):
    windowx = window[0]
    windowy = window[1]
    x1 = windowx[0]
    x2 = windowx[1]
    y1 = windowy[0]
    y2 = windowy[1]
#Extended lines from edges of window
    wln1 = [1, 0, -1*x1]
    wln2 = [0, 1, -1*y2]
    wln3 = [1, 0, -1*x2]
    wln4 = [0, 1, -1*y1]
#Points of intersection between line and extended lines    
    p1 = lines_intersect(line, wln1)
    p2 = lines_intersect(line, wln2)
    p3 = lines_intersect(line, wln3)
    p4 = lines_intersect(line, wln4)
#Figure out which points lie on window edges    
    seg1 = []
    if p1 != None:
        if point_on_segment(p1, [[x1, y1], [x1, y2]]):
            seg1.append(p1)
    if p2 != None:
        if point_on_segment(p2, [[x1, y2], [x2, y2]]):
            seg1.append(p2)
    if p3 != None:
        if point_on_segment(p3, [[x2, y1], [x2, y2]]):
            seg1.append(p3)
    if p4 != None:
        if point_on_segment(p4, [[x1, y1], [x2, y1]]):
            seg1.append(p4)
    if len(seg1) == 2:
        draw_segment(seg1, col)


#Task 6
#Plots window, both lines where they are in the window and their point of intersection
def draw_lines_and_window(line1, line2, window):
    wx = window[0]
    wy = window[1]
    draw_window(window, 'r')
    draw_line_in_window(line1, window, 'g')
    draw_line_in_window(line2, window, 'b')
    point = lines_intersect(line1, line2)
    if point != None:
        if wx[0]<point[0]<wx[1] or wx[1]<point[0]<wx[0]:
            if wy[0]<point[1]<wy[1] or wy[1]<point[1]<wy[0]:
                draw_point(point, 'y')


#Task7
#Plots the section of a ray that is in the window
def draw_ray_in_window(ray, window, col):
    windowx = window[0]
    windowy = window[1]
    x1 = windowx[0]
    x2 = windowx[1]
    y1 = windowy[0]
    y2 = windowy[1]
#Points of intersection between ray and window edges    
    p1 = ray_segment_intersect(ray, [[x1,y1], [x1,y2]])
    p2 = ray_segment_intersect(ray, [[x1,y2], [x2,y2]])
    p3 = ray_segment_intersect(ray, [[x2,y1], [x2,y2]])
    p4 = ray_segment_intersect(ray, [[x1,y1], [x2,y1]])
#Figure out which points lie on window edges   
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
#Plot depends on number of points on window edges            
    if len(ray1) == 2:
        draw_directed_segment([ray1[0], ray1[1]], col)
    if len(ray1) == 1:
        draw_directed_segment([ray[0],ray1[0]], col)


#Task 8
#Calculate dot product 2 vectors
def vdot(v1,v2):
    l = [v1[i] * v2[i] for i in range(len(v1))]
    val = 0
    for j in range(len(v1)):
        val = val + l[j]
    return val


#Determine magnitude of vector
def vabs(v1):
    l = [v1[i]**2 for i in range(len(v1))]
    val = 0
    for j in range(len(v1)):
        val = val + l[j]
    return val**(1/2)


#Produce path of start, exit and any collision
def one_bounce(ray, seg, win):
    PoI = ray_segment_intersect(ray, seg)
    windowx = win[0]
    x1 = windowx[0]
    x2 = windowx[1]
    windowy = win[1]
    y1 = windowy[0]
    y2 = windowy[1]
#4 segments of window
    w1 = [[x1, y1], [x1, y2]]
    w2 = [[x1, y2], [x2, y2]]
    w3 = [[x2, y1], [x2, y2]]
    w4 = [[x1, y1], [x2, y1]]
#If no collision, determine where object intersects window
    if PoI == None:
        if ray_segment_intersect(ray, w1) != None:
            endpt = ray_segment_intersect(ray, w1)
            return [ray[0], endpt]
        if ray_segment_intersect(ray, w2) != None:
            endpt = ray_segment_intersect(ray, w2)
            return [ray[0], endpt]
        if ray_segment_intersect(ray, w3) != None:
            endpt = ray_segment_intersect(ray, w3)
            return [ray[0], endpt]
        if ray_segment_intersect(ray, w4) != None:
            endpt = ray_segment_intersect(ray, w4)
            return [ray[0], endpt]
#With collision, determine where object leaves window
    else:
#First calculate equation for reflected ray
        l1 = line_from_ray(ray)
        l2 = line_from_segment(seg)
        v1 = [l1[1], -l1[0]]
        v2 = [l2[1], -l2[0]]
        alpha = acos(vdot(v1,v2)/(vabs(v1)*vabs(v2)))
        phi = acos(vdot(v2, [-1,0])/vabs(v2))
        refangle = phi + pi - alpha
        reflray = [PoI, refangle]
#Determine which segment it leaves in and where
        if ray_segment_intersect(reflray, w1) != None:
            endpt = ray_segment_intersect(reflray, w1)
            return [ray[0], PoI, endpt]
        if ray_segment_intersect(reflray, w2) != None:
            endpt = ray_segment_intersect(reflray, w2)
            return [ray[0], PoI, endpt]
        if ray_segment_intersect(reflray, w3) != None:
            endpt = ray_segment_intersect(reflray, w3)
            return [ray[0], PoI, endpt]
        if ray_segment_intersect(reflray, w4) != None:
            endpt = ray_segment_intersect(reflray, w4)
            return [ray[0], PoI, endpt]
#Task 9
#Draw path of one bounce
def draw_one_bounce(path, seg, win):
    draw_window(win, 'r')
    draw_segment(seg, 'orange')
    for i in range(len(path)-1):
        draw_directed_segment([path[i], path[i+1]], 'g')
  

#Task 10
#Distance between two points    
def dist2(p1,p2):
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    return (dx**2+dy**2)**0.5

#Calculate new angle of reflected ray
def reflected_angle(ray, seg):
    l1 = line_from_ray(ray)
    l2 = line_from_segment(seg)
    v1 = [l1[1], -l1[0]]
    v2 = [l2[1], -l2[0]]
    alpha = acos(vdot(v1,v2)/(vabs(v1)*vabs(v2)))
    phi = acos(vdot(v2, [-1,0])/vabs(v2))
    refangle = phi + pi - alpha
    return refangle


#Calculate path of particle bouncing many times
def multi_bounce(ray, seglist, win, maxpathlen):
    ans = [ray[0]]
    while len(ans) < maxpathlen + 1:
        lst = []
        lst1 = []
#Finding which segment collided with first
        for i in range(len(seglist)):
            b = ray_segment_intersect(ray, seglist[i])
            if b != None:
#So we don't get the segment the ray starts on
                if dist2(ray[0], b) > 0.001:
                    lst.append(b)
                    lst1.append(seglist[i])
#If doesn't collide with a segment, hits a wall of window
        if len(lst) == 0:
            for i in range(len(seglist)):
                b = ray_segment_intersect(ray, seglist[i])
                if b == None:
                    ans.append(one_bounce(ray, seglist[i], win)[1])
                    return ans
#Calulcating where the segment is struck and forming new ray
        else:
            lst2 = [dist2(ray[0], lst[i]) for i in range(len(lst))]
            distseg = min(lst2)
            n = lst2.index(distseg)
            seghit = lst1[n]
            ans.append(one_bounce(ray, seghit, win)[1])
            p = ray_segment_intersect(ray, seghit)
            refangle = reflected_angle(ray, seghit)
            ray = [p, refangle] 
    return ans


#Task 11
#Draw the path of a ball colliding many times
def draw_multi_bounce(path, seglist, win):
    draw_window(win, 'r')
    for i in range(len(seglist)):
        draw_segment(seglist[i], 'orange')
    for i in range(len(path)-1):
        draw_directed_segment([path[i], path[i+1]], 'g')

    
    
    
