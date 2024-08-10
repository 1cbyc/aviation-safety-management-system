import sys
import os
from app import create_app

# Add the 'web' directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Print the sys.path for debugging
print("sys.path:", sys.path)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)