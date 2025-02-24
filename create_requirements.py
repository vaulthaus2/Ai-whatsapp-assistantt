import os

# Path to the backend directory
backend_dir = "D:/New folder/AI-Whatsapp-Assistantt/backend"

# List of dependencies to include in the requirements.txt
dependencies = [
    "fastapi==0.95.0",
    "uvicorn==0.22.0",
    "pyjwt==2.6.0",
    "pydantic==1.11.1",
    "requests==2.28.2",
    "sqlalchemy==2.0.10",
    "alembic==1.9.3",
    "pytest==7.2.2",
    "httpx==0.24.0",
    "python-dotenv==0.21.0"
]

# Create the 'backend' directory if it doesn't exist
if not os.path.exists(backend_dir):
    os.makedirs(backend_dir)

# Path for the requirements.txt file
requirements_file_path = os.path.join(backend_dir, "requirements.txt")

# Create and write dependencies to the file
with open(requirements_file_path, "w") as f:
    for dep in dependencies:
        f.write(dep + "\n")

print(f"requirements.txt has been created at: {requirements_file_path}")
 
