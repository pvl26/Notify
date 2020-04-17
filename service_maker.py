#!/usr/bin/env python3

#  pare ca "lumea" zice sa folosesti subprocess in loc de os
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
 
    command = "echo '[Service]\nExecStart=/usr/local/lib/notifyapp/service_source.py\n' > notifyapp.service"
    os.system(command)

if __name__ == "__main__":
    main() 