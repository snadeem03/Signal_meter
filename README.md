# Signal_meter
The Signal Meter Python script monitors and visualizes Wi-Fi signal strength over time using Matplotlib. With real-time data fetching and continuous graph updates, this script offers a simple way to observe changes in signal strength. Just run the script, and watch as the graph dynamically reflects signal fluctuations. 

# USAGE:

1. Open a terminal or command prompt.

2. Navigate to the directory where the `signal_meter.py` file is located.

3. Run the script using the following command: python signal_meter.py

4. The script will continuously fetch the Wi-Fi signal strength and update the graph in real-time.


# NOTE : THIS SCRIPT MAY NOT WORK PROPERLY FOR OTHER PLATFORMS (SUITABLE FOR WINDOWS ONLY)


# CONFIGURATION:
You can customize the behavior of the script by modifying the following parameters in the `signal_meter.py` file:

- `plt.pause(1)`: Adjust the update frequency of the graph in seconds.

# TROUBLESHOOTING:
If you encounter any issues with the script, make sure you have the necessary dependencies installed and that your system's environment is set up correctly.

# CONTRIBUTION:
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

**Note:** This script uses the `subprocess` module to fetch Wi-Fi signal strength. While the script attempts to handle errors gracefully, it's recommended to run the script in an environment where you have appropriate permissions and network access.


