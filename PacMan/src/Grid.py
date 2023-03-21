import src.Logger as Logger
from PIL import Image
from src.GridCell import GridCell

MAP_FILE_PATH = 'PacMan/res/textures/Map_Data.png'
CELLS_IN_COLUMN = 11
CELLS_IN_ROW = 10
CELL_PIXEL_SIZE = 3

class Grid:
    def __init__(self, rend, cell_size):
        self.create_grid(rend, cell_size)
        self.create_cell_connections()

    def create_grid(self, rend, cell_size):
        image = Image.open(MAP_FILE_PATH)
        pixels = image.load()
        pixel_size = image.size

        self.cells = []

        row = 0
        col = 0
        while col <= pixel_size[0] - CELL_PIXEL_SIZE:
            while row <= pixel_size[1] - CELL_PIXEL_SIZE:
                up = pixels[col + 1, row]
                right = pixels[col + 2, row + 1]
                down = pixels[col + 1, row + 2]
                left = pixels[col, row + 1]
                x = (col // CELL_PIXEL_SIZE) * cell_size
                y = (row // CELL_PIXEL_SIZE) * cell_size

                self.cells.append(GridCell(up, right, down, left, x, y, col // 3, row // 3, cell_size, rend))

                row += CELL_PIXEL_SIZE
            col += CELL_PIXEL_SIZE
            row = 0

    def create_cell_connections(self):
        row = 0
        col = 0
        while col < CELLS_IN_ROW:
            while row < CELLS_IN_COLUMN:
                cell: GridCell = self.cells[row + (col * CELLS_IN_COLUMN)]
                if cell.up:
                    cell.add_connection(self.cells[(row - 1) + (col * CELLS_IN_COLUMN)], 0)
                if cell.right:
                    cell.add_connection(self.cells[row + ((col + 1) * CELLS_IN_COLUMN)], 1)
                if cell.down:
                    cell.add_connection(self.cells[(row + 1) + (col * CELLS_IN_COLUMN)], 2)
                if cell.left:
                    cell.add_connection(self.cells[row + ((col - 1) * CELLS_IN_COLUMN)], 3)
                row += 1
            col += 1
            row = 0