import serial
ard = serial.Serial('/dev/tty96B0', 9600)

if __name__ == '__main__':
    print("Welcome to the jungle")
    try:
        while True:
            ardOut = ard.readline()
            print(ardOut)
    except KeyboardInterrupt:
        print("Exiting.")
