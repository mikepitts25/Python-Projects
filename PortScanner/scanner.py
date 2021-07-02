import sys


def bye():
    print("Please enter a valid IPv4 address as an argument!")
    exit()


n = len(sys.argv)

if n < 2:
    bye()

target = sys.argv[1]
print("\nTarget entered: {0}".format(target))

if target.count('.') != 3:
    bye()
else:
    octets = target.split('.')

for num in octets:
    numInt = int(num)
    if numInt <= 0 or numInt > 255:
        bye()


def scanner(ip):
    ports = input("Enter the port or port range to scan (Ex. 80 or 1-1000: ")

    if ports.count('-') == 1:
        for port in range(int(ports.split('-')[0]), int(ports.split('-')[1])+1):
            print("Scanning {0}:{1}".format(ip, port))
    elif int(ports) >= 0 and int(ports) <= 65535:
        print("Scanning {0}:{1}".format(ip, ports))


scanner(target)
