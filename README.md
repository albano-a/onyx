<img src="tomi_icon.png">

# Onyx TOMI Plotter

 A plotter for the Terrestrial Organic Matter Input Index

## Utilização

Para utilizá-lo, basta baixar e executar o arquivo

## Como usar

Para utilizar o programa:

* Abra o programa executando o arquivo onyx.exe
* Quando a interface aparecer, no lado esquerdo você encontrará as opções necessárias para plotar o TOMI Index.
* Você irá encontrar uma caixa de seleção, para você selecionar o arquivo que deseja plotar. Você também pode importar o arquivo. Onyx TOMI Plotter suporta arquivos `.csv`, `.txt` e `.xlsx`.
* Após selecionar (ou importar) o arquivo, precisará selecionar o tipo de arquivo selecionado (CSV, TXT ou XLSX).
* **ATENÇÃO**: Atualmente, o programa leva em consideração que o arquivo de entrada possui as colunas na seguinte ordem:

<center>

| Profundidade | TVDSS     | TN% | d15N | TOC% | d13C   | TOC/TN |
|--------------|-----------|-----|------|------|--------|--------|
| 1665         | MR - 1665 | --  | --   | --   | -27.20 | 28.43  |
| 1674         | MR - 1674 | --  | --   | --   | -26.90 | 22.88  |  

</center>

Os valores que realmente importam para o cálculo do TOMI Index são o de d13C e TOC/TN. Se você não tiver esses valores, o programa não conseguirá calcular o TOMI Index. O valor de TVDSS, que as vezes não está na segunda coluna, não é necessário se você tiver o valor de mesa rotativa (TVDSS = MR - Prof. Medida).
* Você precisará do valor da mesa rotativa para o cálculo do TOMI Index. Se você não tiver, deixar o espaço em branco apenas resultará em um gráfico utilizando a profundidade medida.
* Se você selecionar um arquivo `.xlsx`, precisará especificar em qual aba do arquivo está o seu arquivo. Se você selecionar um arquivo `.csv` ou `.txt`, o programa irá automaticamente detectar o arquivo. Lembre-se, os dados precisam estar na ordem correta.
* Após isso, pode clicar em plotar, e o programa irá plotar o TOMI Index. Se quiser configurar o plot (alterar o título, cor da linha e o modelo da interpolação realizada) você pode fazer isso clicando na aba "Config. do plot".
* Também tem a opção "Editar" na parte de baixo do plot. Lá você pode alterar algumas configurações mais específicas do plot.
* Na hora de exportar ou salvar, você pode escolher o nome da Formação para nomear a aba da planilha. Se não colocar nada, o nome padrão é "Formação".
* Se você quiser exportar os dados do TOMI Index, basta clicar em "Exportar dados" e escolher o local onde deseja salvar o arquivo.
* Se você quiser salvar o plot, basta clicar em "Salvar" e escolher o local onde deseja salvar o arquivo.

## Créditos
Esse programa foi desenvolvido por André Albano - [GIECAR](http://gcr.sites.uff.br/) 2024