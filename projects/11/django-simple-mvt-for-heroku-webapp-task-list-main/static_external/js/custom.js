function Change(){
    console.log("Hi!");
    let obj2 = document.getElementById("123456");
    let obj3 = document.getElementById("password");
    let obj4 = document.getElementById("password1");
    obj2.addEventListener('click', ({ target }) => {
        if (obj3.type === 'password'){
            obj3.type = 'text';
            obj4.type = 'text';
        } else {
            obj3.type = 'password';
            obj4.type = 'password';
        }
    });
}