Use a rotary phone connected to a raspberry PI to create a game where 4 local players need to send a T9 text message using the rotary phone.  First to send the message wins!

Part of in internal hackathon project at Genesys

Pin Colors:
Orange - Dialing 
Blue - Pulse
Green - Hook

setup as constants in hackathon.py


                    +5VDC
                     |
                     \
                     /  1K ohms
                     \
                     /
 Wire from Phone     |
---------------------+
                     |
                     |
                     |
                    RPI Pin
