# testesdoMal
Projeto exclusivamente educacional, simulando o funcionamento de keyloger e ransomware

🛡 Simulação Educacional de Malware com Python
📌 Sobre o Projeto

Este projeto tem finalidade exclusivamente educacional, simulando o funcionamento de dois tipos de malware:

Ransomware
Keylogger

Todos os testes foram realizados em ambiente controlado (máquina virtual), sem qualquer risco a sistemas reais.

🔐 Parte 1 — Ransomware Simulado
🎯 Objetivo

Demonstrar como um ransomware:

Percorre arquivos
Criptografa conteúdo
Sobrescreve arquivos
Exibe mensagem de resgate
Permite descriptografia com chave correta
⚙ Tecnologias Utilizadas
Python 3.x
Biblioteca cryptography (Fernet)
Manipulação de arquivos com os e pathlib
🧠 Funcionamento Técnico
1️⃣ Geração da chave
Uma chave simétrica é gerada usando Fernet.
A chave é salva no arquivo key.key.
2️⃣ Varredura do diretório

O script percorre apenas:

ransomware_simulado/arquivos_teste/

Utiliza:

os.listdir()
open(..., "rb")
open(..., "wb")
3️⃣ Criptografia

Para cada arquivo:

Lê conteúdo binário
Aplica fernet.encrypt()
Sobrescreve o conteúdo original
4️⃣ Mensagem de resgate

É criado um arquivo:

LEIA_IMPORTANTE.txt

Com uma mensagem simulando pedido de resgate.

🔓 Descriptografia

O script decrypt.py:

Carrega a chave salva
Percorre os mesmos arquivos
Aplica fernet.decrypt()
Restaura o conteúdo original
⌨ Parte 2 — Keylogger Simulado
🎯 Objetivo

Simular captura de teclas digitadas e armazenamento em log local.

⚙ Tecnologias Utilizadas
Python 3.x
Biblioteca pynput
smtplib (simulação de envio de e-mail)
🧠 Funcionamento Técnico
1️⃣ Captura de teclas

Utiliza:

pynput.keyboard.Listener
Callback on_press()

Cada tecla pressionada é registrada.

2️⃣ Tratamento de teclas especiais
Espaço → " "
Enter → "\n"
Backspace → marcador especial
3️⃣ Armazenamento

O log é salvo em:

keylogger_simulado/logs.txt

Modo append ("a").

4️⃣ Envio por e-mail (simulado)

O script pode:

A cada X teclas
Ou a cada Y segundos

Enviar o arquivo como anexo via SMTP.

Foi utilizado:

smtplib
email.message
TLS na porta 587
🔍 Técnicas de Defesa Identificadas
Contra Ransomware
Backups offline
Controle de privilégios
Monitoramento de modificação em massa
EDR com análise comportamental
Bloqueio de execução em diretórios temporários
Contra Keylogger
Antivírus com monitoramento de hooks de teclado
Firewall bloqueando conexões SMTP suspeitas
MFA
Monitoramento de processos em background
Whitelisting de aplicações
🧪 Evidências de Execução

(Imagens dentro da pasta /images)

Execução do encrypt.py
Arquivos criptografados
Execução do decrypt.py
Log de teclas capturado
📚 Aprendizados

Durante o desenvolvimento deste projeto, foi possível compreender:

Como funciona criptografia simétrica
Como eventos de teclado são interceptados
Como malwares exploram engenharia social
A importância de defesa em camadas
A relevância do fator humano na segurança
🚨 Considerações Éticas

Este projeto foi desenvolvido exclusivamente para fins acadêmicos, em ambiente controlado, com o objetivo de compreender ameaças digitais e aprimorar estratégias defensivas.

💻 Como Executar

Instalar dependências:

pip install cryptography pynput

Executar ransomware:

python encrypt.py

Descriptografar:

python decrypt.py

Executar keylogger:

python keylogger.py
