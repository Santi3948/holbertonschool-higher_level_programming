#!/bin/bash
# 0. cURL body size
curl --head -s $1 | grep "Content-Length" | cut -d " "  -f 2
