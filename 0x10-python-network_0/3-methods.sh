#!/bin/bash
# 3. cURL only methods
curl -i -s $1 | grep "Allow: " | cut -d " " -f 2,3,4
