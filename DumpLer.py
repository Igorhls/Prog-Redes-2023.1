# Igor Henrique

import dpkt
import datetime

arq = "cap1.dump"

with open(arq, 'rb') as f:
    pcap = dpkt.pcap.Reader(f)

    inicio_p = None
    fim_p = None
    maior_p = 0
    imcompleto_p = 0
    tamanho_p = 0
    total_p = 0

    for timestamp, buf in pcap:
        if inicio_p is None:
            inicio_p = datetime.datetime.fromtimestamp(timestamp)
        fim_p = datetime.datetime.fromtimestamp(timestamp)

        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data

        if len(buf) < ip.len:
            imcompleto_p += 1

        if ip.len > maior_p:
            maior_p = ip.len

        tamanho_p += ip.len
        total_p += 1

    media_p = tamanho_p / total_p

    print("Captura iniciada em:", inicio_p)
    print("Captura terminada em:", fim_p)
    print("Tamanho do maior pacote capturado:", maior_p)
    print("Número de pacotes capturados incompletos:", imcompleto_p)
    print("Tamanho médio dos pacotes capturados:", media_p
