#!/bin/sh
docker run -it -p 8080:8080 \
-v `pwd`/../data/:/label-studio/data \
--env LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true \
--env LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/label-studio/files \
-v `pwd`/../data/:/label-studio/files \
heartexlabs/label-studio:latest label-studio
