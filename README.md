# NotificationProject

Installation
============
You will need to install next packages, some might be already installed in your system

        __`sudo apt install python-gi`__                 #for gi package
        sudo apt install gir1.2-notify-0.7         #for notify library
        sudo apt install mpg123                    #for the notification sound
        sudo apt-get install python3-bs4           #for beautifulsoup package
        sudo apt-get install python3-lxml          #for lxml package

    How to create the service:

        chmod +x service_maker.py
        sudo ./service_maker.py       #  run without sudo to see what happens

    WARNING: the process won't stop, you need to forcefully kill it for now


    For debugging:
    
        ./clean.sh      #  sterge serviciul si toate fisierele generate pentru el
        sudo ./service_maker.py     
        
        sudo systemctl daemon-reload 
        sudo systemctl start notifyapp.service
        sudo systemctl status notifyapp.service
        

might left an easter egg
