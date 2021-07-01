import sys

n = len(sys.argv)

if n < 2:
    print("Please enter a valid IP address as an argument!")
    exit()

target = sys.argv[1]

print("\nTarget entered: {0}".format(target))



def scanner(target):
    for octet in range(1, 25): #change to 256
        print("Scanning 192.168.4.{0}".format(octet))