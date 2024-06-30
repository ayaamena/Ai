import tensorflow as tf
import cv2 
import numpy as np

def MrX7_GetPredictions(imgData):
    model = tf.keras.models.load_model("model_checkpoint.h5")

    img_path = ""
    if imgData is None:
        #img_path = r"WhatsApp Image 2024-02-10 at 21.36.50_1ed35dd9.jpg"
        #img_path = r"photo_2024-05-11_19-45-14.jpg"
        img_path = r"photo_2024-05-11_19-45-11.jpg"
    else:
        img_path = imgData


    img = cv2.imread(img_path)
    #cv2.imshow('image',img)

    #if img is not None and image.shape[0] > 0 and image.shape[1] > 0:
    #cv2.imshow('Image', image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    #else:
        #print("Invalid image dimensions.")
    #cv2.waitKey(0)

    # Load the image
    # Resize the image to (256, 256)
    resized_image = cv2.resize(img, (256, 256))

    # Ensure the resized image has 3 channels (RGB)
    #resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

    # Now, resized_image has the dimensions (256, 256, 3)
    # Load the image
    # Resize the image to (256, 256)
    resized_image = cv2.resize(img, (256, 256))

    # Ensure the resized image has 3 channels (RGB)
    resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

    # Expand the dimensions to create a batch of size 1
    resized_image = np.expand_dims(resized_image, axis=0)

    # Now, resized_image has the shape (1, 256, 256, 3)

    # Assuming `model` is your Keras model
    # Predict using the resized image
    predictions = model.predict(resized_image)
    return predictions


def get_model_weights(model):
    weights = []
    for layer in model.layers:
        if len(layer.get_weights()) > 0:
            weights.append(layer.get_weights()[0])
    return weights

def get_model_weights_percentage(model):
    # حساب المجموع الإجمالي للأوزان
    total_weights_sum = sum(sum(abs(weight.flatten())) for weight in get_model_weights(model))

    # حساب نسبة الوزن لكل طبقة وتخزينها في قائمة
    weights_percentages = [(sum(abs(weight.flatten())) / total_weights_sum) * 100 for weight in get_model_weights(model)]

    return weights_percentages