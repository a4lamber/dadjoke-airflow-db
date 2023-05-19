# run the minio server on port 9000, management console on port 9001
# the local mount is ".data"
docker container run -p 9000:9000 -p 9001:9001 \
                     --name minio_server_v01 \
                     -d \
                     -e "MINIO_ROOT_USER=airflow_minio_s3" \
                     -e "MINIO_ROOT_PASSWORD=airflow_minio_s3"\
                     quay.io/minio/minio server /data --console-address ":9001"