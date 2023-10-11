from machine import Pin, SoftI2C ,PWM
import ssd1306
from time import sleep
import dht
import umail
import time
import utime
import network
import os
sensor = dht.DHT22(Pin(14))
buzzer=Pin(23,Pin.OUT)
# Your network credentials
ssid = 'Wokwi-GUEST'
password = ''
# Email details
sender_email = ''
sender_name = 'ESP32' #sender name
sender_app_password = 'pqkptmnmbtyotqbw'
recipient_email =''
email_subject ='DHT22 Sensor Readings'
def connect_wifi(ssid, password):
#Connect to your network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
pass
print('Connection Established '+u"\U0001F973")
print(station.ifconfig())
print("Connecting to International Server..."+u"\U0001F927" )
# Connect to your network
connect_wifi(ssid, password)
# ESP32 Pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
smtp.login(sender_email, sender_app_password)
while True:
try:
oled.fill(0)
sensor.measure()
sleep(0.5)
temp = sensor.temperature()
hum = sensor.humidity()
temps = str(temp)
hums = str(hum)
oled.text('Temp:'+temps+'C', 0, 0)  
oled.text('Humidity:'+hums, 0, 15)
oled.text('Project by :', 0, 35)
oled.text('Mayank,Mihir', 0, 45)
oled.text('Honey', 0, 55)
oled.show()
# Send the email
if int(time.time()) % 10 == 0:
smtp.to(recipient_email)
smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
smtp.write("Subject:" + email_subject + "\n")
smtp.write("Temperature is"+temps+'C' )
smtp.write("\n Humidity is"+hums)
smtp.send()
print('Email sent!' + u"\U0001F60E")
except OSError as e:
oled.text('Failed to read sensor.',0,25)
oled.show()
