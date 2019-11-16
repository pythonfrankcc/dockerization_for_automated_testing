#base image we want to use 
FROM alpine: 3.1

#adding python to the docker image
RUN apk add --update python py-pip

#install our dependencies
RUN pip install -r requirements.txt 

#bundle our app source 
COPY docker-app-test.py /src/docker-app-test.py

#Expose 8000 and run the application
EXPOSE 8000
CMD ["python","/src/docker-app-test.py","-p 8000"]