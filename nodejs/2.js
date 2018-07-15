//console.time()和console.timeEnd()这是一对计时器组合，从console.time()开始计时到console.timeEnd()结束。
console.time("hello");
for(var i = 0; i < 10086; i++){

}
console.timeEnd("hello");

//process 属性
//从控制台输入信息
process.stdin.resume();
//获得控制台的信息
process.stdin.on('data', function (data) {
   process.stdout.write('read from console:' + data.toString());
});
//从控制台获得的data默认是以二进制的形式读取，值是一个Buffer对象，所以要用toString将其转化为字符串

//通过参数获取
process.argv.forEach(function (val, index, array) {
   console.log(index + ':' + val);
});
//获取执行路径（即node.exe的路径）
console.log(process.execPath);
//平台信息
console.log(process.platform);

console.log('当前目录' + process.cwd());//输出当前目录
console.log(process.memoryUsage());//内存使用
process.exit(4);//以指定的状态结束进程

//process 成员方法
process.nextTick(callback)
//这个方法为事件循环设置一项任务，Nodejs会在下次事件循环响应时调用callback;Nodejs只有一个线程，在任意时刻只有一个事件在执行。
//Nodejs适合做IO密集型应用，而不是计算密集型应用；如果某个事件占用很长的CPU时间，那么事件循环的下一个事件就会一直等待，Nodejs
//的原则就是尽量缩短每个事件的执行时间。process.nextTick()可以把复杂的工作拆散，编程一个较小的事件。