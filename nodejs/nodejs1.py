'''
nodejs 是JS运行环境，可以让js脚本在服务器端运行
console.log(__filename);console.log(__dirname);全局对象
console.log("%s:%d","hello",25);
console.info();console.error();console.warning() 类似console.log()
console.trace();向标准错误流输出当前调用栈

process描述了Nodejs进程的状态，提供与操作系统的简单接口
通过process在进程上注册相应的事件，在进程执行到某一个时间点（比如进程将要结束，发生异常时）将自动触发这些事件。
为process绑定uncaughtException可以有效的防治遇到未处理错误时打印堆栈跟踪信息并退出程序的默认行为
process.on("uncaughtException", function () {
    console.log("错误已经处理");
})


'''
