#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp breakoutroomactivity.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install requests" >> tempdir/Dockerfile
echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  breakoutroomactivity.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/breakoutroomactivity.py" >> tempdir/Dockerfile

cd tempdir
docker build -t webapp .

docker run -t -d -p 8080:8080 --name webrun webapp
docker ps -a