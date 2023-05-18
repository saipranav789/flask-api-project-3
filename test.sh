#!/bin/bash


# Below are some sample test cases for POST. All test cases that we used are included in the readme.md file

# Test Case 1
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg":"Hello1"}' http://127.0.0.1:5000/post)
expected='{"id": 27,"key": "9abf68bfa5d58959b021d2b47c36b5a9","msg": "Hello1","timestamp": "*","user": "default","user_id": null}'
if [[ $response == $expected ]]; then
  echo "Test Case 1 passed"
else
  echo "Test Case 1 failed. Expected: $expected, Actual: $response"
fi

# Test Case 2
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg":"Hello2"}' http://127.0.0.1:5000/post)
expected='{"id": 27,"key": "9abf68bfa5d58959b021d2b47c36b5a9","msg": "Hello1","timestamp": "*","user": "default","user_id": null}'
if [[ $response == $expected ]]; then
  echo "Test Case 2 failed. Expected different output from Test Case 1. Actual: $response"
else
  echo "Test Case 2 passed"
fi

# Test Case 3
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg":"Hello2"}' http://127.0.0.1:5000/post)
expected='{"id": 28,"key": "*","msg": "Hello2","timestamp": "*","user": "default","user_id": null}'
if [[ $response == $expected ]]; then
  echo "Test Case 3 passed"
else
  echo "Test Case 3 failed. Expected: $expected, Actual: $response"
fi

# Test Case 4
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg":""}' http://127.0.0.1:5000/post)
expected='{"err": "Message field is missing or not a string"}'
if [[ $response == $expected ]]; then
  echo "Test Case 4 passed"
else
  echo "Test Case 4 failed. Expected: $expected, Actual: $response"
fi

# Test Case 5
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{}' http://127.0.0.1:5000/post)
expected='{"err": "Message field is missing or not a string"}'
if [[ $response == $expected ]]; then
  echo "Test Case 5 passed"
else
  echo "Test Case 5 failed. Expected: $expected, Actual: $response"
fi

# Test Case 6
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"msg":"Helloo"}' http://127.0.0.1:5000/post)
expected='{"id": 29,"key": "*","msg": "Helloo","timestamp": "*","user": "default","user_id": null}'
if [[ $response == $expected ]]; then
  echo "Test Case 6 passed"
else
  echo "Test Case 6 failed. Expected: $expected, Actual: $response"
fi