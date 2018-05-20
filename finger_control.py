import serial
import time
import keyboard

print("Opening Serial Port...")
arduino = serial.Serial('com5',baudrate=9600, timeout = 1)
time.sleep(2)
print("Initialize Complete")


last = 0
while True:
    if keyboard.is_pressed('q'):
        if last != 'q':
            print('q')
            arduino.write(b'q')
            last = 'q'
    if keyboard.is_pressed('w'):
        if last != 'w':
            print('w')
            arduino.write(b'w')
            last = 'w'
    if keyboard.is_pressed('e'):
        if last != 'e':
            print('e')
            arduino.write(b'e')
            last = 'e'
    if keyboard.is_pressed('r'):
        if last != 'r':
            print('r')
            arduino.write(b'r')
            last = 'r'
    if keyboard.is_pressed('t'):
        if last != 't':
            print('t')
            arduino.write(b't')
            last = 't'

    if keyboard.is_pressed('a'):
        if last != 'a':
            print('a')
            arduino.write(b'a')
            last = 'a'
    if keyboard.is_pressed('s'):
        if last != 's':
            print('s')
            arduino.write(b's')
            last = 's'
    if keyboard.is_pressed('d'):
        if last != 'd':
            print('d')
            arduino.write(b'd')
            last = 'd'
    if keyboard.is_pressed('f'):
        if last != 'f':
            print('f')
            arduino.write(b'f')
            last = 'f'
    if keyboard.is_pressed('g'):
        if last != 'g':
            print('g')
            arduino.write(b'g')
            last = 'g'

    if keyboard.is_pressed('z'):
        break

print("done")
