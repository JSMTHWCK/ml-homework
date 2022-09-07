class A{
    constructor(a,b,c){
        this.a = a 
        this.b = b
        this.c = c
    }

    ssss(){
        console.log(this.a)
    }
}


let s = new A(1,2,3)
s.ssss()