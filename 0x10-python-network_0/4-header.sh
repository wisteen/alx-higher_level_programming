#!/bin/bash

url=$1
header="X-School-User-Id: 98"

curl -s -H "$header" "$url"
echo ""
