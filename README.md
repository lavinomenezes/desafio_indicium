# Problema

objetivo é identificar quais máquinas apresentam potencial de falha tendo como base dados extraídos através de sensores durante o processo de manufatura.

**Dataset overview**


| **Variable** | **Meaning** |
|:----------:|---------|
UID | unique identifier ranging from 1 to 10000|
product ID | consisting of a letter L, M, or H for low (50% of all products), medium (30%) and high (20%) as product quality variants and a variant-specific serial number|
type | just the product type L, M or H from column 2|
air temperature [K] | generated using a random walk process later normalized to a standard deviation of 2 K around 300 K|
process temperature [K] | generated using a random walk process normalized to a standard deviation of 1 K, added to the air temperature plus 10 K.|
rotational speed [rpm] | calculated from a power of 2860 W, overlaid with a normally distributed noise|
torque [Nm] | torque values are normally distributed around 40 Nm with a SD = 10 Nm and no negative values.|
tool wear [min] | The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process.|

##  Premissas do negócio

<ul>
<li>O dataset possui a variável target 'failure_type' com 6 classes no total, caracterizando um porblema de classificação multiclasse</li>
<li>As classes tem valores diferentes assim o dataset é autamente desbalanceado, chegando a classe majoritária a corresponder por quase 97% do conjunto de dados</li>
<li>o dataset é de baixa dimensionalidade</li>
</ul>

## Planejamento da Solução

Neste projeto foi aplicado o método CRISP-DM (Cross-Industry Standard Process for Data Mining) adaptado para os processos de ciência de dados que se tornou o CRIS-DS.

![](https://github.com/lavinomenezes/Rossmann_store_sales/blob/main/images/crisp.png)

Modelo crisp-dm

A divisão dos passos utilizados no projeto foi:

<ol>
<li><strong>Entendimento do problema:</strong> observando o conjunto de dados tentar entender de que tipos de máquinas esta sendo tratada e entender o ponto de vista da manutenção as consequências de para uma parada programado do equipamento versos uma parada de emergência devido a falha, assim, entendendo melhor o problema para apresentar a solução mais eficiente no menor tempo possível.
</li>

<li>
<strong>Coleta de dados:</strong> Todos os dados estavam disponíveis em dos datasets um de treino e outra para teste sem a váriavel de resposta.
</li>
<li>
<strong>Análise descritiva:</strong> Uma breve análise dos dados para adquirir familiaridade com os mesmo, incluindo o tamanho do data frame que estamos lidando assim como os tipo de dados que vamos processar, aplicando estatística descritiva sobre as informações para conhecer o comportamento dela.   
</li>
<li>
<strong>Dados faltantes:</strong> sem dados faltante.    
</li>
<li>
<strong>Feature engineering:</strong> Nesse ciclo do projeto, não houve criação de nenhum feature
</li>