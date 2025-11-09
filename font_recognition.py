import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import InputLayer

# Define a custom InputLayer to handle 'batch_shape' parameter
class CustomInputLayer(InputLayer):
    def __init__(self, *args, **kwargs):
        # Extract 'batch_shape' if present and convert to 'batch_input_shape'
        batch_shape = kwargs.pop('batch_shape', None)
        if batch_shape is not None:
            kwargs['batch_input_shape'] = batch_shape
        super().__init__(*args, **kwargs)

# Load the model with the custom InputLayer
model = load_model('model/font_classifier_model.h5', custom_objects={'InputLayer': CustomInputLayer})


# Load your pre-trained model
# model = load_model('model/font_classifier_model.h5') 

# Create your font label mapping
font_labels = {
    0: 'Agency',
    1: 'Akzidenz Grotesk',
    2: 'Algerian',
    3: 'Arial',
    4: 'Baskerville',
    5: 'Bell MT',
    6: 'Bembo',
    7: 'Bodoni',
    8: 'Book Antiqua',
    9: 'Brandish',
    10: 'Calibry',
    11: 'Californian FB',
    12: 'Calligraphy',
    13: 'Calvin',
    14: 'Cambria',
    15: 'Candara',
    16: 'Century',
    17: 'Comic Sans MS',
    18: 'Consolas',
    19: 'Corbel',
    20: 'Courier',
    21: 'Didot',
    22: 'Elephant',
    23: 'Fascinate',
    24: 'Franklin Gothic',
    25: 'Futigre',
    26: 'Futura',
    27: 'Garamond',
    28: 'Georgia',
    29: 'Gill Sans',
    30: 'Helvetica',
    31: 'Hombre',
    32: 'Lato',
    33: 'LCD Mono',
    34: 'Lucida Bright',
    35: 'Monotype Corsiva',
    36: 'Mrs Eaves',
    37: 'Myriad',
    38: 'Nasalization',
    39: 'News Gothic',
    40: 'Palatino linotype',
    41: 'Papyrus',
    42: 'Perpetua',
    43: 'Rockwell',
    44: 'Segoe UI',
    45: 'Tahoma',
    46: 'Times New Roman',
    47: 'Verdana'
}

def test_mappings():
    print("\nFont Class Mappings:")
    for idx, name in sorted(font_labels.items()):
        print(f"Class {idx}: {name}")

# Call the test function when the file loads
test_mappings()

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (64, 64))  # Critical dimension change
    img = img / 255.0
    return np.expand_dims(img, axis=0)

def predict_font(image_path):
    processed_img = preprocess_image(image_path)
    predictions = model.predict(processed_img)
    predicted_class = np.argmax(predictions[0])
    return font_labels[int(predicted_class)]  # Convert to int
