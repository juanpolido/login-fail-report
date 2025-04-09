🔐 Analisador de Falhas de Login (Log Analyzer)

Script em Python que analisa arquivos de log (auth.log) para identificar tentativas de login malsucedidas. Ele extrai os IPs envolvidos nas falhas, conta a quantidade de tentativas por IP, ordena do maior para o menor, e gera um relatório simples com informações essenciais para análises de segurança.

📋 Funcionalidades

Leitura de arquivos de log no formato padrão do Linux (auth.log)

Detecção de tentativas de login com erro (Failed password)

Extração e contagem de IPs

Ordenação por número de tentativas (decrescente)

Geração de relatório com:

Data e hora da análise
Total de IPs únicos
Total de falhas
Lista de IPs com tentativas

🧠 Tecnologias utilizadas
Python 3.x

re (expressões regulares)

datetime (registro de data/hora)

🖥️ Exemplo de saída no terminal

RELATÓRIO DE FALHAS DE LOGIN
Gerado em: 08/04/2025 15:42:00
Total de IPs únicos: 3
Total de falhas: 7

Lista de IPs suspeitos:
192.168.1.10 – 4 tentativa(s)
10.0.0.5     – 2 tentativa(s)
172.16.0.1   – 1 tentativa(s)

🛠️ Como usar

1- Clone o repositório 
git clone https://github.com/seu-usuario/seu-repositorio.git
2- Salve ou copie seu arquivo de log no formato auth.log na mesma pasta do script.
3- Execute o script:
python analisador.py

📄 Licença
Este projeto está licenciado sob a MIT License.


