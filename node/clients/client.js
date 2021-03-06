let grpc = require("grpc");
var protoLoader = require("@grpc/proto-loader");
var readline = require("readline");
 
//Read terminal Lines
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
 
//Load the protobuf
var proto = grpc.loadPackageDefinition(
  protoLoader.loadSync("../../proto/chat.proto", {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
  })
);
 
const REMOTE_SERVER = "0.0.0.0:5001";
 
let username;
 
//Create gRPC client
let client = new proto.dsproject.Chat(
  REMOTE_SERVER,
  grpc.credentials.createInsecure()
);
 
//Bi-directional streaming
function startChat() {
  let channel = client.join({ user: username });
 
  channel.on("data", onData);
 
  rl.on("line", function(text) {
    client.send({ user: username, text: text }, res => {});
  });
}
 
//When server send a message
function onData(message) {
  if (message.user == username) {
    return;
  }
  console.log(`${message.user}: ${message.text}`);
}
 
//Ask user name then start the chat
rl.question("Enter name: ", answer => {
  username = answer;
 
  startChat();
});