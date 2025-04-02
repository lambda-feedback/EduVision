# eduVision
Handle all API calls to external services.

For now, we have examples and API structure prepare for the EduVision Proof of Concept Application.

## Inputs

- `response` (Any): The answers provided by the student. It can be a ID of the instance, a list of IDs, a list of dictionaries, etc. to handle the response from the API.
- `answer` (Any): The correct answers to compare against the API response.
- `params` (Dict): Important endpoint information to make the API call to EduVision API Server. Storing ````endpoint``` information.

```
{server}/{endpoint}{response}
```

## Outputs
Return result value is a boolean.

```python
   {
    "is_correct": true
   }
```

## Examples
For now, we have examples for the EduVision Proof of Concept Application.

### EduVision Application

There is 2 endpoints to call the API. The first one is to get the list of all the students and the second one is to get the list of all the courses.

#### Resistors
Check how many resistors is recognized with its resistance value.
***Answer value must be dictionary.***

```python
{
  "headers": {
    "command": "eval"
  },
  "body": {
    "response": "999999",
    "answer": [],
    "params": {
      "api_endpoint": "endpoint/"
    }
  }
}
```

```python
{
  "headers": {
    "command": "eval"
  },
  "body": {
    "response": "999999",
    "answer": [
        {
            "resistance": 1000.0,
        },
        {
            "resistance": 1000.0,
        },
    ],
    "params": {
      "api_endpoint": "endpoint/"
    }
  }
}
```
#### Resistance
Check global resistance of the circuit
***Answer value must be float.***

```python
{
  "headers": {
    "command": "eval"
  },
  "body": {
    "response": "999999",
    "answer": 1000.0,
    "params": {
      "api_endpoint": "endpoint/"
    }
  }
}
```