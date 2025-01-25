# run.py

from app import create_app
import sys


sys.path.append("/root/Projects/tone-tales/backend")

app = create_app()

if __name__ == "__main__":
    app.run()

