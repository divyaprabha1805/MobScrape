# MobScrape

MobScrape is a web scraping tool that utilizes Selenium and BeautifulSoup to extract product details from Amazon India. This project is designed to navigate through multiple pages and operates in headless mode for faster and more resource-efficient execution.

## Features

- Extracts product details including:
  - Title
  - Price
  - Ratings
- Navigates through multiple pages of products
- Runs in headless mode for improved performance

## Technologies Used

- **Programming Language:** Python
- **Libraries:**
  - Selenium (for web automation)
  - BeautifulSoup (for parsing HTML)

## Installation

To set up the project locally, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/divyaprabha1805/MobScrape.git

    Navigate to the project directory:
    bash

cd MobScrape

Install the required dependencies:
bash

    pip install -r requirements.txt

Usage

To run the scraper:

    Ensure you have the necessary web driver for Selenium (e.g., ChromeDriver for Google Chrome).

    Execute the scraper:
    bash

    python scraper.py

    The extracted product details will be displayed in the console or saved to a specified file.

Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

    Fork the repository.
    Create a new branch:
    bash

git checkout -b feature/YourFeature

Make your changes and commit them:
bash

git commit -m "Add your message here"

Push to the branch:
bash

    git push origin feature/YourFeature

    Open a pull request.

