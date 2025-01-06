# Desafio de Ingestão de Dados e Relatório de Pedidos

Este projeto foi desenvolvido para atender ao desafio proposto de realizar a ingestão de dados a partir de um arquivo posicional, calcular o valor total dos pedidos e gerar um relatório com os 5 pedidos de maior valor total.

## Funcionalidades

- **Leitura de Arquivo Posicional:** O sistema é capaz de ler um arquivo posicional contendo dados sobre pedidos, incluindo número do pedido, quantidade de itens e valor unitário.
- **Cálculo de Valor Total:** Para cada pedido, o sistema calcula o valor total, que é o produto da quantidade de itens pelo valor unitário.
- **Geração de Relatório:** Após o cálculo dos valores totais, o sistema gera um relatório contendo os 5 pedidos com maior valor total.

## Estrutura do Projeto

O projeto é organizado da seguinte maneira:

```bash
desafio-capitani-01/
├── src/
│   ├── init.py         # Arquivo de inicialização do pacote
│   ├── config.py           # Configurações centralizadas do sistema
│   ├── exceptions.py       # Definições de exceções customizadas
│   ├── logger.py           # Configuração de logging
│   ├── main.py             # Ponto de entrada principal do sistema
│   ├── models.py           # Modelos de dados para pedidos
│   ├── repositories.py     # Repositório para leitura e escrita de arquivos
│   └── services.py         # Lógica de negócios do cálculo e relatório
├── data/
│   ├── entrada.txt         # Arquivo de entrada com os dados dos pedidos
│   └── saida.txt           # Arquivo gerado contendo o relatório
├── tests/
│   ├── init.py         # Arquivo de inicialização do pacote de testes
│   ├── test_logger.py      # Testes para o módulo de logging
├── README.md               # Documentação do projeto
├── requirements.txt        # Dependências do projeto
```

### Descrição dos Arquivos

- **src/config.py:** Arquivo de configuração onde são centralizadas as variáveis de ambiente e constantes do sistema.
- **src/exceptions.py:** Definições de exceções customizadas, para melhor controle de erros.
- **src/logger.py:** Configurações do sistema de logs, fornecendo rastreamento adequado das execuções.
- **src/main.py:** Arquivo de entrada principal que orquestra o processo de leitura, cálculo e geração do relatório.
- **src/models.py:** Definição dos modelos de dados que representam um pedido.
- **src/repositories.py:** Responsável pela leitura do arquivo posicional de entrada e gravação do arquivo de saída.
- **src/services.py:** Contém a lógica de negócios que realiza o cálculo do valor total dos pedidos e gera o relatório.

## Como Executar o Projeto

### Pré-requisitos

Certifique-se de que o Python 3.8 ou superior esteja instalado no seu sistema. Caso não tenh o Python instalado, [faça o download aqui](https://www.python.org/downloads/)

### 1. Instalar Dependências

Clone o repositório e instale as dependências necessárias executando os seguintes comandos:

```bash
git clone https://github.com/pesant0s/desafio-capitani-01.git
cd desafio-capitani-01
pip install -r requirements.txt
```

### 2. Configuração dos Arquivos de Entrada e Saída

- O arquivo de entrada entrada.txt deve ser colocado na pasta data/ e deve seguir o formato posicional descrito nos requisitos.
- O arquivo de saída saida.txt será gerado automaticamente na pasta data/ após a execução do programa.

### 3. Executar o Sistema

No repositório do git, já existe um arquivo em data/entrada.txt com um modelo de dados. Caso seja necessário testar com outro modelo, basta substituir os dados dentro do arquivo.

Modelo de dados de entrada para usar

```bash
0000000123010000001500
0000000124010000002000
0000000125010000003000
0000000126010000005000
0000000127010000004500
0000000128010000001000
0000000129010000008000
```

Execute o programa principal com o comando:

```bash
python src/main.py
```

Esse comando irá:

1. Ler o arquivo entrada.txt localizado na pasta data/.
2. Calcular o valor total dos pedidos.
3. Gerar um relatório com os 5 pedidos de maior valor total e salvá-lo no arquivo saida.txt.
4. Exemplos de Arquivos
    • Entrada (entrada.txt): Este arquivo contém os dados dos pedidos no formato posicional, conforme o especificado nos requisitos do desafio.
    • Saída (saida.txt): O relatório gerado, contendo os 5 pedidos de maior valor total, será salvo neste arquivo.

Após a execução do programa, não será exibido nada no terminal. Necessário abrir a pasta de logs/ e verificar o ultimo log gerado com base na data e hora atual.

## Decisões de Projeto

### Estrutura Modular

A escolha de organizar o código em diferentes módulos (como repositories, services, models, etc.) visa uma separação clara de responsabilidades, facilitando a manutenção e o teste do código.

### Uso de Exceções Customizadas

As exceções customizadas permitem um controle mais preciso de erros e um tratamento de falhas mais robusto, melhorando a resiliência do sistema.

### Logging

O sistema de logs foi implementado para registrar as execuções e facilitar o diagnóstico de erros, além de fornecer uma visão geral do fluxo de execução da aplicação.

## Desafios Enfrentados

Leitura de Arquivo Posicional: A interpretação correta dos dados posicionais exigiu atenção ao alinhamento de colunas e ao tratamento de preenchimento com zeros.
Cálculo de Valor Total: Garantir a precisão no cálculo e o formato correto para o valor total de cada pedido foi uma parte crucial do processo.
Desempenho ao Processar Grandes Arquivos: A aplicação foi projetada para ser eficiente, mesmo quando o arquivo de entrada contiver um grande número de pedidos.

## Possíveis Melhorias Futuras

Validação dos Dados: Implementar validações mais robustas para garantir a integridade dos dados de entrada, como verificar se os campos estão dentro dos limites esperados.
Geração de Relatórios em Formatos Diversos: Permitir a geração de relatórios em formatos como CSV ou PDF.
Otimização de Desempenho: Para arquivos muito grandes, pode ser interessante implementar um processamento assíncrono ou em lote para melhorar a escalabilidade.

## Testes

O projeto inclui alguns testes básicos, principalmente para a configuração de logs. Novos testes podem ser adicionados à medida que a aplicação evolui.

Para rodar os testes, utilize o seguinte comando:

```bash
pytest
```

Esse comando irá executar todos os testes automatizados presentes no projeto e fornecer um relatório com os resultados.
