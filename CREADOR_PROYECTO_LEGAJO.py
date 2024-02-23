# Importacion de librerias
import pandas as pd
import os

# Lectura
ot = pd.read_excel('Listado OT.xlsx')
empresas = ot[['Empresa','Sigla']].drop_duplicates(subset=['Sigla']).dropna().sort_values(by=['Empresa']).reset_index(drop=True)

# Interfaz de usuario
print(empresas)
a = input(f'La empresa se encuentra en el listado?\n')
if (a='si'):
    sigla = input(f'Ingrese las siglas de la empresa\n')
else:
    
## Ingrese empresa
## en este paso, previamente deberiamos mostrar el listado de empresas con su respectivo alias

## Ingrese nombre del proyecto

## para crear el legajo debe con el nombre correspondiente debe analizar el listado de legajos y ver cual es el maximo (ultimo legajo)
## Luego el nro de legajo a crear será (MAX+1)