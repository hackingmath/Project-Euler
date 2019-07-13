var primeNums = [2];
var isPrime;
console.time("time");
function checkForPrime(num){
  //returns true if num is prime
  isPrime = true;

  for(var i=3;i<Math.ceil(Math.sqrt(num)+1);i+=2){
    if (num % i == 0){
      isPrime = false;
    }
  }
  return isPrime;
}
var i = 3;
while(primeNums.length < 10001){
 if(checkForPrime(i)){
    primeNums.push(i);
  }
  i+=2;
}
console.timeEnd("time");
console.log(primeNums[10000]);
