# Python Image Overlay Script

A simple Python script to overlay one image onto a series of background images with adjusted opacity and size. This project was created to automate content creation for social media platforms like TikTok.

## Features

-   Overlays a primary image onto multiple backgrounds.
-   Reduces the primary image's opacity (e.g., to 90%).
-   Resizes the primary image to a specific percentage of the background's dimensions (e.g., 75%).
-   Processes all images from an `img` folder and saves results to an `output` folder.

## How to Use

1.  **Prerequisites:**
    * Python 3.x must be installed.

2.  **Setup:**
    * Clone this repository.
    * (Optional but recommended) Create and activate a virtual environment:
        ```bash
        python -m venv .venv
        source .venv/bin/activate  # On Windows: .venv\Scripts\activate
        ```
    * Install the required libraries:
        ```bash
        pip install -r requirements.txt
        ```

3.  **Running the script:**
    * Place your main image (e.g., `1.png`) and all background images into the `img` folder.
    * Run the script from the command line:
        ```bash
        python script.py
        ```
    * The processed images will appear in the `output` folder.
