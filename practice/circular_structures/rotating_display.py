import time
import os

class RotatingDisplay:
    def __init__(self, text, width=20):
        self.text = text + "   " # Adding padding
        self.width = width
        self.offset = 0

    def get_frame(self):
        full_text = self.text
        n = len(full_text)
        
        # Extract window
        frame = ""
        for i in range(self.width):
            frame += full_text[(self.offset + i) % n]
        
        self.offset = (self.offset + 1) % n
        return frame

    def run(self, iterations=10):
        print("Starting Rotating Display...")
        for _ in range(iterations):
            # os.system('clear' if os.name == 'posix' else 'cls')
            print(f"| {self.get_frame()} |", end="\r")
            time.sleep(0.2)
        print("\nDisplay finished.")

if __name__ == "__main__":
    display = RotatingDisplay("SALE NOW ON! 50% OFF ALL ITEMS", width=15)
    # Using small number for automated test
    display.run(iterations=5)
    print("Rotating Display simulation complete.")
