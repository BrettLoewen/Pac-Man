import src.CollisionManager

class Collider:
    def __init__(self, x, y, width, height, tag):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tag = tag
        self.colliders = []
        self.overlap_points = set()

        src.CollisionManager.add_collider(self)

    def add_overlap_collider(self, collider, points: set[tuple]):
        self.colliders.append(collider)

        self.overlap_points = (self.overlap_points | points)

    def clear_overlap_colliders(self):
        self.colliders.clear()
        self.overlap_points.clear()

    def overlaps_collider_with_tag(self, tag):
        for collider in self.colliders:
            if tag == collider.tag:
                return True
        return False