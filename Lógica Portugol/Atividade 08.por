programa {
  funcao inicio() {
    inteiro ano

    escreva("Tu quer saber se o ano � bissexto?\n Basta digitar o ano:")
    leia(ano)

    se(ano % 4==0) {
      escreva("Esse ano � bissexto")} 
      senao {
        escreva("Esse ano n�o � bissexto")
      }
    }
  }
}
