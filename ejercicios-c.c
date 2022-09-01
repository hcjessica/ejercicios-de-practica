#include <stdio.h>

int main(void) {
  int result = retornarNumeroMayor(18, 6, 5, 15);
  printf("El número mayor de los 4 números brindados es:\n");
  //entero
  printf("%d", result);
}

int retornarNumeroMayor(int valor1, int valor2, int valor3, int valor4) {
  int numeros[4] = {valor1, valor2, valor3, valor4};
  int mayor = 0;

  for (int i = 0; i < sizeof(numeros); i++) {
    if (mayor < numeros[i]) {
      mayor = numeros[i];
    }
  }

  return mayor;
}