# Wi-Fi-CSI-Based-Human-Activity

**Wi-Fi CSI-Based Human Activity Detection**

**Overview**

This project explores camera-free human activity detection using Wi-Fi Channel State Information (CSI).

Instead of using a camera, the system analyzes changes in Wi-Fi signal characteristics caused by human movement within the wireless environment.

The project demonstrates how wireless signals can be used to detect changes in human activity while preserving visual privacy.

⸻

Objective

To investigate whether variations in Wi-Fi Channel State Information (CSI) can be used to distinguish between different human activity states without using a camera.

The initial experiment focuses on differentiating between:

* Sitting / Stationary
* Moving

⸻

💡 How It Works

Human movement changes the propagation path of Wi-Fi signals.

These changes affect the measured Channel State Information (CSI).

The general workflow is:

Wi-Fi Signal
     ↓
CSI Measurements
     ↓
Data Collection
     ↓
Signal Processing
     ↓
Pattern Analysis
     ↓
Activity Detection

The system analyzes variations in CSI data and visualizes the resulting patterns to identify differences between stationary and moving states.

⸻

🛠️ Technologies Used

* Python
* NumPy
* Matplotlib
* Wi-Fi Channel State Information (CSI)
* Signal Processing
* Data Visualization

⸻



📊 Experimental Setup

The experiment collects Wi-Fi CSI measurements under different activity conditions.

Two basic conditions were tested:

1. Stationary Condition

The subject remains relatively stationary while CSI measurements are collected.

2. Movement Condition

The subject moves within the monitored wireless environment while CSI measurements are collected.

The resulting CSI variations are analyzed and visualized using Python.

⸻

🔬 Data Processing

The collected CSI data is processed using Python libraries such as NumPy for numerical analysis and Matplotlib for visualization.

The analysis focuses on identifying variations in the wireless signal that correspond to changes in the surrounding environment.

⸻

📈 Results

The experiment demonstrated observable differences in CSI patterns between stationary and movement conditions.

Example results:

Sitting / Stationary

Movement

These visualizations show how human movement can introduce measurable variations in Wi-Fi CSI.

⸻

Privacy Aspect

Unlike camera-based monitoring systems, this approach does not require capturing or storing visual images of the person.

This makes Wi-Fi-based sensing an interesting area for applications where privacy-preserving environmental or activity monitoring is desirable.

⸻

Limitations

This project is an experimental proof of concept and has several limitations:

* The experiment was conducted in a controlled environment.
* Only a limited number of activity conditions were tested.
* CSI measurements can be affected by environmental changes.
* Results may vary depending on Wi-Fi hardware, antenna configuration, distance, and room layout.
* The current implementation is not intended to provide production-level human activity recognition.

⸻

 Future Improvements

Possible improvements include:

* Collecting a larger CSI dataset
* Adding more activity classes
* Applying filtering and noise reduction
* Extracting statistical and frequency-domain features
* Implementing machine-learning-based classification
* Evaluating accuracy using a dedicated test dataset
* Testing the system in different environments
* Developing real-time activity detection

⸻

🧠 Key Learning

This project provided practical exposure to:

* Wi-Fi CSI concepts
* Wireless signal behavior
* Python-based data analysis
* Numerical processing using NumPy
* Signal visualization using Matplotlib
* Privacy-preserving sensing concepts
* Experimental cybersecurity and wireless research

⸻

👨‍💻 Project Status

Status: Experimental / Proof of Concept

The current implementation demonstrates the feasibility of using Wi-Fi CSI variations to distinguish between basic human activity states.

⸻

📜 Disclaimer

This project is intended for educational and research purposes. It does not use cameras or attempt to identify individuals.
