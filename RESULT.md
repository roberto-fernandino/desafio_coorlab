# Resultado - Desáfio CoorLab

## Backend

Para estruturar minha API, optei por utilizar o Django Rest Framework devido à sua simplicidade e à minha experiência avançada com o Django. O Django Rest Framework proporcionou uma maneira eficiente e organizada de criar endpoints RESTful, permitindo uma rápida implementação das funcionalidades necessárias para o desafio. Com a familiaridade que já possuía com o Django, pude otimizar meu tempo e focar em desenvolver recursos robustos e escaláveis para a aplicação.

### Estrutura

Utilizando um banco de dados SQL no caso sqlite3 criei apenas duas tabelas

**Trip**

| Campo         | Tipo                     |
| ------------- | ------------------------ |
| name          | CharField max_length=100 |
| price_confort | FloatField               |
| price_econ    | FloatField               |
| city          | ForeignKey -> City       |
| duration      | CharField max_length=10  |
| seat          | CharField max_length=100 |
| bed           | CharField max_length=100 |

**City**

| Campo | Tipo                                 |
| ----- | ------------------------------------ |
| name  | CharField max_length=100 unique=True |

## Frontend

No que diz respeito ao frontend, enfrentei um desafio estimulante ao precisar aprender Vue do zero. Essa experiência foi enriquecedora, e relativamente tranquilia devido ao meu conhecimento prévio de frameworks de JS orientado a componentes, foi muito bacana pois me desafiou a expandir meu conhecimento e me provou capaz de assimilar novas tecnologias rapidamente. Aprender Vue foi jornada gratificante, descobri sua eficiência e poder na criação de interfaces dinâmicas e responsivas.

Ao desenvolver o frontend, optei por uma abordagem mais orientada a componentes. Quase todas as partes da interface que exigiam reatividade e dinamismo foram implementadas como componentes Vue. Essa prática não apenas simplificou o código, tornando-o mais legível e fácil de dar manutenção, mas também promoveu a reutilização de código e a modularidade da aplicação.

### Componentes

## Componente Trip.vue

O componente `Trip.vue` é responsável por exibir informações sobre uma viagem específica. Ele usa a sintaxe de interpolação Vue para vincular dados dinâmicos ao modelo que mudarção dinâmicamente os icones das viagens de acordo com seu atributo de `Barata`e `Rapida` e até ambas as duas ao mesmo tempo.

### Estrutura do Componente

O componente é composto por três seções principais:

1. **Ícones de Informação da Viagem**: Esta seção contém dois ícones que indicam se a viagem é a mais barata e a mais rápida. O código a seguir mostra essa seção:

   ```vue
   <div id="twoIcons">
       <img src="../assets/hand-coins-white.svg" alt="cheaper icon" id="icon1" />
       <div id="divider"></div>
       <img src="../assets/clock-clockwise.svg" alt="cheaper icon" id="icon2" />
   </div>
   ```

2. **Informações da Viagem**: Esta seção exibe o nome da viagem e a duração estimada. O código a seguir mostra essa seção:

   ```vue
   <div class="tripInfo">
       <span class="tripCompanion">{{ trip.name }}</span>
       <div class="tripDuration">Tempo estimado: {{ trip.duration }}h</div>
   </div>
   ```

3. **Preços da Viagem**: Esta seção exibe os preços para as opções "Convencional" e "Leito". O código a seguir mostra essa seção:

   ```vue
   <div class="tripPrice">
       Convencional R${{ trip.price_econ }} <br />
       Leito: R${{ trip.price_confort }}
   </div>
   ```

Os dados para cada viagem são passados para o componente como propriedades, que são então usadas para preencher as informações exibidas.

## Componente Prices.vue

Este componente é responsável por permitir o usuário escolher datas e destinos e mostrar os resultados renderizando o(s) componente(s) `Trip` o forçando a preencher os dois inputs de **date** e **select**.

Além disso tem a função de consultar o banco de dados já que atua como um intermédiario entre o usuario e os dados portanto ele tem alguns métodos de consulta da nossa `API rest`.

## Metodos

### getCities()

Este método é responsável por obter todas as cidades disponíveis da API. Ele faz uma requisição GET para a rota `http://localhost:3000/api/cities/?format=json`. As cidades obtidas são então adicionadas ao array `this.cities`, desde que a cidade não esteja já presente no array.

### searchTrips()

Este método é responsável por buscar viagens com base na cidade selecionada e na data. Ele primeiro limpa o array `this.trips` para garantir que não haja dados antigos. Em seguida, verifica se o usuário selecionou uma cidade e uma data. Se não, ele emite um evento de erro.

Se uma cidade e uma data foram selecionadas, ele faz uma requisição GET para a rota `http://localhost:3000/api/trips/by_city/${cityId}`. As viagens obtidas são então adicionadas ao array `this.trips`.

Durante a adição de cada viagem ao array, o método também verifica se a viagem é a mais barata ou a mais rápida até agora. Ele faz isso comparando o preço e a duração da viagem com a viagem mais barata e mais rápida conhecida até agora. Se a viagem é mais barata ou mais rápida, ela é marcada como tal.

Finalmente, o método remove um elemento span do DOM e marca a busca como concluída.

##### Fluxo de Trabalho

1. O usuário seleciona uma cidade e uma data.
2. O método `searchTrips()` é chamado.
3. O método `searchTrips()` limpa o array `this.trips`.
4. O método `searchTrips()` verifica se uma cidade e uma data foram selecionadas e se não tiver renderiza o componente _`Modal`_.
5. Se uma cidade e uma data foram selecionadas, o método `searchTrips()` faz uma requisição GET para a API para obter viagens que correspondam à cidade e à data.
6. O método `searchTrips()` adiciona cada viagem obtida ao array `this.trips`, marcando a viagem mais barata e mais rápida.
7. O método `searchTrips()` remove um elemento span do DOM e marca a busca como concluída.

### Observações

Quanto ao envio do desafio, gostaria de explicar que sofri uma cirurgia há três dias, no dia 20 de março, e precisei de alguns dias de repouso para me recuperar. Apesar dos contratempos, dediquei meu tempo de recuperação não apenas para me recuperar fisicamente, mas também para trabalhar no desafio, garantindo que entregasse um trabalho de qualidade dentro do prazo estabelecido.

Estou ansioso para discutir em detalhes minha implementação e como minhas escolhas de tecnologia contribuíram para atender aos requisitos do desafio. Agradeço pela oportunidade e aguardo ansiosamente o feedback.

#### Passo a passo pra execução do projeto.

1. Entre no diretório app
2. Execute o bashscript de execução da aplicação

```bash
./run.sh
```

Ele ira:

1. **Instalar dependências**
2. **Executar os dois servidores em segundo plano**
3. **Salvar o pid dos "jobs" para matar-los corretamente ao precionar `"CTRL + C"` na sessão do terminal**
