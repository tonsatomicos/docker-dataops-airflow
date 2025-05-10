# Extração de Dados de Taxa de Juros

## Objetivo
Extrair dados históricos de taxas de juros de uma página web utilizando Selenium, armazená-los em um banco de dados PostgreSQL e agendar o processo com Apache Airflow, tudo dockerizado para facilitar a replicação do ambiente.

## Arquitetura
- Selenium: Para scraping dos dados.
- PostgreSQL: Armazenamento dos dados extraídos.
- Airflow: Orquestração e agendamento do processo.
- Docker: Containerização dos serviços.

## Tecnologias
- Python 3.13
- Selenium
- PostgreSQL
- Apache Airflow
- Docker

## Como Rodar
Subir os containers Docker:

```bash
docker-compose up -d --build
```

## Acessar o Airflow:

Abra seu navegador e vá até http://localhost:8080.

O processo de extração será executado automaticamente conforme o agendamento configurado na DAG do Airflow.

## Estrutura de Arquivos
- /interest-rate-history: Contém o script de extração dos dados.
- /dags: Contém a DAG do Airflow para agendar a execução diária.

## Configuração do PostgreSQL
- Banco de dados: postgres
- Usuário: admin
- Senha: admin
- Porta: 5432