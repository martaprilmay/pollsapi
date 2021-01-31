# Polls API

RESTful API for creating polls, conducting and collecting answers

## Installation

```bash
docker build -t pollsapi .
docker run --name pollsAPI -p 8000:8000 -d pollsapi
```

## API Documentation
Auto-generated version at http://localhost:8000/swagger.json

## Admin
Admin can retrieve, create, update and delete polls, questions and choices.
Options available to everyone (not just to the admin user) are listed in the User section (below).
### Authentication
Authentication by Token. To Get a Token:
* HTTP Method – POST
* Endpoint – https://localhost:8000/api/v1/token-auth/
* Body
    * username: admin_username
    * password: admin_password
```bash
curl --request POST 'http://localhost:8000/api/v1/token-auth/' \
--form 'username=%admin_username' \
--form 'password=%admin_password'
```
### Retrieve All Polls
* HTTP Method – GET
* Endpoint – https://localhost:8000/api/v1/polls/all/
* Header – Authorization: Token admin_token
```bash
curl --request GET 'https://localhost:8000/api/v1/polls/all/' \
--header 'Authorization: Token %admin_token'
```
### Create Poll
* HTTP Method – POST
* Endpoint – https://localhost:8000/api/v1/polls/create/
* Header – Authorization: Token admin_token
* Body
    * poll_name: poll_name
    * end_date: YYYY-MM-DD
    * description: description
 ```bash
curl --request POST 'https://localhost:8000/api/v1/polls/create/' \
--header 'Authorization: Token %admin_token' \
--form 'poll_name=%poll_name' \
--form 'end_date=%YYYY-MM-DD' \
--form 'description=%description'
```
### Update Poll
* HTTP Method – PUT or PATCH
* Endpoint – https://localhost:8000/api/v1/polls/[id]/update/
* Param – id (poll id)
* Header – Authorization: Token admin_token
* Body
    * poll_name: poll_name
    * end_date: YYYY-MM-DD
    * description: description
 ```bash
curl --request PUT 'https://localhost:8000/api/v1/polls/[id]/update/' \
--header 'Authorization: Token %admin_token' \
--form 'poll_name=%poll_name' \
--form 'end_date=%YYYY-MM-DD' \
--form 'description=%description'
```
### Delete Poll
* HTTP Method – DELETE
* Endpoint – https://localhost:8000/api/v1/polls/[id]/update/
* Param – id (poll id)
* Header – Authorization: Token admin_token
 ```bash
curl --request DELETE 'https://localhost:8000/api/v1/polls/[id]/update' \
--header 'Authorization: Token %admin_token'
```
### Create Question
Question types are: 1 – text, 2 – select a single option, 3 – select multiple.
* HTTP Method – POST
* Endpoint – https://localhost:8000/api/v1/polls/[id]/questions/create/
* Param - id (poll id)
* Header – Authorization: Token admin_token
* Body
    * question_text: question_text
    * question_type: question_type
```bash
curl --request POST 'https://localhost:8000/api/v1/polls/[id]/questions/create' \
--header 'Authorization: Token %admin_token' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type'
```
### Update Question
* HTTP Method – PUT or PATCH
* Endpoint – https://localhost:8000/api/v1/questions/[id]/update/
* Param – id (question id)
* Header – Authorization: Token admin_token
* Body
    * poll: poll_id
    * question_text: question_text
    * question_type: question_type
```bash
curl --request PUT 'https://localhost:8000/api/v1/questions/[id]/update/' \
--header 'Authorization: Token %admin_token' \
--form 'poll=%poll_id' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type'
```
### Delete Question
* Endpoint – https://localhost:8000/api/v1/question/[id]/update/
* Param – id (poll id), q_id (question id)
* Header – Authorization: Token admin_token
```bash
curl --request DELETE 'https://localhost:8000/api/v1/questions/[id]/update' \
--header 'Authorization: Token %admin_token'
```
### Create Choice
* HTTP Method – POST
* Endpoint – https://localhost:8000/api/v1/polls/[id]/questions/[q_id]/choices/create/
* Param – id (poll id), q_id (question id)
* Header – Authorization: Token admin_token
* Body
    * choice_text: choice_text
```bash
curl --request POST 'https://localhost:8000/api/v1/polls/[id]/questions/[q_id]/create/' \
--header 'Authorization: Token %admin_token' \
--form 'choice_text=%choice_text'
```
### Update Choice
* HTTP Method – PUT or PATCH
* Endpoint – https://localhost:8000/api/v1/choices/[id]/update/
* Param – id (choice id)
* Header – Authorization: Token admin_token
* Body
    * question: question_id
    * choice_text: choice_text
