from pydualsense import pydualsense, TriggerModes
import pyvolume
import pyvolume.windows
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK

class 

def dpad_left(state):
    if state:
        win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)

def dpad_right(state):
    if state:
        win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)

def dpad_down(state):
    if state:
        pyvolume.windows.volume_down()

def dpad_up(state):
    if state:
        pyvolume.windows.volume_up()

def cross_pressed(state):
    if state:
        print(VK_MEDIA_PLAY_PAUSE)
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)

def circle_pressed(state):
    ds.close()

ds = pydualsense() # open controller
ds.init() # initialize controller
print(ds.dpad_down)
ds.dpad_right += dpad_right
ds.dpad_left += dpad_left
ds.circle_pressed += circle_pressed
ds.dpad_down += dpad_down
ds.dpad_up += dpad_up
ds.cross_pressed += cross_pressed
ds.light.setColorI(255,0,0) # set touchpad color to red
# ds.triggerR.setMode(TriggerModes.Rigid)
# ds.triggerR.setForce(1, 255)
