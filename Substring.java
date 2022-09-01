class Substring {
  public static void main(String[] args) {
    System.out.println("La palabra recortada es: " + retornarPalabraRetornada("Lasfloresazules", 3, 9));
  }

  public static String retornarPalabraRetornada(String palabra, int desde, int hasta)
  {
    String palabraRecortada = palabra.substring(desde,hasta);
    return palabraRecortada;
  }
}
