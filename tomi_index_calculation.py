import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
from sklearn.impute import SimpleImputer

plt.style.use(["bmh"])

file_name = "./tests/@CN_OGX-101.xlsx"

# Carrega os dados do arquivo Excel
dataframe = pd.read_excel(file_name, skiprows=0, decimal=",", sheet_name="LONGÁ")

# Dados dos pontos-chave de probabilidade do artigo
TOC_TN_ARTIGO = np.array([4, 4, 4, 4, 10, 10, 10, 10, 100, 100, 100, 100])
C13CORG_ARTIGO = np.array([-10, -22, -25, -34, -10, -22, -25, -34, -10, -22, -25, -34])
D15N_ARTIGO = np.array([12, 3, 0, -12, 12, 3, 0, -12, 12, 3, 0, -12])
PROBABILIDADE = np.array([0, 10, 20, 30, 20, 30, 40, 50, 90, 95, 98, 100])

# Extrai os dados das amostras do dataframe
amostra_TOC_TN = dataframe["TOC/TN"].values
amostra_C13CORG = dataframe["d13C"].values
amostra_D15N = dataframe["d15N"].values

# Combina os dados do artigo em uma matriz
DADOS_ARTIGO = np.column_stack((TOC_TN_ARTIGO, C13CORG_ARTIGO, D15N_ARTIGO))
TOMI_PROBABILIDADE = PROBABILIDADE

# Define o kernel para o GaussianProcessRegressor
kernel = C(1.0, (1e-3, 1e3)) * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2))

# Inicializa o GaussianProcessRegressor com o kernel definido
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
# Treina o modelo com os dados do artigo
gp.fit(DADOS_ARTIGO, TOMI_PROBABILIDADE)

# Combina os dados das amostras em uma matriz
DADOS_AMOSTRA = np.column_stack((amostra_TOC_TN, amostra_C13CORG, amostra_D15N))
# Imputa valores faltantes usando a média
imputer = SimpleImputer(strategy="mean")
DADOS_AMOSTRA = imputer.fit_transform(DADOS_AMOSTRA)

# Prediz o índice TOMI com os dados imputados
TOMI_INDEX, sigma = gp.predict(DADOS_AMOSTRA, return_std=True)
# Ajusta o índice TOMI
TOMI_INDEX = 100 - TOMI_INDEX

# Plota os dados
plt.figure(figsize=(5, 8))
plt.plot(TOMI_INDEX, dataframe["TVDSS"], "s-")
plt.xlim(0, 100)
plt.title("TOMI Index", fontsize=14)
plt.xlabel("Índice (%)", fontsize=12)
plt.grid(True)
plt.show()
