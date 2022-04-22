#!/bin/bash
# 8. cURL a JSON file
curl -s -d @$2 -H "Content-Type: application/json" -X POST $1
