# Container Export
This applications is a simple dockerized api to create app through post request and export its created file to the project folder.

### Starting application
Run the following commando to build image
> docker build -t container_export .

Then run this one here to start the container for the application and export the container files folder to the files folder of the initial application
> docker run -p 5000:5000 -v /path/to/your_project/files:/app/files container_export

### POST example
```json
{
    "filename": "giva_test.txt",
    "filecontent": "I'm testing this application. If you're reading it, it's because it worked !"
}
```
### Result
Data created while testing application

![image](https://github.com/GivaldoO/container_export/assets/102987993/c7d3eda1-a190-4870-9c7a-28bd49bd2877)
