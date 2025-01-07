import tensorflow as tf
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import ImageUpload
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the TensorFlow model (ensure the path to your model is correct)
model = tf.keras.models.load_model('PDC/model.h5')

# Map indices to disease names
CLASS_LABELS = {
    0:'Apple___Apple_scab', 
    1:'Apple___Black_rot', 
    2:'Apple___Cedar_apple_rust', 
    3:'Apple___healthy', 
    4:'Blueberry___healthy', 
    5:'Cherry_(including_sour)___Powdery_mildew', 
    6:'Cherry_(including_sour)___healthy', 
    7:'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
    8:'Corn_(maize)___Common_rust_', 
    9:'Corn_(maize)___Northern_Leaf_Blight', 
    10:'Corn_(maize)___healthy', 
    11:'Grape___Black_rot', 
    12:'Grape___Esca_(Black_Measles)', 
    13:'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
    14:'Grape___healthy', 
    15:'Orange___Haunglongbing_(Citrus_greening)', 
    16:'Peach___Bacterial_spot', 
    17:'Peach___healthy', 
    18:'Pepper,_bell___Bacterial_spot', 
    19:'Pepper,_bell___healthy', 
    20:'Potato___Early_blight', 
    21:'Potato___Late_blight', 
    22:'Potato___healthy', 
    23:'Raspberry___healthy', 
    24:'Soybean___healthy', 
    25:'Squash___Powdery_mildew', 
    26:'Strawberry___Leaf_scorch', 
    27:'Strawberry___healthy', 
    28:'Tomato___Bacterial_spot', 
    29:'Tomato___Early_blight', 
    30:'Tomato___Late_blight', 
    31:'Tomato___Leaf_Mold', 
    32:'Tomato Septoria leaf spot', 
    33:'Tomato___Spider_mites Two-spotted_spider_mite', 
    34:'Tomato___Target_Spot', 
    35:'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 
    36:'Tomato___Tomato_mosaic_virus', 
    37:'Tomato___healthy'
    # Add more mappings based 
    # on your model's output classes
}

# Function to preprocess and classify the image
def classify_image(image_path):
    # Load and preprocess the image
    img = load_img(image_path, target_size=(224, 224))  # Resize image to (224, 224)
    img_array = img_to_array(img) / 255.0  # Normalize the image to [0, 1]
    img_array = tf.expand_dims(img_array, axis=0)  # Add batch dimension (1, 224, 224, 3)

    # Predict the class
    predictions = model.predict(img_array)
    predicted_index = predictions.argmax()  # Get the index of the predicted class
    
    # Map the predicted index to the disease name
    disease_name = CLASS_LABELS.get(predicted_index, "Unknown Disease")  # Default to "Unknown Disease" if not found
    return disease_name

# Home view to upload and classify the image
def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the image and get the file path
            obj = form.save()
            
            # Get the prediction
            prediction = classify_image(obj.image.path)  # Get prediction for the uploaded image
            obj.prediction = prediction  # Save prediction to the object
            obj.save()

            # Render the result page with the prediction
            return render(request, 'PDC/result.html', {'object': obj, 'disease': prediction})
    else:
        form = ImageUploadForm()  # Create the form instance for GET request
    
    return render(request, 'PDC/home.html', {'form': form})  # Render the home page with the form
