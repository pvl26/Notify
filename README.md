# NotificationProject

Installation
============
You will need to install next packages, some might be already installed in your system

1. gi: __`sudo apt install python-gi`__
2. notify: __`sudo apt install gir1.2-notify-0.7`__
3. mpg123: __`sudo apt install mpg123`__                   
4. beautifoulsoup4: __`sudo apt-get install python3-bs4`__    
5. lxml: __`sudo apt-get install python3-lxml`__         

Service automatization
======================

How to create the service:

1. Give permissions: __`chmod +x service_maker.py`__
2. Run script: sudo __`./service_maker.py`__   

<font color="red">WARNING</font>: ```service_maker.py``` is not yet ready, don't use untill this message is gone!!!
 

    For debugging:
    
        ./clean.sh      #  sterge serviciul si toate fisierele generate pentru el
        sudo ./service_maker.py     
        
        sudo systemctl daemon-reload 
        sudo systemctl start notifyapp.service
        sudo systemctl status notifyapp.service
        

might left an easter egg
