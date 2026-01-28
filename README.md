# Laptop Price Predictor

A machine learning web application that predicts laptop prices based on various specifications and features. Get instant price estimates for laptops by entering their configuration details!

## Live Demo

🔗 **[Try it Live Here](https://lp-predictor-2efd.onrender.com/ )** 

## About The Project

This is my first machine learning project that helps users estimate laptop prices based on specifications like brand, processor, RAM, storage, screen size, and more. If you're buying a new laptop , this tool gives you a fair price estimate instantly!

### How It Works

The system uses a **Machine Learning Regression Model** trained on real laptop data to predict prices. Simply enter your laptop's specifications, and the model will analyze the features to give you an accurate price prediction with **87% accuracy**!

## Features

- **Instant Price Prediction**: Get laptop price estimates in seconds
- **User-Friendly Interface**: Simple form to input laptop specifications
- **High Accuracy**: Model trained with 87% accuracy
- **Real-Time Results**: Immediate predictions based on your input
- **Multiple Specifications**: Considers brand, processor, RAM, storage, GPU, OS, and more

## Technologies Used

- **Python** - Core programming language
- **Flask** - Web framework for the application
- **Scikit-learn** - Machine learning library
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Pickle** - Model serialization
- **HTML/CSS** - Frontend interface

## Model Information

- **Algorithm**: Regression Model (Random Forest/Linear Regression)
- **Accuracy**: ~87%
- **Training Data**: Laptop specifications and prices from Kaggle
- **Features Used**: Brand, Processor Type, RAM, Storage, GPU, Screen Size, Operating System, Weight, etc.

## Getting Started

Follow these simple steps to run the project on your local machine:

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/Vinay-Saini-0018/laptop_price_predictor.git
   cd laptop_price_predictor
```

2. **Install required packages**
```bash
   pip install -r requirements.txt
```

3. **Run the application**
```bash
   python app.py
```

4. **Open in browser**
```
   Navigate to http://127.0.0.1:5000/ in your web browser
```

## How to Use

1. **Open the Application**: Launch the web app in your browser
2. **Enter Laptop Specs**: Fill in the form with laptop specifications
   - Brand (Dell, HP, Lenovo, Apple, etc.)
   - Processor (Intel i3/i5/i7/i9, AMD Ryzen, etc.)
   - RAM (4GB, 8GB, 16GB, 32GB)
   - Storage (HDD/SSD and size)
   - GPU (Integrated/Dedicated)
   - Screen Size
   - Operating System
3. **Get Prediction**: Click "Predict Price" button
4. **View Results**: See the estimated laptop price instantly!


## Development Process

### Step-by-Step Process:

1. **Data Collection**:
   - Downloaded laptop dataset from Kaggle
   - Dataset contains laptop specifications and prices

2. **Data Preprocessing & Feature Engineering**:
   - Cleaned the data and handled missing values
   - Extracted useful features from raw data
   - Encoded categorical variables (Brand, Processor, OS, etc.)
   - Scaled numerical features for better model performance

3. **Model Training**:
   - Trained multiple regression models
   - Selected the best performing model
   - Achieved **87% accuracy** on test data
   - Fine-tuned hyperparameters for optimal performance

4. **Model Serialization**:
   - Saved the trained model using Pickle (.pkl file)
   - Created data preprocessing pipeline

5. **Web Application Development**:
   - Built Flask web app for user interaction
   - Created HTML forms for input
   - Integrated the ML model for real-time predictions

## Model Performance

- **Training Accuracy**: ~87%
- **Model Type**: Regression (predicts continuous values)
- **Key Features**: Brand, Processor, RAM, Storage, GPU, Screen Size
- **Prediction Speed**: Near-instantaneous
 Open a Pull Request


## 👨‍💻 Author

**Vinay Saini**

- GitHub: [@Vinay-Saini-0018](https://github.com/Vinay-Saini-0018)
