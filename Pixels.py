from Constants import *

def draw(win, shape):
    costheta = cos(shape.theta)
    sintheta = sin(shape.theta)
    printShapeLines = []
    for i in range(shape.nlines):
        x0 = shape.lines[i][0] * costheta - shape.lines[i][1] * sintheta
        y0 = shape.lines[i][0] * sintheta + shape.lines[i][1] * costheta
        printShapeLines.append([x0 + shape.offset[0], y0 + shape.offset[1]])
    pg.draw.aalines(win, WHITE, False, printShapeLines, 1)

'''def set_pixel(surf, x, y, pix):
    if (x >= 0 and y >= 0 and x < surf.w and y < surf.h):
        target = surf._pixel_address() + y * surf.get_pitch() + x * sizeof(Uint32);
        *(Uint32 *)target = pix;

x = 0-1
    y = -1-0
        win, bullet.offset[0] + x, bullet.offset[1] + y, White

def line(SDL_Surface *surf, int x0, int y0, int x1, int y1, Uint32 pix) {
    int dx = abs(x1-x0), 
        sx = x0 < x1 ? 1 : -1; // The horizontal line direction
    int dy = abs(y1-y0), 
        sy = y0 < y1 ? 1 : -1; // The vertical line direction
    int err = (dx>dy ? dx : -dy) / 2, 
        e2;

    while (1) {
        set_pixel(surf, x0, y0, pix);

        if (x0 == x1 && y0 == y1) 
            break; // Exit loop once the end point of the line is reached

        e2 = err;   // A temporary variable to store the value of err before it'll be
                    // changed

        if (e2 > -dx) {
            err -= dy;
            x0 += sx;
        }

        if (e2 < dy) {
            err += dx;
            y0 += sy;
        }
    }
}

def lines(SDL_Surface *surf, vec2f_t *lines, int nlines, vec2f_t offset, 
    float theta, Uint32 pix) {
    float costheta = cosf(theta);
    float sintheta = sinf(theta);

    for (int i = 0; i < nlines; i++) {
        float x0 = lines[i*2].x * costheta - lines[i*2].y * sintheta;
        float y0 = lines[i*2].x * sintheta + lines[i*2].y * costheta;
        float x1 = lines[i*2+1].x * costheta - lines[i*2+1].y * sintheta;
        float y1 = lines[i*2+1].x * sintheta + lines[i*2+1].y * costheta;

        line(surf, offset.x + x0, offset.y + y0, 
            offset.x + x1, offset.y + y1, pix);
    }
}'''