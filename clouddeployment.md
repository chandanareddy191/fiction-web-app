# AWS Deployment Guide for Book Management API

## Prerequisites
- An AWS Account with appropriate permissions
- AWS CLI installed and configured
- Elastic Beanstalk CLI (EB CLI) installed (`pip install awsebcli`)
- Book Management App code stored in a GitHub repository

---
## Step 1: Prepare Your Application
Ensure your application contains the following files:
- `requirements.txt` (list of dependencies)
- `Dockerfile` (for containerization)
- `docker-compose.yml` (for local testing)

### Configure Environment Variables
Modify your `app/__init__.py` to load environment variables:
```python
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'dev-jwt-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
```

---
## Step 2: Create an Elastic Beanstalk Application

### Install EB CLI (if not already installed)
```bash
pip install awsebcli
```

### Navigate to your project directory
```bash
cd book-management-app
```

### Initialize Elastic Beanstalk
```bash
eb init
```
- Select your AWS region (e.g., `us-east-1`)
- Choose `Docker` as the platform
- Opt out of CodeCommit if using GitHub (`No`)
- Set up SSH for instance access if required

---
## Step 3: Create an Environment and Deploy

### Create and deploy to a new environment
```bash
eb create book-api-env
```
- This process will take a few minutes as AWS sets up the necessary resources.

### Monitor deployment
```bash
eb events -f
```

### Open the deployed application
```bash
eb open
```

---
## Step 4: Configure Environment Variables

1. Go to **AWS Elastic Beanstalk Console**
2. Select your **application** and **environment**
3. Navigate to **Configuration → Software**
4. Add the following environment variables:
   - `SECRET_KEY`: **your-secure-secret-key**
   - `JWT_SECRET_KEY`: **your-secure-jwt-key**
   - `FLASK_ENV`: **production**
5. Apply the changes

---
## Step 5: Set Up a Database (Optional)
For production use, set up **Amazon RDS** instead of SQLite:

1. In Elastic Beanstalk, go to **Configuration → Database**
2. Create a new database:
   - **Engine**: PostgreSQL
   - **Instance class**: `db.t2.micro` (or as needed)
   - **Storage**: 5GB minimum
   - **Username** and **password**: Set secure credentials
3. Apply changes (this will take several minutes)
4. Update your `DATABASE_URL` environment variable accordingly

---
## Step 6: Test Your Deployed API

Once deployed, your API will be available at:
```bash
http://book-api-env.eba-xyz123.us-east-1.elasticbeanstalk.com
```

### Register a new user
```bash
curl -X POST http://your-eb-url.elasticbeanstalk.com/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "your-password"}'
```

### Login to obtain JWT token
```bash
curl -X POST http://your-eb-url.elasticbeanstalk.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "your-password"}'
```

### Use JWT token to access books
```bash
curl -X GET http://your-eb-url.elasticbeanstalk.com/api/books \
  -H "Authorization: Bearer YOUR_TOKEN"
```



