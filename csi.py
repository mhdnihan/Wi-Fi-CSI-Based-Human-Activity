import re
import numpy as np
import matplotlib.pyplot as plt

def read_csi(filename):
    samples = []

    with open(filename, "r", errors="ignore") as file:
        for line in file:
            if "CSI:" not in line:
                continue

            values = line.split("CSI:", 1)[1]

            numbers = re.findall(r"-?\d+", values)

            if numbers:
                samples.append([int(x) for x in numbers])

    return np.array(samples, dtype=object)


empty = read_csi("person_moving.txt")
sitting = read_csi("person_sitting.txt")

print("Empty-room samples:", len(empty))
print("Sitting samples:", len(sitting))

# Convert each CSI sample into a simple magnitude measure
def calculate_amplitude(data):
    result = []

    for sample in data:
        sample = np.array(sample, dtype=float)

        # RMS amplitude
        amplitude = np.sqrt(np.mean(sample ** 2))
        result.append(amplitude)

    return np.array(result)


empty_amp = calculate_amplitude(empty)
sitting_amp = calculate_amplitude(sitting)

# Plot
plt.figure(figsize=(12, 5))

plt.plot(empty_amp, label="Empty room")
plt.plot(sitting_amp, label="Person sitting")

plt.xlabel("CSI sample")
plt.ylabel("CSI amplitude")
plt.title("ESP32 CSI Comparison")
plt.legend()
plt.grid(True)

plt.show()