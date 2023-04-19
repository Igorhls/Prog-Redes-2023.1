import dpkt
import datetime

arq = "cap1.dump"

with open(arq, 'rb') as f:
    pcap = dpkt.pcap.Reader(f)

    inicia = None
    termina = None
    maior = 0
    incompleto_p = 0
    tamanho_p = 0
    total_p = 0

    for timestamp, buf in pcap:
        if inicia is None:
            inicia = datetime.datetime.fromtimestamp(timestamp)
        fim_p = datetime.datetime.fromtimestamp(timestamp)

        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data

        if len(buf) < ip.len:
            incompleto_p += 1

        if ip.len > maior:
            maior = ip.len

        tamanho_p += ip.len
        total_p += 1

    media_p = tamanho_p / total_p

    print("A captura de pacotes inicia em {0} e termina em {1}."
          "\nO maior pacote capturado é: {2}"
          "\nOs pacotes não salvos são: {3}"
          "\nA média dos tamanhos de pacotes é: {4}"
          .format(inicia,termina,maior,incompleto_p,media_p))
