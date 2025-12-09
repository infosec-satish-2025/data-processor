# Data Processor

Python service for processing and analyzing data from various sources.

## Features

- Batch data processing
- Real-time data streaming
- Data validation and cleaning
- Export to multiple formats
- Scheduled jobs with Celery

## Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```
DATABASE_URL=postgresql://user:password@localhost/dbname
REDIS_URL=redis://localhost:6379
DATA_SOURCE_API=https://api.example.com
```

## Usage

```bash
# Run data processor
python processor.py

# Run with specific config
python processor.py --config production

# Run tests
pytest tests/
```

## Tech Stack

- Python 3.10+
- Pandas for data manipulation
- SQLAlchemy for database
- Celery for task queue
- Redis for caching
