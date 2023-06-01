# Python Technical Challenge


## Question 1

O método *get_top_N_open_contracts* recebe três parâmetros de entrada: *open_contracts*, *renegotiated_contracts* e *top_n*. Ele retorna uma lista dos *top_n* contratos abertos com a dívida mais alta, excluindo os contratos que foram renegociados.

O método primeiro filtra todos os contratos em *open_contracts* que foram renegociados, usando um for e o operador not in. Em seguida, ele classifica os contratos restantes em ordem decrescente de dívida, usando a função *sorted* e uma função *lambda* para especificar a chave de classificação. Por fim, ele retorna uma lista dos *IDs* dos contratos *top_n*, usando outro for e dividindo a lista classificada.

Alguns erros encontrados foram na parte de separar os contratos para remover os que já haviam sido renegociados.

## Question 2

Nessa implementação, primeiro classificamos a lista de solicitações em ordem decrescente. Isso nos permite começar com as maiores solicitações e emparelhá-las com solicitações menores para minimizar o número de viagens necessárias.

Em seguida, inicializamos uma variável *num_trips* como 0 e dois ponteiros *i* e *j* para o início e o fim da lista de solicitações, respectivamente. Usamos um loop while para iterar sobre a lista de solicitações, emparelhando as solicitações do início e do fim da lista até que tenhamos emparelhado todas as solicitações.

Para cada iteração do loop, verificamos se a soma das solicitações apontadas por *i* e *j* é menor ou igual a *n_max*. Se for, decrementamos j para passar para a próxima solicitação do início da lista. Sempre diminuímos *j* para passar para a próxima solicitação a partir do final da lista. Também incrementamos *num_trips* para contar o número de viagens necessárias.

Quando o loop é concluído, retornamos o valor final de *num_trips*, que representa o número mínimo de viagens necessárias para atender a todas as solicitações.

Alguns erros encontrados foram na parte da soma onde em alguns casos o código não somava os valores corretamente acarretando em um valor maior de num_trips.
