from src import create_app
import json

with open('config.json') as f:
    config = json.load(f)

app = create_app(config)

if __name__ == '__main__':
    app.run(debug=True, port=config["PORT"])
