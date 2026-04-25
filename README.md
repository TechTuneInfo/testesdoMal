# 🛡 Simulação Educacional de Malware com Python

> ⚠️ **Aviso Importante**  
> Este projeto foi desenvolvido exclusivamente para fins educacionais, em ambiente controlado (máquina virtual), com o objetivo de compreender o funcionamento de ameaças digitais e estudar estratégias de defesa.  
> Nenhum código aqui deve ser utilizado fora de ambiente de testes.

---

# 📌 Sobre o Projeto

Este projeto simula o comportamento de dois tipos de malware amplamente utilizados em ataques reais:

- 🔐 **Ransomware**
- ⌨ **Keylogger**

O objetivo é compreender, na prática:

- Como esses malwares operam  
- Quais vulnerabilidades exploram  
- Como podem ser detectados  
- Quais estratégias de mitigação são eficazes  

---

# 🎯 Objetivos de Aprendizagem

Ao desenvolver este projeto, foram explorados os seguintes conceitos:

- Manipulação de arquivos em Python  
- Criptografia simétrica  
- Captura de eventos do teclado  
- Comunicação via protocolo SMTP  
- Pensamento ofensivo e defensivo em segurança  
- Documentação técnica estruturada  

---

# 🗂 Estrutura do Projeto

```
malware-simulation-python/
│
├── ransomware_simulado/
│ ├── encrypt.py
│ ├── decrypt.py
│ ├── key.key
│ └── arquivos_teste/
│ ├── teste1.txt
│ ├── teste2.txt
│
├── keylogger_simulado/
│ ├── keylogger.py
│ └── logs.txt
│
├── images/
│
└── README.md
```


---

<details>
  <summary>
    # 🔐 Parte 1 — Ransomware Simulado
  </summary><br>

## 📖 Objetivo

Simular o comportamento básico de um ransomware:

1. Gerar chave criptográfica  
2. Percorrer arquivos em diretório controlado  
3. Criptografar conteúdo  
4. Sobrescrever arquivos  
5. Criar mensagem simulando pedido de resgate  
6. Permitir descriptografia com chave correta  

---

## ⚙ Tecnologias Utilizadas

- Python 3.x  
- Biblioteca `cryptography` (Fernet)  
- Manipulação de arquivos (`os`, `pathlib`)  

---

## 🧠 Funcionamento Técnico

### 🔑 Geração da Chave

- É utilizada criptografia simétrica  
- A chave é gerada com Fernet  
- A chave é armazenada localmente em `key.key`  

---

### 📂 Varredura de Diretório

O script atua **apenas** no diretório: ransomware_simulado/arquivos_teste/


São utilizados:

- `os.listdir()` ou `os.walk()`  
- `open(..., "rb")`  
- `open(..., "wb")`  

---

### 🔒 Processo de Criptografia

Para cada arquivo:

1. Leitura em modo binário  
2. Aplicação de criptografia  
3. Sobrescrita do conteúdo original  

---

### 📝 Mensagem de Resgate

Após a criptografia, é criado um arquivo: SIFU_DEU.txt


Simulando uma mensagem típica de ransomware.

---

### 🔓 Processo de Descriptografia

O script `decrypt.py`:

1. Lê a chave salva  
2. Percorre os arquivos criptografados  
3. Aplica descriptografia  
4. Restaura o conteúdo original  

---
</details>

<details>
  <summary>
    # ⌨ Parte 2 — Keylogger Simulado
  </summary><br>

## 📖 Objetivo

Simular a captura de teclas digitadas e armazenamento em log local.

---

## ⚙ Tecnologias Utilizadas

- Python 3.x  
- Biblioteca `pynput`  
- `smtplib` (simulação de envio de e-mail)  

---

## 🧠 Funcionamento Técnico

### 🎹 Captura de Teclas

- Utiliza `pynput.keyboard.Listener`  
- Implementa função de callback para capturar eventos de tecla pressionada  

---

### 🔎 Tratamento de Teclas Especiais

- Espaço → `" "`  
- Enter → `"\n"`  
- Backspace → marcador especial  
- Teclas especiais são tratadas para manter legibilidade  

---

### 🗂 Registro em Arquivo

As teclas capturadas são armazenadas em: keylogger_simulado/logs.txt


Utilizando modo append (`"a"`).

---

### 📧 Envio por E-mail (Simulado)

O projeto demonstra conceitualmente:

- Uso do protocolo SMTP  
- Conexão TLS (porta 587)  
- Envio automatizado após determinado critério (tempo ou volume de dados)  

---
</details>

# 🛡 Técnicas de Defesa Identificadas

## 🔐 Contra Ransomware

- Backups offline  
- Controle de privilégios  
- Atualizações regulares  
- Monitoramento de modificação em massa  
- EDR com análise comportamental  
- Segmentação de rede  

---

## ⌨ Contra Keylogger

- Antivírus com monitoramento comportamental  
- Firewall bloqueando conexões suspeitas  
- MFA (Autenticação Multifator)  
- Monitoramento de processos em segundo plano  
- Whitelisting de aplicações  

---

# 🔎 Como Detectar Esse Tipo de Ameaça

## Indicadores de Ransomware:

- Uso elevado de CPU  
- Modificação simultânea de múltiplos arquivos  
- Criação de arquivos de resgate  
- Alterações inesperadas em extensões  

## Indicadores de Keylogger:

- Processos ocultos em execução contínua  
- Acesso constante a eventos de teclado  
- Conexões SMTP não usuais  
- Arquivos de log sendo atualizados constantemente  

---

# 🧪 Ambiente de Testes

- Execução realizada em máquina virtual  
- Ambiente isolado  
- Sem acesso a arquivos reais do sistema  
- Uso exclusivo de arquivos de teste  

---

# 📚 Aprendizados Obtidos

Durante o desenvolvimento deste projeto, foi possível:

- Compreender o funcionamento interno de ransomware  
- Entender como eventos de teclado podem ser interceptados  
- Identificar vulnerabilidades exploradas por engenharia social  
- Estudar medidas reais de defesa  
- Desenvolver pensamento crítico voltado para segurança ofensiva e defensiva  

---

# ⚖ Considerações Éticas

O estudo de malware é fundamental para profissionais de segurança da informação.  
Este projeto foi desenvolvido com responsabilidade, visando exclusivamente aprendizado e conscientização sobre ameaças digitais.

---

# 🚀 Como Executar

Instalar Dependências
```
pip install cryptography pynput
```
Executar Ransomware (Simulação)
```
python encrypt.py
```
Descriptografar Arquivos
```
python decrypt.py
```
Executar Keylogger (Simulação)
```
python keylogger.py
```

