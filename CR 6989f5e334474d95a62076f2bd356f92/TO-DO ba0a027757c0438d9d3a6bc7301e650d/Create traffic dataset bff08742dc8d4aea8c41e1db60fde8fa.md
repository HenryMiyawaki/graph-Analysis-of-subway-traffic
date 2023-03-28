# Create traffic dataset

Status: Done

## Creation of the traffic dataset

There are 4 data sources to obtain the data of subway and train passagers transportation.

Our sources contains:

- Transported passagers by sao paulo subway: [(link)](https://transparencia.metrosp.com.br/dataset/demanda)
- Transported passagers by ViaQuatro: [(link)](https://www.viaquatro.com.br/linha-4-amarela/passageiros-transportados)
- Transported passagers by ViaMobilidade: [(link)](https://www.viamobilidade.com.br/nos/passageiros-transportados)
- Transported passagers by CPTM: [(link)](https://www.cptm.sp.gov.br/negocios/Pages/Movimentacao-de-Passageiros.aspx?RootFolder=%2Fnegocios%2FMovimentao%20de%20Passageiros%2F2022&FolderCTID=0x0120001B071DE8D9072049B0F9B0E2E77B902E&View=%7B23EF9C34-E382-4D73-84B5-A63047037BE4%7D)

It can be noticed that the data from Sao Paulo subway is organized by passagers per utility days of 2022 for each station.

Meanwhile, the data from CPTM are provided just for the months (JAN, FEB, APR, MAY, SEP and OCT), so it'll be required to divide them by 30 to get each day approximately, then, calculate the average for the year, we can see it in the image below:

![Untitled](Create%20traffic%20dataset%20bff08742dc8d4aea8c41e1db60fde8fa/Untitled.png)

For the ViaMobilidade data, we needed a different approach, their data are organized by passagers per utility days monthly, so that means we need to calculate the avarege in the year of 2022. 

Note: The lines 8 and 9 was owned by CPTM, then the data for january was in their pattern, even though, the average wasn’t hardly affected.
And for ViaQuarto that has only the line 4 was also needed to calculate an avarage, but in this case we have all months of the 2022 year.

![Untitled](Create%20traffic%20dataset%20bff08742dc8d4aea8c41e1db60fde8fa/Untitled%201.png)

![Untitled](Create%20traffic%20dataset%20bff08742dc8d4aea8c41e1db60fde8fa/Untitled%202.png)

With all the data normalized we can make a json that has this pattern:

```
[
	{
    "Linha": "Linha 1-Azul",
    "Estacoes": [
      {
        "Estação": "Estação Jabaquara",
        "Passageiros": {
          "Média Diária": 64
        }
      }
		]
	},
	{
    "Linha": "Linha 5-Lilás",
    "Estacoes": [
      {
        "Estacao": "Estação Capão Redondo",
        "Passageiros": {
          "Média Diária": 84
        }
      }
		]
	}
]
```