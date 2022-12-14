This is my best attempt at making a security system from scratch.
The logic is very simple and mainly consists of 3 parts, the arming phase (where the device is armed and receiving constant input from the motion sensor), the alert phase (the motion sensor has been triggered), and finally the remote phase in which the device uses its USB wifi adapter to send a message to me reporting that there is someone been sensed.
First, I would recommend getting the button and LED setup so that whenever a button gets pressed, the led turns on and off. The button is the main boolean flag that will basically enable and disable the system. I believed that it would be important to be able to do this to not only save resources but also to not have Twilio SMS constantly be notified in the event of motion. Specifically, one feature is to introduce a delay after the button has been armed to make sure that the system gives the person arming it adequate time to leave the frame.
On the other side of things, a reliable wifi connection is akey to this so that the device can update to Twillio.
Lastly, using Twilio gives us a cheap and easy way to notify the user if there is someone in a place that they are not supposed to be. Using a pay-per-use model saves us money rather than getting a subscription to some service and allows for easy prototyping.