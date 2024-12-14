# Smart Disaster Relief

## Overview
The **Smart Disaster Relief** project aims to revolutionize disaster management by integrating drones, machine learning, NLP, and real-time communication technologies. The system is designed to assist in locating injured individuals, processing their audio signals, and transmitting critical information to rescue teams via a user-friendly dashboard.

## Features
- **Drone Management**: Deploy and monitor drones for real-time rescue operations.
- **Audio Processing**: Capture and process audio signals to identify human voices in disaster zones.
- **Real-Time Data Processing**: Receive and visualize real-time data from drones, including GPS coordinates and alerts.
- **Alert System**: Generate and manage alerts based on data analysis.
- **Machine Learning Models**: Classify and prioritize rescue alerts using AI.
- **LoRa Communication**: Enable long-range wireless data transmission using LoRa technology.

## Project Structure
The repository is organized as follows:

- **Alert_System/**: Contains the logic for generating and managing disaster alerts.
- **Audio_Processing/**: Includes scripts and models for processing audio data.
- **BackendServer/**: Supports the backend operations, built using Django.
- **Drone_Management/**: Handles drone deployment and GPS tracking.
- **ML_Models/**: Contains machine learning models for classification and analysis.
- **Real_Time_Data/**: Manages real-time data collection and visualization.

## Prerequisites
To set up and run the project, ensure you have the following installed:

- **Python 3.8+**
- **Django 4.0+**
- **ReactJS** (for the frontend)
- **Redis** and **Celery** (for task management)
- **LoRa Communication Modules** (e.g., Waveshare SX1262 LoRa HAT)
- **Raspberry Pi**

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Bandar-Sh/Smart_Disaster_Relief.git
   cd Smart_Disaster_Relief
   ```

2. Install dependencies:
   - Using the `requirements.txt` file:
     - Ensure `pip` is installed, then run:
       ```bash
       pip install -r requirements.txt
       ```
   - Alternatively, if you prefer `pipenv`, first install it:
     ```bash
     pip install pipenv
     ```
     Then, install the required packages using:
     ```bash
     pipenv install
     ```

3. Activate the virtual environment (if using `pipenv`):
   ```bash
   pipenv shell
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Navigate to `http://127.0.0.1:8000/` to access the application.

## Usage
- **Deploy Drones**: Use the dashboard to assign drones to specific areas.
- **Monitor Audio**: Analyze audio signals captured by the drones to detect voices.
- **Generate Alerts**: Use the alert system to notify rescue teams of potential survivors.
- **Visualize Data**: View real-time GPS and audio data on the dashboard.

## Technologies Used
- **Frontend**: ReactJS
- **Backend**: Django
- **Database**: MySQL
- **Task Management**: Celery with Redis
- **Hardware**:
  - Raspberry Pi
  - Waveshare SX1262 LoRa HAT
  - MAX9814 Electret Microphone
  - Ublox NEO-6M GPS Module
- **Machine Learning**: Scikit-learn, TensorFlow
- **NLP**: Natural Language Toolkit (NLTK)
