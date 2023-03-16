import subprocess
import time

while True:
    # Lock screen
    subprocess.call(["/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession", "-suspend"])
    
    # Request reason for unlocking
    reason = input("Enter reason for unlocking: ")
    while not reason:
        reason = input("Please enter a reason to unlock: ")
    
    # Wait for 30 minutes
    time.sleep(1800)
