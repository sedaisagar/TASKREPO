###  High-Level Design
```
Proposed Architecture:

This system is totally done using Django, Django Socio gRPC for creating GRPC
The system follows a microservices architecture with Django Socio gRPC as the RPC layer and Celery for task processing.

gRPC is used for efficient communication.

Mysql is the primary database for storing task metadata.

Redis serves as the message broker for Celery.

Docker Compose is used for container orchestration.

Scaling & Avoiding Duplicate Processing:

Celery workers scale horizontally by increasing worker instances.

As per the requirements mentioned, I choosed email sending task. I've checked if email domain has any mx record, if found then I've sent email to particular address with subject and body and marked task as completed.

While executing this process, i've locked particular task marked it processing to denote its processing state and eventually marked completed or failed after email send function execution.

```

### Database Changes:

```
Kept As it is
```

### Microservice Workflow:
```
Task Processing System (task_processing_system) is a django app which includes tasks as app where RPC services are written for creation and listing of tasks.

When a task is created , new celery task is added

Then Celery worker executes the task processing step
```

### Failure Handling Strategy:

```
Since Redis acts as the message broker, tasks remain in the queue even if the API server crashes.
If the Celery workers restart, they reconnect to Redis and resume picking up pending tasks.
```


### How to run project

```
SET EMAIL_USER and EMAIL_PASS in docker-compose.yml environment

![alt text](https://ibb.co/DD194zgJ)
```

### RUN
```
docker-compose up --build -d
```

### Lets suppose an arbitary microservice creates task for sending email by calling rpc create method

### For Create Method following is payload sample

```
{
    "data": {
        "email": "sohome9366@bmixr.com",
        "subject": "ipsum anim tempor dolor",
        "body": "aliquip Ut"
    }
}
```


### For List Method following is the sample for filtering
#### Available statuses ```pending``` ```processing``` ```completed``` ```failed``` 

```
{
    "_filters": {
        "fields": {
            "status": {
                "string_value": "pending"
            }
        }
    }
}
```