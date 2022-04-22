#!/bin/bash
# status 100
curl -s -o /dev/null -I -w "%{http_code}" $1
