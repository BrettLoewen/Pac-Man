import src.Logger as Logger

colliders = []
precision = 7
do_draw_colliders = False

# Add the passed collider to the manager list of tracked colliders
def add_collider(collider):
    colliders.append(collider)

# Control the precision of the collision overlap check
def set_collision_precision(p):
    global precision
    precision = p

# Control whether or not the colliders will be drawn
def set_draw_colliders(do_draw):
    global do_draw_colliders
    do_draw_colliders = do_draw

# Calculate the sub points of the passed colliders
def get_collider_points(collider):
    points = []
    
    # Get the collider's defining info
    x = collider.x
    y = collider.y
    width = collider.width
    height = collider.height

    startX = x - (x % precision)
    startY = y - (y % precision)
    
    offsetX = startX + precision
    offsetY = startY + precision

    while offsetX < startX + width:
        while offsetY < startY + height:
            points.append((offsetX, offsetY))
            offsetY += precision
        offsetX += precision
        offsetY = startY + precision

    return points

# Determine which collider sub points are shared between the two passed colliders
def get_overlap_points(collider1, collider2):
    points1 = get_collider_points(collider1)
    points2 = get_collider_points(collider2)

    return set(points1).intersection(points2)

# Check if the passed collider is overlapping with any other colliders
def check_for_overlap(collider):
    for other in colliders:
        if(collider == other):
            continue
        points = get_overlap_points(collider, other)
        if len(points) > 0:
            collider.add_overlap_collider(other, points)

# Should be called each frame before the draw colliders
# Determines which colliders are overlapping
def check_collisions():
    for collider in colliders:
        collider.clear_overlap_colliders()
        check_for_overlap(collider)

# Needs to be called in Renderer before Logger.draw_lines()
def draw_colliders():
    # Only draw colliders if that is wanted
    if do_draw_colliders:
        # Loop through every collider and draw them
        for collider in colliders:
            # Get the collider's defining info
            x = collider.x
            y = collider.y
            width = collider.width
            height = collider.height

            # Get each collision point in the collider
            points = get_collider_points(collider)
            overlapPoints = collider.overlap_points

            # Use whether or not the collider overlapping anything to determine the outline's color
            if(len(overlapPoints) > 0):
                Logger.set_line_color(Logger.LineColor.RED)
            else:
                Logger.set_line_color(Logger.LineColor.GREEN)

            # Draw the outline of the collider
            Logger.add_wire_square(x, y, width, height)

            # Draw the sub points of the collider
            draw_sub_points(points, overlapPoints)

def draw_sub_points(points, overlapPoints):
    # Loop through every point and draw them
    for point in points:
        # Set the color of the point based on whether or not it is overlapping another ponit
        if(point in overlapPoints):
            Logger.set_line_color(Logger.LineColor.RED)
        else:
            Logger.set_line_color(Logger.LineColor.GREEN)

        # Draw the point
        Logger.add_wire_square(point[0], point[1], 1, 1)