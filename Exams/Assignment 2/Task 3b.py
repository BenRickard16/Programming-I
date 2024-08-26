def point_on_segment(point, seg):
    seg1 = seg[0]
    seg2 = seg[1]
    v1 = [seg1[0] - point[0], seg1[1] - point[1]]
    v2 = [seg2[0] - point[0], seg2[1] - point[1]]
    dotpdct = v1[0]*v2[0] + v1[1]*v2[1]
    return dotpdct < 0

