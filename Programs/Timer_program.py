# Timer program for class, just practice!
# Feb 2nd 2024 :)

from datetime import datetime

def menu_top():
    print("The Timer program")
    print()

def timer_start_stop():
    input("Press Enter to start...")
    time_start = datetime.now()
    print(f"Start time: {time_start.strftime('%Y-%m-%d %H:%M:%S.%f')}")

    input("Press Enter to stop...")
    time_stop = datetime.now()
    print(f"Stop time: {time_stop.strftime('%Y-%m-%d %H:%M:%S.%f')}")

    time_between = time_stop - time_start
    print("\nELAPSED TIME")
    print(f"Time: {time_between}")

def main():
    menu_top()
    timer_start_stop()

if __name__ == "__main__":
    main()
