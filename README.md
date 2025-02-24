# ai-whatsapp-assistant

## Repository Structure
```
ai-whatsapp-assistant/
│── backend/                 # Backend services
│   ├── app/                 
│   │   ├── models/          # Database models (User, Tasks, Ads, etc.)
│   │   ├── routes/          # API endpoints
│   │   ├── services/        # Business logic (AI processing, Ad optimization)
│   │   ├── utils/           # Utility functions
│   │   ├── main.py          # Main FastAPI app entry point
│   ├── tests/               # Unit & integration tests
│   ├── config.py            # Configurations (API keys, env variables)
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile           # Containerization for deployment
│
│── ai-engine/               # AI-related processing
│   ├── chatbot.py           # AI conversation logic (GPT-4 integration)
│   ├── nlp_model.py         # Custom AI models for task execution
│   ├── training_data/       # Fine-tuning datasets for responses
│
│── integrations/            # External API integrations
│   ├── whatsapp_api.py      # WhatsApp API (Twilio, Meta)
│   ├── shopify_api.py       # Shopify API connection
│   ├── google_ads_api.py    # Google Ads automation
│   ├── facebook_ads_api.py  # Meta Ads automation
│
│── database/                # Database setup & migrations
│   ├── schema.sql           # Database schema (PostgreSQL/MongoDB)
│   ├── migrations/          # Database versioning
│
│── docs/                    # Documentation
│   ├── API.md               # API endpoints & usage
│   ├── ARCHITECTURE.md      # System architecture overview
│   ├── SETUP.md             # Setup instructions
│
│── .github/workflows/       # GitHub Actions for CI/CD
│   ├── deploy.yml           # Automated deployment workflow
│
│── .env                     # Environment variables (API keys, credentials)
│── .gitignore               # Ignore unnecessary files
│── README.md                # Project overview
```

## Installation & Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/ai-whatsapp-assistant.git
cd ai-whatsapp-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Backend
```bash
uvicorn backend.app.main:app --reload
```

## Docker Support
```bash
# Build the Docker image
docker build -t ai-whatsapp-assistant .

# Run the container
docker run -p 8000:8000 ai-whatsapp-assistant
```

## GitHub Actions Deployment
A GitHub Actions workflow (`.github/workflows/deploy.yml`) is included for automated deployment. It will:
1. Run tests
2. Build the Docker image
3. Deploy to a cloud provider (e.g., AWS, DigitalOcean, or Render)

### Example `deploy.yml`:
```yaml
name: Deploy Backend

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

    - name: Run tests
      run: pytest

    - name: Build and push Docker image
      run: |
        echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
        docker build -t yourdockerhub/ai-whatsapp-assistant:latest .
        docker push yourdockerhub/ai-whatsapp-assistant:latest

    - name: Deploy to server
      run: |
        ssh -o StrictHostKeyChecking=no user@yourserver "docker pull yourdockerhub/ai-whatsapp-assistant:latest && docker-compose up -d"
```

### Setting Up Secrets
In your GitHub repository settings, add:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `SERVER_SSH_KEY` (if deploying to a remote server)

This ensures your AI WhatsApp assistant is deployed automatically on every push to `main`.
 
