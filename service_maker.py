#!/usr/bin/env python3

#  note: pare ca "lumea" zice ca e mai bun subprocess in loc de os
import os

def main():
    #  create a directory for service_source.py at /usr/local/lib
    try: 
        os.mkdir("/usr/local/lib/notifyapp/")
    except:
        print("Please run script as superuser!")
        os.abort()

    #  create service file
    os.system("touch notifyapp.service")  

    #  create a copy of the python program to move to /usr/local/lib
    os.system("touch service_source.py")
    os.system("cat source.py > service_source.py")
    os.system("chmod +x service_source.py")

    #  move sevice_source.py to /usr/local/lib/notifyapp
    os.rename("service_source.py", "/usr/local/lib/notifyapp/service_source.py")
 
    #  fill notifyapp.service
    command = "echo '[Unit]\nDescription=Notification app\n\n[Service]\nEnvironment=DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus\nEnvironment=DISPLAY=:0\nExecStart=/usr/local/lib/notifyapp/service_source.py\n\n[Install]\nWantedBy=default.target' > notifyapp.service"
    os.system(command)

    #  move notifyapp.service to /etc/systemd/system
    os.rename("notifyapp.service", "/etc/systemd/system/notifyapp.service")

    #  start notifyapp.service
    os.system("systemctl start notifyapp.service")

    #  enable notifyapp.service
    os.system("systemctl enable notifyapp.service")

if __name__ == "__main__":
    main() 
