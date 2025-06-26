import matplotlib.pyplot as plt

distances = [10, 20, 30, 40, 50]  # Example distances


# Define the path to your log file
file_path = "C:\\Users\\Owner\\Desktop\\uWaveTest3.txt"

# List to store extracted commands containing "$PUWV3"
puwv3_commands = []
fourth_index_values = []
# Open and read the log file
with open(file_path, "r") as file:
    for line in file:
        # Check if the line contains "$PUWV3"
        if "$PUWV3" in line:
            try:
                # Extract command (everything after INFO: << or INFO: >> if applicable)
                if "INFO: <<" in line or "INFO: >>" in line:
                    command = line.split("INFO: ")[1].strip()
                else:
                    command = line.strip()  # Default to the full line if no "INFO: <<" or "INFO: >>"

                # Add the command to the list
                puwv3_commands.append(command)

                # Split the command by commas and extract the 4th index value
                parts = command.split(",")
                if len(parts) > 3:  # Ensure the 4th index exists
                    fourth_index_values.append(parts[4])
                else:
                    fourth_index_values.append("N/A")  # Use "N/A" if index is missing
            except IndexError:
                print(f"Skipping malformed line: {line.strip()}")

# Print out the list of 4th index values
print("4th Index Values from $PUWV3 Commands:")
for idx, value in enumerate(fourth_index_values, start=1):
    print(f"{idx}: {value}")



#Defining a fucntion to plot 

def plot_values_vs_distance(distances, values):
    """
    Plots the extracted values as a function of distance.
    """
    if len(distances) != len(values):
        print("Error: The number of distances and values must match!")
        return

    # Filter out None values to avoid errors in plotting
    filtered_distances = [distances[i] for i in range(len(values)) if values[i] is not None]
    filtered_values = [values[i] for i in range(len(values)) if values[i] is not None]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_distances, filtered_values, marker="o", linestyle="-", color="b")
    plt.title("MSR vs. Distance (taken in my room)")
    plt.xlabel("Distance (vm)")
    plt.ylabel("MSR value (dB)")
    plt.grid()
    plt.show()

# Main logic
# Plot the values as a function of distance
plot_values_vs_distance(distances, fourth_index_values)
