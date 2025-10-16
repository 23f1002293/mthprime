from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # Check for odd divisors from 3 up to the square root of num
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def find_nth_prime(n):
    """Finds the nth prime number."""
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

@app.route('/')
def index():
    """Serves the main HTML page."""
    return send_from_directory('.', 'index.html')

@app.route('/api/get_prime')
def api_get_prime():
    """API endpoint to get the nth prime."""
    n_str = request.args.get('n')
    if not n_str:
        return jsonify({"error": "Missing parameter 'n'"}), 400
    
    try:
        n = int(n_str)
        if n <= 0:
             return jsonify({"error": "Input 'n' must be a positive integer."}), 400
        
        # Add a reasonable limit to prevent server overload in this demo
        if n > 10000:
            return jsonify({"error": "For performance reasons, n is limited to 10,000 in this demo."}), 400

        prime = find_nth_prime(n)
        return jsonify({"n": n, "prime": prime})
    except ValueError:
        return jsonify({"error": "Invalid input. 'n' must be an integer."}), 400
    except Exception as e:
        # A generic error for unexpected issues
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # For a real application, use a production-ready WSGI server like Gunicorn
    app.run(host='0.0.0.0', port=5000)
