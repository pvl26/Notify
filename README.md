# NotificationProject

    Installing the requirements:

        sudo apt install python-gi                 #for gi package
        sudo apt install gir1.2-notify-0.7         #for notify library

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
