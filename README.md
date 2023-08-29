# Image Captioning with Transformer - CNN & NLP

<img width="925" alt="2k_pictures" src="https://github.com/herish23/ImageCaptioner/assets/87555721/25106d8c-0bec-4823-8cf9-1a1b63376a69">

This repository contains code for an image captioning model using a Transformer architecture implemented with TensorFlow. The model takes an input image and generates a descriptive caption for the image using a trained Transformer-based decoder. It uses Convolutional Neural Networks (CNNs) and Natural Language Processing to generate captions correspondingly 

## Prerequisites

- TensorFlow
- pandas
- numpy
- collections
- requests
- PIL (Pillow)

## Usage

### Data Preparation

1. You may use the 8k dataset staright from (https://www.kaggle.com/datasets/adityajn105/flickr8k?resource=)
2. `deleter.py` reduces number os images to needs and reformats into `selected_images` and `selected_captions.txt`

1. Open the provided script file (`main.py`) in your Python environment used 3.11

### Configure Parameters

1. Configure various parameters in the script, such as `MAX_LENGTH`, `VOCABULARY_SIZE`, `BATCH_SIZE`, etc., according to your requirements.

### Execute the Script

1. Run the script. It will preprocess the data, build and train the image captioning model, and generate captions for provided images.

### Generated Captions

- After training, the model will be able to generate captions for new images.
- You can use the `generate_caption(img_path)` function to generate captions for specific images.

### Predict with External Images

- You may use a URL to an image to generate captions using fetch 

## Model Components

- **TransformerEncoderLayer:** A layer responsible for encoding image embeddings using a Transformer encoder.
- **Embeddings:** A layer for generating embeddings, including both token embeddings and positional embeddings.
- **TransformerDecoderLayer:** A layer for generating caption tokens using a Transformer decoder. It uses the encoder's output and previously generated tokens as input.
- **ImageCaptioningModel:** The main image captioning model, which combines the encoder and decoder. It handles training and evaluation.

## Training and Testing

- The model is trained using the training dataset and validated using the validation dataset.
- Training progress and validation metrics (loss and accuracy) are displayed during training.




Feel free to customize the parameters, model architecture, and training process as needed for your specific project.
