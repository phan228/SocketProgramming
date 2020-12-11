# Socket Programming

Implementation of a client-server application for a private remote model. The client and server can upload/download files and store them in their folders. The functionalities of this include **upload**, **download**, **delete**, and see the content of the shared folder (which contains the information about the files’ sizes, uploading date and time, and the number of downloads)

The client can 
- Make connection to a specified port
- Upload a file to the server
- Download a file from the server
- Delete a file that exists either on the client’s folder or the server’s folder
- See the content of the shared folder. 

On the other hand, the server accepts an incoming connection and handles the commands coming from the client.

## Functionalities

`Connect`: The client request to connect to a specific port number. If successful, it will show “Connection from: (host, port#)” on the server side.

![connect 1](https://user-images.githubusercontent.com/74878333/101846270-9f251f80-3b1e-11eb-9ee5-2d472e0f8201.png)

![connect 2](https://user-images.githubusercontent.com/74878333/101846360-c1b73880-3b1e-11eb-92a6-742d5dd66803.png)

`Upload`: Enter “upload” to upload a file, then type in the file name.
- If the file doesn’t exist in the client’s local folder, there’s nothing to upload --> an “Error!” message will show up:

![upload1](https://user-images.githubusercontent.com/74878333/101846659-6f2a4c00-3b1f-11eb-8ae4-8cf7f99f09c6.png)

- If the file exists in the client’s local folder, the upload process will begin. 

![upload3](https://user-images.githubusercontent.com/74878333/101846671-74879680-3b1f-11eb-9ef8-b7e295ca7b4f.png)

The upload speed is displayed on the terminal as below:

![upload2](https://user-images.githubusercontent.com/74878333/101846665-72bdd300-3b1f-11eb-9fce-32971a8a5584.png)

`Download`: Enter “download” and a file name to download.
- If the file doesn’t exist in the client’s local folder, there’s nothing to upload --> a
“Error!” message will show up:

![dl1](https://user-images.githubusercontent.com/74878333/101846899-ee1f8480-3b1f-11eb-9f3f-bca906149d04.png)

- If the file exists in the server’s folder, the download process will begin.

![dl2](https://user-images.githubusercontent.com/74878333/101846902-efe94800-3b1f-11eb-91f3-a18c7e0c2f0a.png)

`Delete`: Enter “delete” and a file name to delete.

![del1](https://user-images.githubusercontent.com/74878333/101847261-d5639e80-3b20-11eb-9926-d25bd65cd5f8.png)

- If the file is found, the deletion process begins and the result is shown below:

![del2](https://user-images.githubusercontent.com/74878333/101847269-db597f80-3b20-11eb-8dee-08fc6610e8fb.png)

- If the file does not exist:

![del4](https://user-images.githubusercontent.com/74878333/101847275-de547000-3b20-11eb-8f5f-3f829a02b9a3.png)
![del3](https://user-images.githubusercontent.com/74878333/101847280-e01e3380-3b20-11eb-800c-5418de45f6fe.png)

`Dir`:  Enter “dir” and a folder name to see the content of that folder.
- If the folder doesn’t exist, an “Error” message is displayed:

![dir1](https://user-images.githubusercontent.com/74878333/101847543-7eaa9480-3b21-11eb-9307-5bd1b15071df.png)
![dir2](https://user-images.githubusercontent.com/74878333/101847549-80745800-3b21-11eb-993a-218bd9cc4363.png)

- If the folder exists, the content of the folder is displayed as below:

![dir3](https://user-images.githubusercontent.com/74878333/101847559-82d6b200-3b21-11eb-8229-37e93e39f401.png)
![dir4](https://user-images.githubusercontent.com/74878333/101847563-84a07580-3b21-11eb-8204-439b0895ccf4.png)

*2020 Computer Networking*
