#imports
from flask import Flask, jsonify, request, make_response, render_template
from flask_restful import Api
import json

#Define Flask app
app = Flask(__name__)
Api = Api(app)


#save data to json file
def save_json_file(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f)


#home page
@app.get('/')
def first_run():
    return "Welcome to Soulful Soups API!"
    #return render_template('index.html', soup=soup)


#get all soups in one go
@app.route('/soups/api/all', methods=['GET'])
def get_all_soups():
    with open('./data/soups_recipe.json', 'r') as file:
        all_soups = json.load(file)
    return all_soups, 200


#get specific soup by soup_id
@app.route('/soups/api/<soup_id>', methods=['GET'])
def get_one_soup(soup_id):
    try:
        with open('./data/soups_recipe.json', 'r') as fi:
            one_soup = json.load(fi)

        for soup in one_soup:
            if soup_id in soup:
                return jsonify(soup[soup_id])
        # If the soup ID is not found in any soup data, return a message
        return jsonify({'error': 'Soup not found'}), 404

    except FileNotFoundError:
    # Handle file not found error
        return jsonify({'error': 'File not found'}), 500

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500

#post new soup and save json file
@app.route('/soups/api/new_soup', methods=['POST'])
def post_new_soups():
    req = request.get_json()
    response = {
        "cooking_duration": req.get("cooking_duration"),
        "cooking_instructions": req.get("cooking_instructions"),
        "ingredients": req.get("ingredients"),
        "soup_name": req.get("soup_name")
    }
    res = make_response(jsonify(response), 200)

    # Extract existing soup IDs
    with open('./data/soups_recipe.json', 'r') as f:
        soup_data = json.load(f)

    soup_ids = [int(list(soup.keys())[0].replace('soup', '')) for soup in soup_data]

    # Determine the next available soup ID
    new_soup_id = max(soup_ids) + 1 if soup_ids else 1

    new_soup_key = f"soup{new_soup_id}"
    soup_data.append({new_soup_key: req})

    # Save the updated soup data
    save_json_file(soup_data, './data/soups_recipe.json')
    return jsonify({'message': f'Soup {new_soup_key} added successfully'}), 201
    print(res)


#delete one soup
@app.route('/soups/api/pour_soup/<soup_id>', methods=['DELETE'])
def pour_soup(soup_id):
    with open('./data/soups_recipe.json', 'r') as f:
        soup_data = json.load(f)

    soup_location = int(soup_id.replace("soup", ""))

    del soup_data[soup_location - 1]

    response = {
        "message": "Successfully deleted soup from database"
    }
    save_json_file(soup_data, './data/soups_recipe.json')
    return jsonify(response, 200)


#Flask app run
if __name__ == '__main__':
    app.run(debug=True)
