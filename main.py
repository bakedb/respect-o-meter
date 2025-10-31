import json, argparse, sys, random
from time import sleep

try:
    from question import q
except ModuleNotFoundError:
    print("Looks like you're missing question.py! Please put it in the same directory as main.py.")
try:
    from loading_animation import loading
except ModuleNotFoundError:
    print("Looks like you're missing loading_animation.py! Please put it in the same directory as main.py.")
try:
    from slow_print import sp
except ModuleNotFoundError:
    print("Looks like you're missing slow_print.py! Please put it in the same directory as main.py.")

# configure execution flags
parser = argparse.ArgumentParser(description="A script that shows how respected you are.")
parser.add_argument("-s", "--start", action="store_true", help="Start the respect diagnostic.")
parser.add_argument("-l", "--list", action="store_true", help="List all previous entries of the diagnostic.")
args = parser.parse_args()

error = "It seems that you have made an invalid selection. Please quit the program with ctrl + C and start again."

# main diagnostic function
def main():
    nameinput = q("nameinput", "What is your name?")
    sp(f"Hello, {nameinput}.\n")
    sleep(1)

    os = q("os", "What operating system do you regularly use?\n1) Windows\n2) macOS\n3) GNU/Linux\n4) BSD\n1, 2, 3, or 4 >")
    if os == "1":
        show_os = "Windows"
    elif os == "2":
        show_os = "macOS"
    elif os == "3":
        show_os = "GNU/Linux"
    elif os == "4":
        show_os = "BSD"
    else:
        sp(error)
    sp(f"{show_os} selected.\n")
    sleep(1)

    if os == "1":
        os_version = q("os_version", f"What version of {show_os} do you regularly use?\n1) Older Windows version\n2) Windows 7\n3) Windows 8/8.1\n4) Windows 10\n5) Windows 11")
        mac = "-1"
        if os_version == "1":
            show_os_version = "Older Windows version" # 100%
        elif os_version == "2":
            show_os_version = "Windows 7" # 100%
        elif os_version == "3":
            show_os_version = "Windows 8/8.1" # 80%
        elif os_version == "4":
            show_os_version == "Windows 10" # 60%
        elif os_version == "5":
            show_os_version == "Windows 11" # -100%
        else:
            sp(error)
        
        sp(f"{show_os_version} selected.\n")
        sleep(1)
    
    if os == "2":
        mac = q("What kind of Mac do you use?\n1) Intel Mac (~2019 and earlier)\n2) Apple Silicon Mac (~2020 and later)\n3) Hackintosh\n4) PowerPC Mac")
        os_version = "-1"
        if mac != "1" or "2" or "3" or "4":
            sp(error)

    if os == "3" or "4":
        distro = q("distro", f"What distribution of {show_os} do you regularly use?") # 100%
        show_os_version = distro
        os_version = "-1"
        mac = "-1"

    sp(f"{distro} selected.\n")
    
    loading()

    os = int(os)
    if os_version:
        os_version = int(os_version)
    if mac:
        mac = int(mac)
    if not distro:
        distro = "N/A"

    points = 0

    if os == 1:
        if os_version == 1 or 2:
            points += 100
        elif os_version == 3:
            points += 80
        elif os_version == 4:
            points += 60
        elif os_version == 5:
            points -= 100
    
    if os == 2:
        if mac == 1:
            points += 60
        elif mac == 2:
            points += 50
        elif mac == 3:
            points += 100
        elif mac == 4:
            points += 90
    
    if os == 3 or 4:
        points += 100
    
    if points < 0:
        response = "Please never use a computer again."
    elif points < 60:
        response = "You have failed the respect test."
    elif points < 70:
        response = "At least you passed."
    elif points < 80:
        response = "You have a moderate amount of respect. Good job."
    elif points < 90:
        response = "You are a well-respected computer user."
    elif points == 100:
        response = "You have gained full respect."
    
    sp(f"You have been given a respect score of {points}%. {response}\n")

    # log response in file
    with open('responses.json', 'a') as t:
        data = json.load(t)
        new_entry = {"name": nameinput, "os": show_os, "os_version": show_os_version, "mac": mac, "distro": distro, "points": points}
        data.append(new_entry)
        loading("Writing to file...")

def list():
    with open('responses.json', 'r') as t:
        data = json.load(t)
    print(data)

# runtime execution (detecting flags)
if args.start:
    main()
elif args.list:
    list()
else:
    # print help if everything else is false
    parser.print_help()