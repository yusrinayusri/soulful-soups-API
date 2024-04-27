# soulful-soups-API 🥣
<p>A soup recipe RESTful API built using Flask. <i>Nobody in their right mind would turn down a bowl of hearty soup.</i></p>

### Disclaimer:
Although the API will be available publicly, it is currently not hosted anywhere. Development 🌱 <b>In Progress</b> 🌱. 


## How to Use Soupful-Soups-API

### API Methods/Operations

#### #1 Get All Soups (full list)
```bash
curl http://127.0.0.1:5000/soups/api/all
```

#### #2 Get Specific Soup based on soup ID
```bash
curl http://127.0.0.1:5000/soups/api/<soup_id>
```

#### #3 Update new soup to the database
<i>Data currently kept in a JSON file.</i> Please supply below arguments (a must):
<p></p>

```bash
curl -X POST http://127.0.0.1:5000/soups/api/new_soup/ -d '{"soup_name": "Tomato Soup", "ingredients": "Tomatoes, onion, butter", "cooking_duration": "30 minutes", "cooking_instructions": "Cook tomatoes and onion in butter for 30 minutes."}'
```

#### #4 Remove any soup record from database (must know soup ID)

```bash
curl -X DELETE http://127.0.0.1:5000/soups/api/pour_soup/<soup_id> 
```

## Contributing Guide

### Development Setup

1. Clone/Fork Repository

```bash
git clone 
```

2. Run pip install
```python
pip3 install -r requirements.txt
```

3. Run Flask app (dev environment)
```python
flask run
```

### Submitting Pull Requests
1. Clone/Fork this repository
2. Create your feature branch (`git checkout -b feature/<featurename>`)
3. Commit your changes with meaningful comments (`git commit -a -m 'Add feature <details>'`)
4. Push to the branch (`git push origin feature/<featurename>`)
5. Create a new Pull Request



