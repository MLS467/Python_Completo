"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 50  # velocidade atual do carro
local_carro_1 = 101 # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega


velocidade_veiculo = velocidade > RADAR_1
veiculo_passou_local_1 = local_carro_1 >= (LOCAL_1 - RADAR_RANGE) and \
local_carro_1 <= (LOCAL_1+RADAR_RANGE)

veiculo_multado = veiculo_passou_local_1 and velocidade_veiculo

if velocidade_veiculo :
    print("Velocidade acima do permitido")

if veiculo_passou_local_1:
    print("veiculo Passou local 1")

if veiculo_multado:
   print('Carro multado em radar 1')