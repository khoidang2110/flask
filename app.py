# app.py
from src.infrastructure.web.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6001, debug=True)  # đổi port ở đây
