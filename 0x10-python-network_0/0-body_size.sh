#!/bin/bash
# 0. cURL body size
curl -sI $1 '/Content-Length/{print $2}'
