# Nth Prime Finder

## Summary

This is a minimal, full-stack web application that allows users to find the nth prime number. The user enters an integer 'n' into a web interface, and the application calculates and displays the corresponding prime number.

The application consists of a Python Flask backend that handles the prime number calculation and a simple HTML/CSS/JS frontend for user interaction.

## Setup

Follow these instructions to get the application running on your local machine.

### Prerequisites

- Python 3.6+
- `pip` (Python package installer)

### Installation & Running

1.  **Save the files:**
    Save `main.py` and `index.html` into the same directory.

2.  **Install dependencies:**
    This application requires the Flask web framework. Install it using pip:
    ```bash
    pip install Flask
    ```

3.  **Run the web server:**
    Navigate to the directory containing the files and run the main Python script:
    ```bash
    python main.py
    ```
    You should see output indicating that the server is running, typically on `http://127.0.0.1:5000`.

## Usage

1.  Once the server is running, open your web browser and go to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

2.  You will see the "Nth Prime Number Finder" interface.

3.  Enter a positive integer (e.g., 1, 10, 1000) into the input field.

4.  Click the "Find Prime" button.

5.  The application will calculate the result and display it below the form. If you enter invalid input, an error message will be shown.

## Code Explanation

### `main.py`

This file contains the backend logic using the Flask framework.

-   **`is_prime(num)`**: A helper function that checks if a given number is prime using an optimized trial division method.
-   **`find_nth_prime(n)`**: The core logic function that iterates through numbers, using `is_prime` to count primes until it finds the nth one.
-   **`@app.route('/')`**: This route serves the `index.html` file, which is the main user interface.
-   **`@app.route('/api/get_prime')`**: This is the API endpoint that the frontend calls. It takes an integer `n` as a query parameter, validates it, calls `find_nth_prime`, and returns the result as a JSON object. It includes error handling for invalid input or server-side issues.

### `index.html`

This file provides the frontend user interface and logic.

-   **HTML Structure**: A simple form with a number input field and a submit button. There is also a `div` with the id `result` to display the output.
-   **CSS Styling**: Inline CSS is used to provide a clean, modern, and user-friendly layout.
-   **JavaScript Logic**:
    -   An event listener is attached to the form's `submit` event.
    -   It prevents the default page reload behavior.
    -   It uses the `fetch` API to make an asynchronous GET request to the `/api/get_prime` backend endpoint.
    -   It provides user feedback by disabling the button and showing a "Calculating..." message during the request.
    -   It handles the JSON response, displaying either the calculated prime number or an error message in the `result` div.

## License

This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
