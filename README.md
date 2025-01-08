# **Plant Disease Classification**

This project leverages deep learning techniques to identify and classify diseases in plants based on images. The aim is to assist farmers, gardeners, and agricultural researchers in diagnosing plant health issues efficiently.

---

## **Features**
- **AI-Powered Disease Detection**: Quickly and accurately identifies diseases from plant images.
- **User-Friendly Web Interface**: Accessible via a simple browser-based interface.
- **Interactive Predictions**: Upload an image and receive detailed results with suggestions for remedies.
- **Scalable**: Designed to handle multiple disease categories with high accuracy.

---


## **Installation**

Follow these steps to set up the project locally:

### **Prerequisites**
Ensure you have the following installed:
- Python 3.8 or later
- pip (Python package manager)
- SQLite (default database for Django)

### **Steps**
1. **Clone the Repository**  
   Open your terminal and run:
   ```bash
   git clone https://github.com/Edina-24/Plant_Disease_Identification.git
   cd Plant_Disease_Identification

2. **Create a Virtual Environment**
   Set up an isolated Python environment to manage dependencies:
   ```bash
   python -m venv venv 
   source venv/bin/activate  # For macOS/Linux 
   venv\Scripts\activate     # For Windows

3. **Install Required Libraries**
   Use pip to install dependencies from the requirements.txt file:
   ```bash
   pip install -r requirements.txt
   
4. **Run Database Migrations**
   Prepare the database by applying migrations:
   ```bash
   python manage.py makemigrations 
   python manage.py migrate
5. **Start the Development Server**
   Launch the web application:
   ```bash
   python manage.py runserver
6. **Access the Application**
   Open your browser and navigate to:
   ```bash
   http://127.0.0.1:8000
