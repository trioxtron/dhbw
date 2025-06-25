from threading import Thread
import time

def print_clock(format:str = "%H:%M:%S"):
    # Format should be in 12h or 24h format
    # 12h format: %I:%M:%S %p
    # 24h format: %H:%M:%S
    while True:
        print(time.strftime(format, time.localtime()))
        time.sleep(1)

def wait_for_input():
    while True:
        user_input = input("Enter something: ")
        if user_input.lower() == '1':
            return "%I:%M:%S %p"
        elif user_input.lower() == '2':
            return "%H:%M:%S"

def main():
    format = "%H:%M:%S"
    # Start the clock thread
    clock_thread = Thread(target=print_clock, args=(format,))
    clock_thread.daemon = True  # Daemonize thread
    clock_thread.start()

    # Wait for user input to change the format
    while True:
        new_format = wait_for_input()
        if new_format == "%I:%M:%S %p":
            print("Changing format to 12h")
            format = "%I:%M:%S %p"
        elif new_format == "%H:%M:%S":
            print("Changing format to 24h")
            format = "%H:%M:%S"
        else:
            print("Invalid input, please enter '1' for 12h or '2' for 24h")

        # Stop the current clock thread
        clock_thread.join(timeout=0)
        # Check if the thread is still alive
        if clock_thread.is_alive():
            print("Clock thread is still running, stopping it...")
            clock_thread.join()
        # Restart the clock thread with the new format
        clock_thread = Thread(target=print_clock, args=(format,))
        clock_thread.daemon = True
        clock_thread.start()


if __name__ == "__main__":
    main()
