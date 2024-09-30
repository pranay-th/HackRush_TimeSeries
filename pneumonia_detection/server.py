import os
import io
from flask import Flask, request, jsonify
from kagglehub import model_download
import kagglehub
import torch
from PIL import Image
from torchvision import transforms

app = Flask(__name__)

model_path = kagglehub.model_download("huutai23012003/googlenet-chest-xray-pneumonia/pyTorch/default")
model = torch.load(os.path.join(r"C:\Users\Pranay Thakur\.cache\kagglehub\models\huutai23012003\googlenet-chest-xray-pneumonia\pyTorch\default\1", "model.pt"))
model.eval()

# Transform for input images
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    return image

def postprocess_output(output):
    # Assume the model outputs a mask or bounding box
    # This is a placeholder function, replace it with actual post-processing logic
    return output

@app.route('/process', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    image = preprocess_image(file)
    with torch.no_grad():
        output = model(image)

    # Convert output to base64 for displaying in HTML
    postprocessed_output = postprocess_output(output)
    buffered = io.BytesIO()
    postprocessed_output.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return jsonify({'image': img_str})

if __name__ == '__main__':
    app.run(debug=True)