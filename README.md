# Flask App with Frontend and Backend

This project is a simple Flask application with a backend API and a frontend served by Flask. It is containerized using Docker.

## Structure

- `backend/`: Flask backend (API and server)
- `frontend/`: HTML frontend
- `Dockerfile`: For building the Docker container

## Running Locally

### 1. Install dependencies

```
pip install -r backend/requirements.txt
```

### 2. Run the Flask app

```
python backend/app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Running with Docker

Build and run the container:

```
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

Then open [http://localhost:5000](http://localhost:5000).
