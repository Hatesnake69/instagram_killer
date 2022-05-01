from app import app
import os

if __name__ == '__main__':
    os.makedirs('app/static/uploads', exist_ok=True)
    app.run(debug=True)
