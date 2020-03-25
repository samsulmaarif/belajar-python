docker run --name postgres-db -v `pwd`:/app -w /app -e POSTGRES_PASSWORD=mysecretpassword -dti -p 5432:5432 postgres:alpine

export DATABASE_URL=postgres://postgres:mysecretpassword@localhost:5432/