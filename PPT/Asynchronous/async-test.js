function num1() {
    console.log("Num 1 is called");
}

function num2() {
    setTimeout(() =>{
        console.log("Num 2 is called");
    }, 2000);
}

function num3() {
    console.log("Num 3 is called");
}

num1();
num2();
num3();