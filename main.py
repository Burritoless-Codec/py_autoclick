import time
import threading
from pynput.mouse import Button, Controller

from pynput.keyboard import Listener, KeyCode

delayTime = 0.0001
buttonDirection = Button.left
startStopButton = KeyCode(char='-')
terminateButton = KeyCode(char='=')


class ClickTheMouse(threading.Thread):
    def __init__(self, delayTime, buttonDirection):
        super(ClickTheMouse, self).__init__()
        self.delayTime = delayTime
        self.buttonDirection = buttonDirection
        self.running = False
        self.program_running = True
        print("Auto Clicker")
        print("Press '-' to start/stop clicking")
        print("Press '=' to exit")

    def startMouseclick(self):
        print('Clicking started...')
        self.running = True

    def stopMouseClick(self):
        print('Clicking stopped...')
        self.running = False

    def exitScript(self):
        self.stopMouseClick()
        print('Exiting program.\n')
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.buttonDirection)
                time.sleep(self.delayTime)
            time.sleep(0.1)


mouse = Controller()
clickThread = ClickTheMouse(delayTime, buttonDirection)
clickThread.start()


def on_press(key):
    if key == startStopButton:
        if clickThread.running:
            clickThread.stopMouseClick()
        else:
            clickThread.startMouseclick()
    elif key == terminateButton:
        clickThread.exitScript()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
