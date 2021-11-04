import os
import pandas as pd
import time

inputdf = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(inputdf)

montadoras = df['make'].unique()
try:
    for mont in montadoras: 
        if mont == "alfa-romero":
            dfmont = df[(df.make == "alfa-romero")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\alfa-romero.xlsx", index=True)
        if mont == "audi":
            dfmont = df[(df.make == "audi")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\audi.xlsx", index=True)
        if mont == "bmw":
            dfmont = df[(df.make == "bmw")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\bmw.xlsx", index=True)
        if mont == "chevrolet":
            dfmont = df[(df.make == "chevrolet")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\chevrolet.xlsx", index=True)
        if mont == "dodge":
            dfmont = df[(df.make == "dodge")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\dodge.xlsx", index=True)
        if mont == "honda":
            dfmont = df[(df.make == "honda")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\honda.xlsx", index=True)
        if mont == "isuzu":
            dfmont = df[(df.make == "isuzu")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\isuzu.xlsx", index=True)
        if mont == "jaguar":
            dfmont = df[(df.make == "jaguar")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\jaguar.xlsx", index=True)
        if mont == "mazda":
            dfmont = df[(df.make == "mazda")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\mazda.xlsx", index=True)
        if mont == "mercedes-benz":
            dfmont = df[(df.make == "mercedes-benz")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\mercedes-benz.xlsx", index=True)
        if mont == "mitsubishi":
            dfmont = df[(df.make == "mitsubishi")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\mitsubishi.xlsx", index=True)
        if mont == "nissan":
            dfmont = df[(df.make == "nissan")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\nissan.xlsx", index=True)
        if mont == "peugot":
            dfmont = df[(df.make == "peugot")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\peugot.xlsx", index=True)
        if mont == "plymouth":
            dfmont = df[(df.make == "plymouth")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\plymouth.xlsx", index=True)
        if mont == "porsche":
            dfmont = df[(df.make == "porsche")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\porsche.xlsx", index=True)
        if mont == "renault":
            dfmont = df[(df.make == "renault")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\renault.xlsx", index=True)
        if mont == "saab":
            dfmont = df[(df.make == "saab")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\saab.xlsx", index=True)
        if mont == "subaru":
            dfmont = df[(df.make == "subaru")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\subaru.xlsx", index=True)
        if mont == "toyota":
            dfmont = df[(df.make == "toyota")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\toyota.xlsx", index=True)
        if mont == "volkswagen":
            dfmont = df[(df.make == "volkswagen")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\volkswagen.xlsx", index=True)
        if mont == "volvo":
            dfmont = df[(df.make == "volvo")]
            dfmont.to_excel(r"I:\Documentos\Programacao\Projetos de Python\Montadoras\volvo.xlsx", index=True)
    print('Relatório gerados!')
except Exception as e:
    print(f'Erro apresentado: \n{e}')
