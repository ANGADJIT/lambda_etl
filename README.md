# Lambda Etl
<br>
<img src="https://user-images.githubusercontent.com/67195682/232246075-99c4bce8-23f6-416f-b6b4-06bbc634b3a3.png">
<br><br>

## Workflow Explanation
1. First we are getting todo object one by one using this link https://jsonplaceholder.typicode.com/todos/{todo_number} and each object will be stored as json file in s3 under landing folder with naming as todo_{todo_number}.json .
2. After uploading all the objects , we have to get all the stored objects from landing folder that we can transform it .
3. After getting the objects we are partitioning by key completed and storing into 2 seprated list for completed and not_completed .
4. After partitioning data we are uploading data in csv format , here are 2 files will be uploaded not_completed_todos.csv and compleded_todos.csv .
