# Spam Detection Project

This project is designed to detect spam and ham emails and URLs using machine learning models saved as pickle files and integrated via an API. The goal is to provide an efficient and accurate way to filter and identify unwanted or malicious content.

## Features

- **Email Classification:** Distinguishes between spam and legitimate (ham) emails.
- **URL Analysis:** Detects suspicious URLs that could be used for phishing or other malicious activities.
- **API Integration:** Provides an interface for real-time detection, allowing other applications or services to leverage the spam detection capabilities.
- **Pre-trained Models:** Utilizes machine learning models stored as pickle files for quick predictions.

## Prerequisites

- **Python 3.x**
- **pip**

### Required Libraries

Listed in `requirements.txt`:
- scikit-learn
- pandas
- numpy
- flask (or another framework if using a different API setup)
- Any additional dependencies specific to your project

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AeroScissors/Spam-Detection.git
   cd Spam-Detection
