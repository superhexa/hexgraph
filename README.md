![Screenshot from 2024-09-09 14-34-47](https://github.com/user-attachments/assets/43c7a319-846d-4c2e-a320-e3fec6b014ed)


# Hexgraph

Hexgraph is a simple web application built with Flask and Quill. It allows users to create and view posts with rich text formatting. This application uses a lightweight database client to store posts and provides a clean, modern user interface for interacting with the posts.

## Features

- **Create Posts:** Users can create new posts with a title and rich text content using the Quill editor.
- **View Posts:** Users can view individual posts with their title and formatted content.
- **Responsive Design:** The application is designed to be user-friendly and responsive.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework for Python.
- **Quill:** A modern WYSIWYG editor built for the web.
- **FlashSQL:** A lightweight database for storing post data.
- **HTML/CSS:** For building the web pages and styling them.

## Getting Started

To get Hexgraph up and running on your local machine, follow these steps:

### Prerequisites

- **Python**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).
- **pip**: Python's package installer.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/superhexa/hexgraph.git
   cd hexgraph
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**

   ```bash
   python app.py
   ```

   The application will start and be available at `http://127.0.0.1:1020`.

### Run via Docker

If you prefer to run Hexgraph via Docker, follow these steps:

1. **Build the Docker Image**

   ```bash
   docker build -t hexgraph .
   ```

2. **Run the Docker Container**

   ```bash
   docker run -p 1020:1020 hexgraph
   ```

   The application will be available at `http://127.0.0.1:1020` in your browser.

### Usage

1. **Access the Application**

   Open a web browser and navigate to `http://127.0.0.1:1020` to view the application.

2. **Create a Post**

   - Enter a title for the post in the "Post Title" field.
   - Use the Quill editor to write the content of the post.
   - Click "Create Post" to submit the form. You will be redirected to the post's view page.

3. **View a Post**

   - After creating a post, you'll be automatically redirected to the post's page.
   - You can also view posts by navigating to `http://127.0.0.1:1020/post/<post_id>`, replacing `<post_id>` with the actual ID of the post.

## Live preview

- https://graph.pvfd.online

## Contributing

Feel free to submit issues, fork the repository, and create pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

