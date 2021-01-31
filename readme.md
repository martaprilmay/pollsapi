# Polls API

REST API for creating polls and collecting answers

## Installation

```bash
docker build -t pollsapi .
docker run --name pollsAPI -p 8000:8000 -d pollsapi
```

## API Documentation
Auto-generated version at http://localhost:8000/swagger.json

## Admin
### Authentication
### Retrieve All Polls
### Create Poll
### Update Poll
### Delete Poll
### Create Question
### Update Question
### Delete Question
### Create Question
### Update Question
### Delete Question

## User
### Authentication
Authentication by a unique auth_id:int -- no registration needed.
To get an id:
### Retrieve All Polls
### Retrieve A Single Poll Details
### Retrieve All Questions For A Specified Poll
### Retrieve A Singe Question Details
### Retrieve All Choices For A Specified Question
### Answer A Question
### Retrieve All Answered Polls with Answers


