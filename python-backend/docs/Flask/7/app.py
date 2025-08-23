from flask import Flask
app=Flask('__name__')
@app.route("/<int:number>")
def prime(number):
    fibs="First  "+str(number)+" Fibonacci numbers : "
    fib1=0
    fib2=1
    
    for i in range(2,number+1):
          fibs+= str(fib1)+", "
          fib1,fib2=fib2,fib1+fib2
    return fibs

if __name__ == '__main__':
   app.run()