```bash
curl --request PUT 'https://localhost:8000/api/v1/choices/[id]/update/' \
--header 'Authorization: Token %admin_token' \
--form 'question=%question_id' \
--form 'choice_text=%choice_text'
```
### Delete Choice
* HTTP Method – DELETE
* Endpoint – https://localhost:8000/api/v1/choices/[id]/update/
* Param – id (poll id), q_id (question id)
* Header – Authorization: Token admin_token
```bash
curl --request DELETE 'https://localhost:8000/api/v1/choices/[id]/update/' \
--header 'Authorization: Token %admin_token'
```
## User
User can retrieve a list a active polls, detailed information on polls and questions without authentication.
To answer a question and to retrieve a list of all answers an auth_id is required.
### Authentication
Authentication by a unique auth_id:int – no registration needed.
To get an id:
* HTTP Method – POST
```bash
curl --request DELETE 'https://localhost:8000/api/v1/create-id/'
```
### Retrieve All Active Polls
* HTTP Method – GET
* Endpoint – https://localhost:8000/api/v1/polls/
```bash
curl --request GET 'https://localhost:8000/api/v1/polls/'
```
### Retrieve A Single Poll Details
* HTTP Method – GET
* Endpoint – https://localhost:8000/api/v1/polls/[id]/
* Param – id (poll id)
```bash
curl --request GET 'https://localhost:8000/api/v1/polls/[id]/'
```
### Retrieve All Questions For A Specified Poll
* HTTP Method – GET
* Endpoint – https://localhost:8000/api/v1/polls/[id]/questions/
* Param – id (poll id)
```bash
curl --request GET 'https://localhost:8000/api/v1/polls/[id]/questions/'
```
### Retrieve A Singe Question Details
* HTTP Method – GET
* Endpoint – https://localhost:8000/api/v1/polls/[id]/questions/[q_id]/
* Param – id (poll id), q_id (question id)
```bash
curl --request GET 'https://localhost:8000/api/v1/polls/[id]/questions/[q_id]/'
```
### Retrieve All Choices For A Specified Question
* HTTP Method – GET
* Endpoint – https://localhost:8000/api/v1/polls/[id]/questions/[q_id]/choices/
* Param – id (poll id), q_id (question id)
```bash
curl --request GET 'https://localhost:8000/api/v1/polls/[id]/questions/[q_id]/choices/'
```
### Answer A Text Question
NB! An empty list should be submitted for selected_options (body) 
* HTTP Method – POST
* Endpoint – https://localhost:8000/api/v1/polls/[id]/questions/[q_id]/answer/
* Param – id (poll id), q_id (question id)
* Header – auth-id: auth_id
* Body
    * answer_text: answer_text
    * selected_choices: []
```bash
curl --request POST 'https://localhost:8000/api/v1/polls/[id]/questions/[q_id]/answer/' \
--header 'auth-id: %auth-id' \
--form 'answer_text=%answer_text' \
--form 'selected_choices=[]'
```
### Answer A Single Option Question
NB! An empty list should be submitted for selected_options (body) 
* HTTP Method – POST
* Endpoint – https://localhost:8000/api/v1/polls/[id]/questions/[q_id]/answer/
* Param – id (poll id), q_id (question id)
* Header – auth-id: auth_id
* Body
    * selected_option: option_id
    * selected_options: []
```bash
curl --request POST 'https://localhost:8000/api/polls/[id]/questions/[q_id]/answer/' \
--header 'auth-id: %auth-id' \
--form 'selected_option=%option_id' \
--form 'selected_choices=[]'
```
### Answer A Multiple Choice Question
* HTTP Method – POST
* Endpoint – https://localhost:8000/api/v1/polls/[id]/questions/[q_id]/answer/
* Param – id (poll id), q_id (question id)
* Header – auth-id: auth_id
* Body
    * selected_options: a list of option_ids
```bash
curl --request POST 'https://localhost:8000/api/v1/polls/[id]/questions/[q_id]/answer/' \
--header 'auth-id: %auth-id' \
--form 'selected_choices=%a_list_of_option_ids'
```
### Retrieve All Answered Polls with Answers
* HTTP Method – GET
* Endpoint – https://localhost:8000/api/v1/polls/my-answers/
* Header – auth-id: auth_id
```bash
curl --request GET 'https://localhost:8000/api/v1/polls/my-answers/' \
--header 'auth-id: %auth-id'
```


