import os
from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get environment variable (default to 'World' if not set)
    name = os.environ.get('NAME', 'World')
    
    # Get all environment variables for display
    env_var = os.environ.get('CUSTOM_MESSAGE', 'No CUSTOM_MESSAGE environment variable set')
    
    # Create plain text response
    response_text = f"""Hello, {name}!

Environment Variable:
CUSTOM_MESSAGE: {env_var}

Set the NAME and CUSTOM_MESSAGE environment variables to customize this message.
"""
    
    # Return response with text/html content type
    return Response(response_text, mimetype='text/html')

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

