docker compose -f konteneryzacja.yml down

docker rmi task_server:latest
docker rmi task_client:latest
docker rmi springbootapp:latest
docker rmi login_server:latest

docker compose -f konteneryzacja.yml up -d

echo "Containers are up and running."