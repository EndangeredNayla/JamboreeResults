from flask import Flask, render_template, request, redirect, url_for, send_file
from PIL import Image
import os
import tempfile
import threading
import time

app = Flask(__name__)

def delete_file_after_delay(file_path, delay):
    time.sleep(delay)  # Wait for the specified delay
    if os.path.exists(file_path):
        os.remove(file_path)  # Delete the file

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_data():
    # Collecting star and coin amounts for four players
    star_amounts = [
        request.form.get('star_amount_1'),
        request.form.get('star_amount_2'),
        request.form.get('star_amount_3'),
        request.form.get('star_amount_4')
    ]
    coin_amounts = [
        request.form.get('coin_amount_1'),
        request.form.get('coin_amount_2'),
        request.form.get('coin_amount_3'),
        request.form.get('coin_amount_4')
    ]
    turn_count = request.form.get('turn_count')
    board = request.form.get('board')

    # Here you can process the existing images and data in the maps directory
    # For example, you might want to load an image based on the selected board
    board_image_path = os.path.join(f"maps/{turn_count}{board}.png")  # Assuming images are in PNG format

    if not os.path.exists(board_image_path):
        return f"Board image not found: {board_image_path}"

    # Load the board image
    board_image = Image.open(board_image_path)
    
    try:
        p1_star_2 = Image.open(f'number/{int(star_amounts[0][1])}.png')
        board_image.paste(p1_star_2, (500, 120), p1_star_2)
        p1_star_1 = Image.open(f'number/{int(star_amounts[0][0])}.png')
        board_image.paste(p1_star_1, (460, 120), p1_star_1)
    except:
        p1_star_1 = Image.open(f'number/{int(star_amounts[0][0])}.png')
        board_image.paste(p1_star_1, (460, 120), p1_star_1)

    try:
        p2_star_2 = Image.open(f'number/{int(star_amounts[1][1])}.png')
        board_image.paste(p2_star_2, (500, 260), p2_star_2) 
        p2_star_1 = Image.open(f'number/{int(star_amounts[1][0])}.png')
        board_image.paste(p2_star_1, (460, 260), p2_star_1)
    except:
        p2_star_1 = Image.open(f'number/{int(star_amounts[1][0])}.png')
        board_image.paste(p2_star_1, (460, 260), p2_star_1)

    try:
        p3_star_2 = Image.open(f'number/{int(star_amounts[2][1])}.png')
        board_image.paste(p3_star_2, (500, 400), p3_star_2) 
        p3_star_1 = Image.open(f'number/{int(star_amounts[2][0])}.png')
        board_image.paste(p3_star_1, (460, 400), p3_star_1)
    except:
        p3_star_1 = Image.open(f'number/{int(star_amounts[2][0])}.png')
        board_image.paste(p3_star_1, (460, 400), p3_star_1)

    try:
        p4_star_2 = Image.open(f'number/{int(star_amounts[3][1])}.png')
        board_image.paste(p4_star_2, (500, 540), p4_star_2)
        p4_star_1 = Image.open(f'number/{int(star_amounts[3][0])}.png')
        board_image.paste(p4_star_1, (460, 540), p4_star_1) 
    except:
        p4_star_1 = Image.open(f'number/{int(star_amounts[3][0])}.png')
        board_image.paste(p4_star_1, (460, 540), p4_star_1)

    try:
        p1_coin_3 = Image.open(f'number/{int(coin_amounts[0][0])}.png')
        board_image.paste(p1_coin_3, (895, 120), p1_coin_3)
        p1_coin_2 = Image.open(f'number/{int(coin_amounts[0][1])}.png')
        board_image.paste(p1_coin_2, (935, 120), p1_coin_2)
        p1_coin_1 = Image.open(f'number/{int(coin_amounts[0][2])}.png')
        board_image.paste(p1_coin_1, (975, 120), p1_coin_1)
    except:
        try:
            p1_coin_2 = Image.open(f'number/{int(coin_amounts[0][0])}.png')
            board_image.paste(p1_coin_2, (895, 120), p1_coin_2)
            p1_coin_1 = Image.open(f'number/{int(coin_amounts[0][1])}.png')
            board_image.paste(p1_coin_1, (935, 120), p1_coin_1)
        except:
            p1_coin_1 = Image.open(f'number/{int(coin_amounts[0][0])}.png')
            board_image.paste(p1_coin_1, (895, 120), p1_coin_1)

    try:
        p2_coin_3 = Image.open(f'number/{int(coin_amounts[1][0])}.png')
        board_image.paste(p2_coin_3, (895, 260), p2_coin_3) 
        p2_coin_2 = Image.open(f'number/{int(coin_amounts[1][1])}.png')
        board_image.paste(p2_coin_2, (935, 260), p2_coin_2)
        p2_coin_1 = Image.open(f'number/{int(coin_amounts[1][2])}.png')
        board_image.paste(p2_coin_1, (975, 260), p2_coin_1)
    except:
        try:
            p2_coin_2 = Image.open(f'number/{int(coin_amounts[1][0])}.png')
            board_image.paste(p2_coin_2, (895, 260), p2_coin_2)
            p2_coin_1 = Image.open(f'number/{int(coin_amounts[1][1])}.png')
            board_image.paste(p2_coin_1, (935, 260), p2_coin_1)
        except:
            p2_coin_1 = Image.open(f'number/{int(coin_amounts[1][0])}.png')
            board_image.paste(p2_coin_1, (895, 260), p2_coin_1)
    try:
        p3_coin_3 = Image.open(f'number/{int(coin_amounts[2][0])}.png')
        board_image.paste(p3_coin_3, (895, 400), p3_coin_3) 
        p3_coin_2 = Image.open(f'number/{int(coin_amounts[2][1])}.png')
        board_image.paste(p3_coin_2, (935, 400), p3_coin_2)
        p3_coin_1 = Image.open(f'number/{int(coin_amounts[2][2])}.png')
        board_image.paste(p3_coin_1, (975, 400), p3_coin_1)
    except:
        try:
            p3_coin_2 = Image.open(f'number/{int(coin_amounts[2][0])}.png')
            board_image.paste(p3_coin_2, (895, 400), p3_coin_2)
            p3_coin_1 = Image.open(f'number/{int(coin_amounts[2][1])}.png')
            board_image.paste(p3_coin_1, (935, 400), p3_coin_1)
        except:
            p3_coin_1 = Image.open(f'number/{int(coin_amounts[2][0])}.png')
            board_image.paste(p3_coin_1, (895, 400), p3_coin_1)

    try:
        p4_coin_3 = Image.open(f'number/{int(coin_amounts[3][0])}.png')
        board_image.paste(p4_coin_3, (895, 540), p4_coin_3)
        p4_coin_2 = Image.open(f'number/{int(coin_amounts[3][1])}.png')
        board_image.paste(p4_coin_2, (935, 540), p4_coin_2)
        p4_coin_1 = Image.open(f'number/{int(coin_amounts[3][2])}.png')
        board_image.paste(p4_coin_1, (975, 540), p4_coin_1)
    except:
        try:
            p4_coin_2 = Image.open(f'number/{int(coin_amounts[3][0])}.png')
            board_image.paste(p4_coin_2, (895, 540), p4_coin_2)
            p4_coin_1 = Image.open(f'number/{int(coin_amounts[3][1])}.png')
            board_image.paste(p4_coin_1, (935, 540), p4_coin_1)
        except:
            p4_coin_1 = Image.open(f'number/{int(coin_amounts[3][0])}.png')
            board_image.paste(p4_coin_1, (895, 540), p4_coin_1)


    # Process the data as needed
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        modified_image_path = temp_file.name
        board_image.save(modified_image_path)

    # Start a thread to delete the file after 60 seconds
    threading.Thread(target=delete_file_after_delay, args=(modified_image_path, 60)).start()

    # Return the temporary image to the user
    return send_file(modified_image_path)

if __name__ == '__main__':
    app.run(debug=True)