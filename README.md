# ESPN32-mini-project
Weather (temp. and humidity) monitoring on OLED display with Realtime Email Reporting

THEORY


from machine import Pin, SoftI2C, PWM
This line imports specific classes (Pin, SoftI2C, PWM) from the machine module. These classes allow us
to control various hardware components of the microcontroller.
import ssd1306
This line imports thessd1306 module, which provides functionality to interact with OLED displays.
from time import sleep
This line imports the sleep function from the time module. The sleep function is used to introduce
delays in the program execution.
This line imports the dht module, which allows us to read temperature and humidity data from
DHT sensors.
import umail
This line imports the umail module, which provides functionality for sending emails.
import time
import utime
These lines import the time and utime modules, which provide functions for working with timerelated operations.
import network
This line imports the network module, which allows us to connect to Wi-Fi networks.
import os
This line imports the os module, which provides access to operating system-related functionalities.
sensor = dht.DHT22(Pin(14))
This line creates an instance of the DHT22 class from the dht module, representing the DHT22
temperature and humidity sensor connected to pin 14 of the microcontroller. It assigns this
instance to the variable sensor.
buzzer = Pin(23, Pin.OUT)
This line creates an instance of the Pin class from the machine module, representing the buzzer
connected to pin 23 of the microcontroller. It assigns this instance to the variable buzzer.
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
This line creates an instance of the SoftI2C class from the machine module, representing the I2C
communication interface. It specifies that the clock line (SCL) is connected to pin 22 and the data
line (SDA) is connected to pin 21. It assigns this instance to the variable i2c.
oled_width = 128
oled_height = 64
These lines define variables oled_width and oled_height to specify the dimensions of the OLED
display. In this case, the display has a width of 128 pixels and a height of 64 pixels.
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
This line creates an instance of the SSD1306_I2C class from the ssd1306 module, representing the
OLED display. It takes the specified width, height, and I2C interface (i2c) as arguments. It assigns
this instance to the variable oled.
smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True)
This line creates an instance of the SMTP class from the umail module, representing the Simple Mail
Transfer Protocol (SMTP) connection. It specifies the SMTP server address, port number, and
enables SSL encryption. It assigns this instance to the variable smtp.
def connect_wifi(ssid, password):
 station = network.WLAN(network.STA_IF)
 station.active(True)
 station.connect(ssid, password)
 while station.isconnected() == False:
 pass
 print('Connection Established ' + u"\U0001F973")
 print(station.ifconfig())
This code defines a function named connect_wifi that takes two parameters: ssid (Wi-Fi network
name) and password (network password). Inside the function, it creates a Wi-Fi station interface,
activates it, and attempts to connect to the specified network using the provided SSID and
password. It waits in a loop until the connection is established. Finally, it prints a success message
and the network configuration.
print("Connecting to International Server..." + u"\U0001F927")
connect_wifi(ssid, password)
This line prints a message to indicate that the program is attempting to connect to a Wi-Fi
network. Then, it calls the connect_wifi function with the provided SSID and password to establish
the connection.
The remaining lines of the code are within a while True: loop, which means they will be executed
repeatedly.
try:
 oled.fill(0)
 sensor.measure()
 sleep(0.5)
 temp = sensor.temperature()
 hum = sensor.humidity()
 temps = str(temp)
 hums = str(hum)
Inside the loop, it starts with a try block. The OLED display is cleared (oled.fill(0)). The
temperature and humidity are measured by calling sensor.measure(). A brief delay of 0.5 seconds is
introduced using sleep(0.5) to allow the sensor to stabilize. The temperature and humidity values
are then obtained and converted to strings.
oled.text('Temp:' + temps + 'C', 0, 0)
 oled.text('Humidity:' + hums, 0, 15)
 oled.text('Project by :', 0, 35)
 oled.text('Mayank,Mihir', 0, 45)
 oled.text('Honey', 0, 55)
 oled.show()
The temperature and humidity values are displayed on the OLED screen using the oled.text()
function. Each line of text is positioned at specific coordinates on the screen. The oled.show()
function updates the display to reflect the changes.
 if int(time.time()) % 10 == 0:
 smtp.to(recipient_email)
 smtp.write("From:" + sender_name + "<" + sender_email + ">\n")
 smtp.write("Subject:" + email_subject + "\n")
 smtp.write("Temperature is" + temps + 'C')
 smtp.write("\n Humidity is" + hums)
 smtp.send()
 print('Email sent!' + u"\U0001F60E")
This conditional block checks if the current time is a multiple of 10 (every 10 seconds). If it is, an
email is sent using the SMTP object (smtp). The recipient, sender, subject, and content of the email
are specified. Finally, a success message is printed to the console.
except OSError as e:
 oled.text('Failed to read sensor.', 0, 25)
 oled.show()
If an OSError occurs while reading the sensor (e.g., a communication error), an exception is caught,
and an error message is displayed on the OLED screen. The error message is positioned at specific
coordinates, and the display is updated.
The loop then repeats, continuously measuring sensor readings, updating the OLED display, and
potentially sending emails.
