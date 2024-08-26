def one_bounce(ray, seg, win):
    draw_window(win, 'r')
    collisionpoint = ray_segment_intersect(ray, seg)
    if collision point == None:
        dra
    


        dtpdctrayseg = (cos(2*pi-ray[1])*(pt1[0]-pt2[0])+sin(2*pi-ray[1])*(pt1[1]-pt2[1]))
        angleincidence = acos(dtpdctrayseg/(((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)**(1/2)))
        newangle = 3/2*pi - angleincidence - tan((pt2[1]-pt1[1])/(pt2[0]-pt1[0]))
        newray = [collisionpoint, newangle]
        draw_ray_in_window(ray, win, 'g')
        draw_ray_in_window(newray, win, 'g')

def one_bounce(ray, seg, win):
    draw_window(win, 'r')
    draw_segment(seg, 'y')
    collisionpoint = ray_segment_intersect(ray, seg)
    pt1 = seg[0]
    pt2 = seg[1]
    if collisionpoint == None:
        draw_ray_in_window(ray, win, 'g')
    else:
        draw_directed_segment([ray[0], collisionpoint], 'b')
        l1 = line_from_ray(ray)
        l1vect = [l1[0], l1[1]]
        segvect = [pt2[0]-pt1[0], pt2[1]-pt1[1]]
        dtpdct = vdot(l1vect, segvect)
        d1 = (l1vect[0]**2 + l1vect[1]**2)**(1/2)
        d2 = (segvect[0]**2 + segvect[1]**2)**(1/2)
        incidence = acos(dtpdct/(d1*d2))
        seggrad = tan(segvect[1]/segvect[0])
        newangle = 3*pi/2 - incidence - seggrad
        reflected = [collisionpoint, newangle]
        draw_ray_in_window(reflected, win, 'g')