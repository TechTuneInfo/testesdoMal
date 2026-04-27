# 🛡️ Simulação Educacional de Malware com Python

> ⚠️ **Aviso Importante**  
> Este projeto foi desenvolvido exclusivamente para fins educacionais, em ambiente controlado (máquina virtual), com o objetivo de compreender o funcionamento de ameaças digitais e estudar estratégias de defesa. **Nenhum código aqui deve ser utilizado fora de ambientes de teste.**

---

# 📌 Sobre o Projeto

Este repositório contém a implementação de duas ameaças simuladas para análise de comportamento, impacto e contramedidas:

- 🔐 **Ransomware**: Sequestro de dados via criptografia simétrica.
- ⌨️ **Keylogger**: Monitoramento de entrada de dados e exfiltração remota.

O objetivo é compreender como essas ameaças operam, quais vulnerabilidades exploram e como aplicar estratégias de mitigação eficazes.

---

# 🎯 Objetivos de Aprendizagem

Ao desenvolver este projeto, foram explorados os seguintes conceitos técnicos:
- **Criptografia Simétrica**: Uso de chaves AES para proteção/sequestro de dados.
- **Intercepção de Eventos**: Captura de I/O de teclado em nível de software.
- **Protocolos de Rede**: Comunicação via SMTP para exfiltração de informações.
- **Segurança Defensiva**: Identificação de Indicadores de Comprometimento (IoCs).

---

# 🗂️ Estrutura do Repositório

```text
testesdoMal/
│
├── ranrans/                 # Módulo de Ransomware
│   ├── ramsonware.pyw       # Script de ataque (execução oculta)
│   ├── decrypt.py           # Ferramenta de restauração de arquivos
│   ├── chave.key            # Chave gerada para a sessão de teste
│   ├── SIFU_DEU.txt         # Mensagem de resgate
│   └── arquivos_teste/      # Pasta contendo arquivos para simulação
│
├── keyL/                    # Módulo de Keylogger
│   ├── keylogger.pyw        # Captura local com lógica de cooldown
│   ├── keylogger_email.py   # Script de captura com envio via SMTP
│   └── logs.txt             # Arquivo de armazenamento dos logs
│
└── README.md
```

---

# 🔐 Parte 1 — Ransomware Simulado

## 🧠 Funcionamento Técnico

1.  **Geração de Chave**: Utiliza a biblioteca `cryptography` (Fernet) para criar uma chave única de 32 bytes.
2.  **Varredura Recursiva**: O script percorre o diretório alvo utilizando `os.walk`, identificando arquivos para cifrar.
3.  **Criptografia in-place**: Os arquivos são lidos em modo binário, criptografados e sobrescritos imediatamente, tornando o conteúdo original inacessível sem a chave.
4.  **Nota de Resgate**: É gerado o arquivo `SIFU_DEU.txt`, simulando a comunicação de um atacante real.

### Comandos de Execução
```bash
# Instalar biblioteca necessária
pip install cryptography

# Executar a criptografia
python ranrans/ramsonware.pyw

# Executar a restauração
python ranrans/decrypt.py
```

---

# ⌨️ Parte 2 — Keylogger Simulado

## 🧠 Funcionamento Técnico

1.  **Captura de Teclas**: Utiliza o `pynput.keyboard.Listener` para registrar eventos de entrada em tempo real.
2.  **Lógica de Cooldown**: Implementa um intervalo de 60 segundos. Caso o usuário pare de digitar por esse tempo, o script insere automaticamente um marcador de data/hora para organizar o log.
3.  **Tratamento de Caracteres**: Converte teclas especiais (Espaço, Enter, Backspace) em formatos legíveis no arquivo final.
4.  **Exfiltração (Conceitual)**: O módulo de e-mail utiliza `smtplib` com TLS para enviar os dados acumulados para um servidor remoto de forma assíncrona.

### Comandos de Execução
```bash
# Instalar biblioteca necessária
pip install pynput

# Iniciar o monitoramento
python keyL/keylogger.pyw
```

---

# 🛡️ Estratégias de Defesa Recomendadas

### Contra Ransomware
- **Backups Offline**: Manter cópias de segurança desconectadas da rede (Regra 3-2-1).
- **Monitoramento de Arquivos**: Ferramentas de FIM (File Integrity Monitoring) que detectam mudanças em massa.

### Contra Keylogger
- **MFA (Autenticação Multifator)**: O uso de códigos dinâmicos anula a utilidade de uma senha capturada.
- **Teclado Virtual**: Utilização de interfaces visuais para digitação de senhas críticas (ex: bancos).

### Como Detectar
- **Análise de Processos**: Monitorar processos `python.exe` sem janela visível via **Process Explorer**.
- **Indicadores de Rede**: Conexões inesperadas para servidores SMTP (Porta 587) partindo de estações de trabalho.

---

# 🧪 Ambiente de Testes
- **Virtualização**: Todos os testes foram realizados em máquina virtual (VMWare/VirtualBox) isolada da rede principal.
- **Controle**: Uso de pastas específicas para teste, garantindo a integridade dos arquivos do sistema operacional.

---

# ⚖️ Considerações Éticas
Este projeto foi desenvolvido com responsabilidade, visando exclusivamente o aprendizado técnico e a conscientização sobre ameaças digitais. A segurança ofensiva é estudada aqui como ferramenta para construir defesas mais sólidas.
