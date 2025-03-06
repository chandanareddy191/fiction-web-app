
# Book Management API

A containerized REST API for managing a book collection with authentication and rate limiting.

A book collection is just to test the functonality of this and took it for reference purpose only not defining this to only for book collection.

## Project Overview

This project was created to fulfill the requirements of building a containerized web app with CRUD operations and API authentication. I chose to implement a Book Management system because it presented a good balance of complexity and practical utility.

The core features include:
- User registration and JWT-based authentication
- Create, read, update, and delete operations for books
- Rate limiting to prevent abuse
- Containerization with Docker
- Cloud deployment capability

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy with SQLite (can be easily switched to PostgreSQL)
- **Authentication**: JWT using flask-jwt-extended
- **Rate Limiting**: Flask-Limiter
- **API Documentation**: Included in this README
- **Container**: Docker
- **Cloud Platform**: AWS Elastic Beanstalk

## sample output

![image](https://github.com/user-attachments/assets/5eba0f54-ca9e-490b-ad04-a2c684255741)

![image](https://github.com/user-attachments/assets/78437262-0978-4dbd-8dbe-72c9767465af)


## Local Setup

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Docker (optional for containerization)

### Installation

Clone the repository and set up the environment:

```bash
# Clone the repository
git clone # clone the current repo as it is 
cd book-management-app

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py

Note : to setup in cloud environment please look into the clouddeployment.md file provided for the steps 


