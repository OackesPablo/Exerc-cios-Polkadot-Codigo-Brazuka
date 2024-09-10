programa {
  funcao inicio() {
    inteiro ano

    escreva("Tu quer saber se o ano é bissexto?\n Basta digitar o ano:")
    leia(ano)

    se(ano % 4==0) {
      escreva("Esse ano é bissexto")} 
      senao {
        escreva("Esse ano não é bissexto")
      }
    }
  }
}
