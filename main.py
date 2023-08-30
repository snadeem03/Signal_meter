import subprocess
import time
import matplotlib.pyplot as plt
import re

# Initialize lists to store data
timestamps = []
signal_strengths = []


# Function to fetch the signal strength
def get_signal_strength():
    try:
        result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True,check=True,timeout=10).stdout
        signal_strength_match = re.search(r"Signal\s+:\s+(\S+)", result)

        if signal_strength_match:
            signal_strength = signal_strength_match.group(1)
            integer_strength = int(signal_strength.strip('%'))
            return integer_strength
        else:
            return None
    except subprocess.CalledProcessError as e:
        print("Cannot fetch the signal strength ")
        print(f"More details regarding error : {e}")
    except subprocess.TimeoutExpired as e:
        print("Taking longer time than usual")
        print(f"More details about the error {e}")
    except subprocess.SubprocessError as e:
        print("An unknown error had occured")
        print(f"More details regarding error {e}")



# Function to update the graph
def update_graph(timestamps, signal_strengths):
    timestamps.append(time.time())
    signal_strengths.append(float(get_signal_strength()))


# Function to plot the graph
def plot_graph(timestamps, signal_strengths):
    plt.clf()
    plt.plot(timestamps, signal_strengths, 'o--r', linewidth=2)
    plt.xlabel('Time')
    plt.ylabel('Signal Strength in percentage')
    plt.title('Signal Strength Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()


# Main function
def main():
    plt.ion()  # Turn on interactive mode for continuous updates
    plt.figure()

    while True:
        update_graph(timestamps, signal_strengths)
        plot_graph(timestamps, signal_strengths)
        plt.pause(1)  # Update frequency in seconds


if __name__ == "__main__":
    main()
