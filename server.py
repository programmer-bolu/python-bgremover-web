from flask import Flask, render_template, send_file, send_from_directory, request
import os
import removebg

app = Flask(__name__, static_url_path='/static')

# Define the directory to save uploaded files
UPLOADS_DIR = os.path.join(os.path.dirname(__file__), 'uploads')

@app.route('/')
def index():
    return render_template('index.html')


uploaded_file_path = ''

@app.route('/upload', methods=['POST'])
def upload():
    global uploaded_file_path
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    if file:
        # Create the 'uploads' directory if it doesn't exist
        os.makedirs(UPLOADS_DIR, exist_ok=True)

        # Save the file to the 'uploads' directory
        file_path = os.path.join(UPLOADS_DIR, file.filename)
        try:
            file.save(file_path)
        except Exception as e:
            return f'Failed to save file: {str(e)}', 500
        
        # Store the file path in a variable and print it
        uploaded_file_path = file_path

        removebg.remove_background(uploaded_file_path, 'e1BA4hMvom21bGBbHyzxaaei')#Replace with your API key from remove.bg/tools-api
    return uploaded_file_path



@app.route('/get_image/<filename>')
def uploaded_file(filename):
    image_path = os.path.join('removed_images', filename)  # Your updated image path
    return send_file(image_path, mimetype='image/png')










IMAGE_PATH = 'C:\\Users\\Boluwatife\Desktop\\Bg-Remover-Flask\\removed_images\\output_image.png'

@app.route('/download-image')
def download_image():
    return send_file(IMAGE_PATH, as_attachment=True)
    


if __name__ == '__main__':
    app.run(debug=True)
