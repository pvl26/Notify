# NotificationProject

    Installing the requirements:

        sudo apt install python-gi                 #for gi package
        sudo apt install gir1.2-notify-0.7         #for notify library
        sudo apt-get install python3-pydbus        #e nevoie de el pentru a trimite notificari de la serviciu

    How to create the service:

        chmod +x service_maker.py
        sudo ./service_maker.py       #  run without sudo to see what happens

    WARNING: the process won't stop, you need to forcefully kill it for now