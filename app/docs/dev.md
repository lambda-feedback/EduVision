# eduVision
Handle all API calls to external services.

For now, we have examples and API structure prepare for the EduVision Proof of Concept Application.

## Inputs

- `response` (Any): The answers provided by the student. It can be a ID of the instance, a list of IDs, a list of dictionaries, etc. to handle the response from the API.
- `answer` (Any): The correct answers to compare against the API response.
- `params` (Dict): Important server and endpoint information to make the API call.
Structure of API connection. Storing ```server``` and  ```endpoint``` information.

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
    "response": "160929",
    "answer": [],
    "params": {
      "server": "http://20.117.225.136:8000",
      "api_endpoint": "resistors/"
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
    "response": "160929",
    "answer": [
        {
            "resistance": 1000.0,
        },
        {
            "resistance": 1000.0,
        },
    ],
    "params": {
      "server": "http://20.117.225.136:8000",
      "api_endpoint": "resistors/"
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
    "response": "160929",
    "answer": 1000.0,
    "params": {
      "server": "http://20.117.225.136:8000",
      "api_endpoint": "resistance/"
    }
  }
}
```