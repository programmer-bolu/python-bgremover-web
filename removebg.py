import requests

def remove_background(image_path, api_key):
    # Read the image file
    with open(image_path, 'rb') as file:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': file},
            data={'size': 'auto'},
            headers={'X-Api-Key': api_key},
        )

    if response.status_code == requests.codes.ok:
        with open('C:\\Users\\Boluwatife\Desktop\\Bg-Remover-Flask\\removed_images\\output_image.png', 'wb') as out_file:
            out_file.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

