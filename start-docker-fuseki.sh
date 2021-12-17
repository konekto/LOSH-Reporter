#!/bin/zsh

docker run --rm -it -p 3030:3030 --name fuseki -e ADMIN_PASSWORD=testtest -e ENABLE_DATA_WRITE=true -e ENABLE_UPDATE=true -e ENABLE_UPLOAD=true -e QUERY_TIMEOUT=5000 --mount type=bind,source="$(pwd)"/fuseki-data,target=/fuseki-base/databases --mount type=bind,source="$(pwd)"/fuseki-configuration,target=/fuseki-base/configuration secoresearch/fuseki
