# 🏠 House Price Prediction Web Application

## 📌 Overview
This project is a web application built using Django that predicts house prices based on user input. It utilizes a linear regression model trained on a dataset of house features to estimate the price of a property.

## 🌟 Features
- 🎨 User-friendly web interface
- 🎭 Dynamic background with CSS styling
- 📝 Form-based input for house features
- 🔍 Predicts house prices using a trained linear regression model
- 🛠 Handles missing or incorrect input values gracefully

## 🛠 Technologies Used
- 🐍 **Python** (Django, NumPy, Pandas, Scikit-Learn)
- 🎨 **HTML, CSS** (Frontend UI with a modern design)
- ⚡ **JavaScript** (for interactive elements)

## 📦 Installation
### 🔧 Prerequisites
Ensure you have the following installed:
- 🐍 Python (>= 3.7)
- 🌐 Django (>= 3.0)
- 📊 Scikit-learn
- 🗃 Pandas
- 🔢 NumPy

### 🚀 Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/house-price-prediction.git
   cd house-price-prediction
   ```

2. **Create a Virtual Environment and Activate It:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the Django Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## 🎯 Usage
1. Click on the **Start** button to access the prediction page.
2. Enter the required house features:
   - 💰 Average Area Income
   - 🏠 Average Area House Age
   - 🏘 Average Area Number of Rooms
   - 🛏 Average Area Number of Bedrooms
   - 🌍 Average Area Population
3. Click on the **Predict** button.
4. The predicted house price will be displayed.

## 📁 Project Structure
```
House-Price-Prediction/
│── house_price/         # Main Django app
│   │── templates/       # HTML templates
│   │── static/          # Static assets (CSS, JS, images)
│   │── views.py         # Django views
│   │── urls.py          # URL configuration
│   │── models.py        # Database models (if required)
│── manage.py            # Django management script
│── requirements.txt     # Required Python dependencies
│── USA_Housing.csv      # Dataset used for training
```

## 📊 Model Training
The model is trained using **Linear Regression** from Scikit-Learn. The dataset (USA_Housing.csv) includes columns such as:
- 💰 `Avg. Area Income`
- 🏠 `Avg. Area House Age`
- 🏘 `Avg. Area Number of Rooms`
- 🛏 `Avg. Area Number of Bedrooms`
- 🌍 `Avg. Area Population`
- 🎯 `Price` (Target Variable)

The `result` function in `views.py` processes user input and predicts the house price using the trained model.

##
