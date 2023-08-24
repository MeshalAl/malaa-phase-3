# Malaa Phase 3 Project

Phase 3 of Malaa's technical assesment project.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Major Frameworks and Libraries](#major-frameworks-and-libraries)
- [Installation](#installation)
- [Configuration](#configuration)
- [In Progress](#in-progress)

## Getting Started

Clone the repository to your local machine to get started with the project.


```bash
git clone https://github.com/MeshalAl/malaa-phase-3.git
```
## Prerequisites

- Python 3.11.4 or higher
- Docker
- RapidAPI Account (for market data)

## Major Frameworks and Libraries

- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **Uvicorn**: An ASGI server that serves as the interface between FastAPI and the outside world.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Requests**: A popular library for making HTTP requests in Python.
- **Celery**: A distributed task queue that allows for processing tasks asynchronously.
- **Celery Beat**: A scheduler for Celery, allowing for periodic task execution.
- **AMQPStorm**: A library for interacting with AMQP brokers, such as RabbitMQ.
- **Pika**: A pure-Python library for interacting with RabbitMQ.
- **Tenacity**: A library for retrying failed operations.
- **Other Dependencies**: Additional libraries and tools may be used, and their details can be found in the \`requirements.txt\` file.

## Installation

1. Navigate to the project directory.
2. Build the Docker containers:

```bash
docker-compose -f dev_setup/docker-compose.yml build
```

3. Start the containers:

```bash
docker-compose -f dev_setup/docker-compose.yml up
```

## Configuration

### RapidAPI-Key Configuration

To access market data, you need to add your RapidAPI-Key. Follow these steps:

1. Open the \`docker-compose.yml\` file under the \`dev_setup\` directory.
2. Locate the environment section and add your RapidAPI-Key:

```yaml
   environment:
     - RAPID_API_KEY=your-rapidapi-key-here
```

3. Save the file and restart the Docker containers.

## In Progress

- **Running Tests**: The testing framework and test cases are currently being developed and will be available in future updates.

---
