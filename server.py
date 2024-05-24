from flask import Flask, render_template, send_file, request
import os
import removebg

app = Flask(__name__, static_url_path='/static')

# Define the directory to save uploaded files
UPLOADS_DIR = os.path.join(os.path.dirname(__file__), 'uploads')

@app.route('/')
def index():
    return render_template('index.html')

D_DIR = os.path.join(os.path.dirname(__file__), 'removed_images')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    global uploaded_file_pat
    file = request.files['file']
    if file:
        # Create the 'uploads' directory if it doesn't exist
        os.makedirs(UPLOADS_DIR, exist_ok=True)

        # Save the file to the 'uploads' directory
        file_path = os.path.join(UPLOADS_DIR, file.filename)
        try:
            file.save(file_path)
            # Store the file path in a variable and print it
            uploaded_file_path = file_path
            os.makedirs(D_DIR, exist_ok=True)
            download_file_path = os.path.join(D_DIR, 'output_image.png')
            removebg.remove_background(uploaded_file_path, download_file_path, 'e1BA4hMvom21bGBbHyzxaaei')#Replace with your API key from remove.bg/tools-api

        except Exception as e:
            return f'Failed to save file: {str(e)}', 500

    return uploaded_file_path



@app.route('/get_image/<filename>')
def uploaded_file(filename):
    image_path = os.path.join('removed_images', filename)  # Your updated image path
    return send_file(image_path, mimetype='image/png')



@app.route('/download-image')
def download_image():
    IMAGE_PATH = os.path.join(D_DIR, 'output_image.png')
    return send_file(IMAGE_PATH, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
