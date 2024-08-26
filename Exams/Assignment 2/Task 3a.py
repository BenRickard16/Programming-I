def line_from_segment(seg):
    p1 = seg[0]
    p2 = seg[1]
    a = p1[0]
    b = p1[1]
    c = p2[0]
    d = p2[1]
    return [d-b, a-c, b*c-a*d]



