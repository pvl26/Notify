import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Test")

import time


while True:
    notification = Notify.Notification.new(
        "Notificarea ta din 20 in 20 de secunde", 
        "┗(＾0＾)┓"   
    )
    notification.set_urgency(0)
    notification.show()

    time.sleep(20)    

Notify.uninit("Test")