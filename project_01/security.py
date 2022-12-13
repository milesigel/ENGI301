"""
-----------------------------------------------------------------
---------
Home Security System
-----------------------------------------------------------------
---------
License:
Copyright 2022 Miles Sigel

Redistribution and use in source and binary forms, with or
without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
notice, this
list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above
copyright notice,
this list of conditions and the following disclaimer in the
documentation
and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its
contributors
may be used to endorse or promote products derived from this
software without
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.
-----------------------------------------------------------------
---------
"""
import time
import Adafruit_BBIO.GPIO as GPIO
from twilio.rest import Client

class PIRMotionSensor:
  def __init__(self, pin):
    self.pin = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.pin, GPIO.IN)

  def is_motion_detected(self):
    return GPIO.input(self.pin) == 1

class Button:
    def __init__(self, pin, led_pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        GPIO.setup(self.led_pin, GPIO.OUT)

    def is_pressed(self):
        return GPIO.input(self.pin) == 0

    def arm(self):
        GPIO.output(self.led_pin, GPIO.HIGH)

    def disarm(self):
        GPIO.output(self.led_pin, GPIO.LOW)


    def test(self):
        self.arm()
        time.sleep(1)
        self.disarm()
        time.sleep(1)
        self.arm()

class WiFiAdapter:
    def __init__(self, name, supported_bands):
        self.name = name
        self.supported_bands = supported_bands

    def connect(self, network_name, password):
        """
        Connect to the specified WiFi network using the given password.
        """
        # Connect to the network here
        print(f"Connecting to {network_name}...")
        # dont know exact mechanics of how to connect because dependent on actual hardware

    def disconnect(self):
        """
        Disconnect from the currently-connected WiFi network.
        """
        # Disconnect from the network here
        print("Disconnecting from network...")


class security():

    def __init__(self, moiton_pin, button_pin, led_pin):
        # Initialize variables
        self.motionSensor = PIRMotionSensor(moiton_pin)
        self.button = Button(button_pin, led_pin)
        self.account_sid = 'YOUR_ACCOUNT_SID'
        self.auth_token = 'YOUR_AUTH_TOKEN'
        self.twilioNum = 'Twilio Number'
        self.myNumber = "5129873780"
        self.twilio_client = Client(self.account_sid, self.auth_token)
        self.wifi_adapter = WiFiAdapter("basic", ["5Gz"])

        # i was not sure how to use the Wifi adapter


        # Initialize the client
        self._setup()



    def _setup(self):
        self.button.test()

        pass



    def button_press(self, button, function=None):
        """Button press
               - Optional function to execute while waiting for the button to be pressed
                 - Returns the last value of the function when the button was pressed
               - Waits for a full button press
               - Returns the time the button was pressed as tuple
        """
        button_press_time = 0.0  # Time button was pressed (in seconds)
        ret_val = None  # Optional return value for provided function

        # Optinally execute function pointer that is provided
        #   - This is so that function is run at least once in case of a quick button press
        if function is not None:
            ret_val = function()

        # Wait for button press
        while (GPIO.input(button) == 1):
            # Optinally execute function pointer that is provided
            if function is not None:
                ret_val = function()

            # Sleep for a short period of time to reduce CPU load
            time.sleep(0.1)

        # Record time
        button_press_time = time.time()

        # Wait for button release
        while (GPIO.input(button) == 0):
            # Sleep for a short period of time to reduce CPU load
            time.sleep(0.1)


    def run(self):
        #arm the system
        while True:
            # check if the system is armed
            while self.button.is_pressed():
                if self.motionSensor.is_motion_detected():
                    message = self.client.messages.create(
                        body=f"someone is in your room!!! at {time.time()}",
                        from_='YOUR_TWILIO_NUMBER',
                        to=self.myNumber
                    )
                else:
                    time.sleep(2) # save cpu
            while not self.button.is_pressed():
                time.sleep(10)
                # save cpu and just sleep



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Starting the program")

    # Create instantiation of the lock
    securitySystem = security()

    try:
        # Run the lock
        securitySystem.run(button_pin="P1_08", motion_pin="P1_10", led_pin="P2_04")

    print("Program Complete and terminating")
