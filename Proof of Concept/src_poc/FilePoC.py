from src_poc.Input import Input
from src_poc.Renderer import Renderer
from src_poc.Text import Text
import src_poc.Logger as Logger
from src_poc.GameManager import GameManager
import src_poc.FileManager as FileManager

class FilePoC(GameManager):
    def __init__(self, rend: Renderer, input: Input):
        GameManager.__init__(self, rend, input)

        Text('Proof of Concept: File Management', rend, 20, (0, 0, 225), (0, 255, 255), 0, 0)

        # Logger.info(FileManager.read_file('Proof of Concept/res/Test.txt'))

        # Logger.info(FileManager.write_file('Proof of Concept/res/WriteTest.txt', 'This is a test'))

        # Logger.info(FileManager.update_file('Proof of Concept/res/Test.txt', 'Proof of Concept/res/WriteTest.txt'))

        Logger.info(FileManager.read_image_file('Proof of Concept/res/Image Reading Test.png'))

    # Not needed for this demonstration
    def on_update(self):
        pass