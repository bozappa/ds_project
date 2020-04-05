# ds_project
Project for DS NCI - gRPC Node.js

Added working chat functionality for node - bidirectional streaming
Run ./node/servers/server.js
Run 2 instances of ./node/clients/client.js 
Runs a chat where a user can input name and chat through the terminal

CRUD functionality added for GOLANG and for Node.js

For Python
python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/imageTest.proto
To start server,

python imageTest_server.py

To start client,

python imageTest_client.py

\\\\\ References /////
https://itnext.io/learning-go-mongodb-crud-with-grpc-98e425aeaae6
https://developers.google.com/protocol-buffers/docs/gotutorial
https://techblog.fexcofts.com/2018/07/20/grpc-nodejs-chat-example/
https://codelabs.developers.google.com/codelabs/cloud-grpc/index.html?index=..%2F..index#3
https://medium.com/@alfianlosari/building-grpc-service-server-note-crud-api-with-node-js-bcc5478d5bdb
http://www.javased.com/index.php?source_dir=jmdns/src/samples/DiscoverServices.java
https://github.com/Nirvan101/GRPC-Video-streaming
