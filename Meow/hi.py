import sys
import time
import random

def shutdown_simulation():
    print("System shutdown initiated...")
    time.sleep(2)
    print("Preparing to close all applications...")
    time.sleep(2)
    print("Disconnecting from the network...")
    time.sleep(2)
    print("Finalizing shutdown sequence...")
    time.sleep(2)
    
    # Randomly choose a funny message
    messages = [
        "Oops! Looks like the system is stuck!",
        "Just kidding! The shutdown was cancelled!",
        "Haha, you fell for it! Still here!",
        "This is your computer talking... I'm not shutting down!"
    ]
    
    print(random.choice(messages))
    time.sleep(2)
    print("Returning to normal operation.")
    time.sleep(2)
    print("Have a great day!")

if __name__ == "__main__":
    shutdown_simulation()
