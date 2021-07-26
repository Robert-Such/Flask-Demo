# REST API with Flask, Docker, PyCharm, Postman and MySQL
This project is to create a REST API and use Postman to test the GET, POST, PUT, and DELETE request
methods.

Docker Compose is being utilized to setup a python flask app and a mysql server which will load data from
the db/init.sql file during the first start up of the database.

The flask framework is being used to create a REST that can be tested with Postman to
demonstrate GET, POST, PUT, and DELETE to retrieve, create, update, and delete records.


## Screenshot showing postman listing all records via GET Request:
![postman all records](screenshots/Postman_AllRecords.png)

## Screenshot of postman showing one record via GET request:
![postman one record](screenshots/Postman_OneRecord.png)

## Screenshot showing postman creating a record by showing the POST request:
![postman one record](screenshots/Postman_NewRecord.png)

## Screenshot showing postman list new record in record listing:
![postman one record](screenshots/Postman_ListNewRecord.png)

## Screenshot showing postman editing a record by showing the PUT request:
![postman one record](screenshots/Postman_EditRecord.png)

## Screenshot showing postman list the edited record in record listing:
![postman one record](screenshots/Postman_ListEditedRecord.png)

## Screenshot showing postman deleting a record by showing the DELETE request:
![postman one record](screenshots/Postman_DeleteRecord.png)

## Screenshot in postman demonstrating that the record in question has been deleted:
![postman one record](screenshots/Postman_ListDeleteRecord.png)



