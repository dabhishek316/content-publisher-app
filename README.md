# content-publisher-app

A modular Streamlit-based tool enabling streamlined upload and publication of media content (photos, videos, stories) across multiple platforms. Features secure authentication management, media preview, and extensible API integration to support diverse publishing needs.

## Features
- Upload Instagram stories and videos via a simple web UI
- View and edit story captions (up to 2200 characters)
- Securely manage API credentials using environment variables
- View Instagram profile stats (followers, media count) in the sidebar
- Built with Streamlit for rapid prototyping and deployment

## Getting Started

### Prerequisites
- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (for fast dependency management)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/dabhishek316/content-publisher-app.git
   cd content-publisher-app
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   uv venv
   .venv\Scripts\activate  # On Windows
   uv pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with the following variables:
   ```env
   instagram_profile_name=YOUR_INSTAGRAM_USERNAME
   long_access_token=YOUR_LONG_LIVED_ACCESS_TOKEN
   instagram_business_account=YOUR_INSTAGRAM_BUSINESS_ACCOUNT_ID
   ```

### Running the App
```sh
streamlit run app.py
```

The app will be available at http://localhost:8501

## Project Structure
- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (not committed to git)
- `.gitignore` - Standard Python, Streamlit, and VS Code ignores

## License
See [LICENSE](LICENSE)
