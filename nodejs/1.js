var http = require("http");
http.createServer(function (req,res){
    res.writeHead(200,{'Content-type':"text/html"});
    res.write("<h1>Nodejs</h1>>");
    res.write("<p>Hello World</p>>");
}).listen(8080);
process.on("exit", function (code) {
    console.log("程序已经执行完毕" + code);
    throw new Error("系统错误");
});

process.on("uncaughtException", function () {
    console.log("错误已经处理");
})

console.log("正在启动服务器")
console.log(__filename);
console.log(__dirname);