# Simulador de Automatos (LFA) 🤖

Este projeto contém simuladores de Autômatos Finitos Determinísticos (AFD) e Não-Determinísticos (AFN) desenvolvidos em Python para a disciplina de Linguagens Formais e Autômatos.

## 📁 Estrutura do Projeto

* `afd.py`: Simulador de AFD configurado para validar palavras com uma quantidade par de símbolos `1`.
* `afn.py`: Simulador de AFN configurado para validar a expressão regular que reconhece transições usando conjuntos de estados.
* `requirements.txt`: Arquivo com as dependências do projeto.

##  Como Executar o Projeto

### 1. Configurar o Ambiente Virtual
Certifique-se de ativar o ambiente virtual antes de rodar os scripts:
```powershell
.\venv\Scripts\Activate.ps1

### 2. Executar o AFD
Para rodar o simulador do AFD, utilize o comando:
python afd.py
Exemplo de teste: Digite 1100 (a palavra será aceita)

### 3. Executar o AFN
Para rodar o simulador do AFN, utilize o comando:
python afn.py
Exemplo de teste: Digite ab (a palavra será aceita)
