import re
import datetime

ips = {}

with open("auth.log", "r") as log:

    for linha in log:

        if re.search(r"Failed password", linha):
            match = re.search(r"\d+\.\d+\.\d+\.\d+", linha)

            if match:
                ip = match.group()

                if ip in ips:
                    ips[ip] += 1
                else:
                    ips[ip] = 1

                data_hora = " ".join(linha.split()[0:3])

ip_ordenado = sorted(ips.items(), key=lambda item: item[1], reverse=True)

data_relatorio = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

total_falhas = sum(ips.values())

print("RELATÓRIO DE FALHAS DE LOGIN")
print(f" Gerado em: {data_relatorio}")
print(f"Total de IPs únicos: {len(ips)}")
print(f"Total de falhas: {total_falhas}\n")
print("Lista de IPs suspeitos: ")

for ip, tentativas in ip_ordenado:
    print(f"{ip} – {tentativas} tentativa(s)")



