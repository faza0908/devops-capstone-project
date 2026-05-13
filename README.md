# Devops Capstone Project

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://shields.io/)
[![Build Status](https://github.com/YOUR_USERNAME/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/YOUR_USERNAME/devops-capstone-project/actions)

## Overview

This project is a RESTful microservice for managing bank accounts, built with Flask and deployed on Kubernetes. It follows Agile development practices with CI/CD pipelines using GitHub Actions and Tekton.

## Features

- Create, Read, Update, Delete (CRUD) operations for bank accounts
- RESTful API endpoints
- Security headers with Talisman
- CORS policies
- Containerized with Docker
- Deployed on Kubernetes
- CI pipeline with GitHub Actions
- CD pipeline with Tekton

## Project Structure

```
devops-capstone-project/
├── service/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── common/
│       ├── error_handlers.py
│       ├── log_handlers.py
│       └── status.py
├── tests/
│   ├── __init__.py
│   └── test_routes.py
├── .github/
│   └── workflows/
│       └── ci-build.yaml
├── .tekton/
│   ├── pipeline.yaml
│   └── tasks.yaml
├── deploy/
│   └── k8s/
│       ├── deployment.yaml
│       └── service.yaml
├── Dockerfile
├── setup.cfg
├── requirements.txt
└── README.md
```

## Setup and Installation

### Prerequisites

- Python 3.9+
- Docker
- Kubernetes (kubectl)
- Tekton Pipelines

### Local Development

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/devops-capstone-project.git
cd devops-capstone-project

# Install dependencies
pip install -r requirements.txt

# Run the service
flask run

# Run tests
nosetests
```

### Docker

```bash
# Build the Docker image
docker build -t accounts-service:latest .

# Run the container
docker run -p 8080:8080 accounts-service:latest
```

### Kubernetes

```bash
# Apply Kubernetes manifests
kubectl apply -f deploy/k8s/

# Check deployment status
kubectl get all -l app=accounts
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/accounts` | List all accounts |
| POST | `/accounts` | Create an account |
| GET | `/accounts/{id}` | Read an account |
| PUT | `/accounts/{id}` | Update an account |
| DELETE | `/accounts/{id}` | Delete an account |

## License

Copyright 2022 John Rofrano. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0
