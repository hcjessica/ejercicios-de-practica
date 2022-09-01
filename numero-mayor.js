let mayor1 = 0; 
let mayor2 = 0; 
let statusSegundoMayor = false;
let mayor = 0;
let numeros = [2,6,3,7,1,10];
let contador = 0;
do{
  for (let index = 0; index < numeros.length; index++) {
    if(statusSegundoMayor)
    {
      if(numeros[index] != mayor1)
      {
        if(numeros[index] > mayor){
          mayor = numeros[index];        
        }
      }  
    }else
    {
      if(numeros[index] > mayor){
          mayor = numeros[index];
      }
    }
  }

  if(!statusSegundoMayor)
  {
    mayor1 = mayor;
    mayor = 0;
    statusSegundoMayor = true;
    contador = 1;
  }else
  {
    mayor2 = mayor;
    contador = 2;
  }
  
}while(contador < 2);

console.log("Mi primer valor 1 mayor es: " + mayor1);
console.log("Mi segundo valor 2 mayor es: " + mayor2);
