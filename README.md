# Messaging and Like Service

## Overview

This project consists of a three services: `messaging service` and a `like service` and `user service` built using FastAPI. The messaging service allows users to create and read messages, while the like service enables users to like messages and count the number of likes for each message while the user service register the user and chaeck if the user is exist . 

Each servive is runnign on differernt port , and they talk to each other using RestAPI 
### Services

- **Message Service**: `http://message_service:8001`
- **Like Service**: `http://like_service:8002`
- **User Service**: `http://user_service:8000/user_service/users`

## API Endpoints
### User Service
 - **POST** `/users/`
 - **Request Body**:
    - `username`

### Message Service

#### Create Message

- **POST** `/messages/`
- **Request Body**:
    - `content`: The content of the message .
    - `user_id`: The ID of the user creating the message .

#### Read Messages

- **GET** `/messages/`
- **Query Parameters**:
    - `skip`: The number of messages to skip .
    - `limit`: The number of messages to return .

#### Read Message by ID

- **GET** `/messages/{message_id}`
- **Path Parameters**:
    - `message_id`: The ID of the message .

### Like Service

#### Like Message

- **POST** `/like_service/messages/{message_id}/like`
- **Path Parameters**:
    - `message_id`: The ID of the message to like .
- **Request Body**:
    - `user_id`: The ID of the user liking the message .

#### Get Like Count for a Message

- **GET** `/like_service/messages/{message_id}/likes/count`
- **Path Parameters**:
    - `message_id`: The ID of the message to get like count for .

## Usage

1. **Start Services**:  all services should be  running. using Docker Compose .
1. **create a user** : Send a POST request to `/users/` with username .
2. **Create a Message**:
    - Send a POST request to `/messages/` with the message content and user ID.

3. **Read Messages**:
    - Send a GET request to `/messages/` to retrieve a list of messages.
    - Optionally, use `skip` and `limit` to paginate results.

4. **Like a Message**:
    - Send a POST request to `/like_service/messages/{message_id}/like` with the user ID.


## Running the Application

To run the application:

```bash
docker-compose up --build
```
