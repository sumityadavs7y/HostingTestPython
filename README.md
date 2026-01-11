# Flask Hello World Application

A simple Flask application that displays "Hello World" and prints environment variables.

## Features

- Displays a hello message with customizable name from environment variable
- Shows a custom message from an environment variable
- Configurable port via environment variable

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Basic Run
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Run with Environment Variables

Set environment variables before running:

```bash
export NAME="John"
export CUSTOM_MESSAGE="Welcome to my Flask app!"
export PORT=8080
python app.py
```

Or run with inline environment variables:

```bash
NAME="Alice" CUSTOM_MESSAGE="Hello from Flask!" python app.py
```

## Environment Variables

- `NAME` - Name to display in the hello message (default: "World")
- `CUSTOM_MESSAGE` - Custom message to display (default: "No CUSTOM_MESSAGE environment variable set")
- `PORT` - Port to run the application on (default: 5000)

## Example

```bash
# Set environment variables
export NAME="Developer"
export CUSTOM_MESSAGE="This is my first Flask app!"

# Run the application
python app.py
```

Visit `http://localhost:5000` to see the result.

