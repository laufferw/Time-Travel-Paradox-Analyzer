import sys
import threading
import time
import itertools


class ProgressSpinner:
    """
    A simple terminal spinner to indicate progress.
    Displays an animated spinner with a custom message.
    """

    def __init__(self, message="Processing...", spinner_chars="|/-\\"):
        """
        Initialize the spinner with a custom message and spinner characters.
        
        Args:
            message (str): The message to display alongside the spinner.
            spinner_chars (str): Characters to use for the spinner animation.
        """
        self.message = message
        self.spinner_chars = spinner_chars
        self.stop_event = threading.Event()
        self.spinner_thread = None
        self.is_running = False

    def _spin(self):
        """
        Internal method to display the spinning animation.
        """
        spinner = itertools.cycle(self.spinner_chars)
        while not self.stop_event.is_set():
            sys.stdout.write(f"\r{self.message} {next(spinner)} ")
            sys.stdout.flush()
            time.sleep(0.1)
        
        # Clear the spinner when stopped
        sys.stdout.write(f"\r{' ' * (len(self.message) + 2)}\r")
        sys.stdout.flush()

    def start(self):
        """
        Start the spinner animation in a separate thread.
        """
        if self.is_running:
            return
        
        self.stop_event.clear()
        self.spinner_thread = threading.Thread(target=self._spin)
        self.spinner_thread.daemon = True
        self.spinner_thread.start()
        self.is_running = True

    def stop(self):
        """
        Stop the spinner animation.
        """
        if not self.is_running:
            return
        
        self.stop_event.set()
        if self.spinner_thread and self.spinner_thread.is_alive():
            self.spinner_thread.join()
        self.is_running = False

    def update_message(self, message):
        """
        Update the message displayed alongside the spinner.
        
        Args:
            message (str): The new message to display.
        """
        self.message = message


# Example usage:
if __name__ == "__main__":
    # Example of how to use the spinner
    spinner = ProgressSpinner("Working on it")
    spinner.start()
    
    try:
        # Simulate work
        for i in range(10):
            time.sleep(1)
            if i == 5:
                spinner.update_message("Almost done")
    finally:
        spinner.stop()
        print("Completed!")

