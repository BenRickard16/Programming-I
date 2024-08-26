from matplotlib import pyplot as plt

def draw_point(pt, col):
    plt.plot(pt[0], pt[1], 'o', color = col)



def draw_segment(seg, col):
    pt1 = seg [0]
    pt2 = seg[1]
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color = col)



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



def draw_path(path, col):
    for i in range(len(path)-1):
        draw_directed_segment([path[i], path[i+1]], col)
        


def draw_window(win, col):
    xrange = win[0]
    yrange = win[1]
    draw_segment([[xrange[0], yrange[0]], [xrange[0], yrange[1]]], col)
    draw_segment([[xrange[1], yrange[0]], [xrange[1], yrange[1]]], col)
    draw_segment([[xrange[0], yrange[0]], [xrange[1], yrange[0]]], col)
    draw_segment([[xrange[0], yrange[1]], [xrange[1], yrange[1]]], col)

draw_point([0, 1], 'red')
draw_point([1, 0], 'blue')
draw_point([1.5, 1], 'pink')
draw_directed_segment([[0,1], [1,0]], 'green')
draw_directed_segment([[-1.5,-1.5], [-1.4,-1.5]], 'cyan')
draw_directed_segment([[1.5,-1.5], [1.47,-1.45]], 'green')
draw_directed_segment([[1,1], [0,1]], [0, 1, 0])
draw_path([[-1.75, 0.0], [-1.25, 0.0], [-1.5, 0.5], [-1.0, 1.6]], 'grey')
draw_segment([[-1,-0.5], [1.5, 0.3]], [1, 1, 0])
draw_segment([[-1, 1], [1, -1]], [0.5, 0.5, 0.5])
draw_window([[-2, 2], [-1.8, 1.6]], [1,0,0])
plt.show()
