function doSomething(){
    console.log("world");
    process.nextTick(function () {
        for(var i = 0; i < 999999; i++){

        }
        console.log("end")
    });
}
doSomething();
console.log("hello");
