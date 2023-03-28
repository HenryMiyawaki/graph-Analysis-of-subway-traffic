# Create JSON dataset of metro and train

Status: Done

[station.json](Create%20JSON%20dataset%20of%20metro%20and%20train%205a17d85cf3b8443bbffa1d67500facba/station.json)

## Following

> When working with graphs, the adjacency matrix is a crucial tool for representing the graph mathematically. The adjacency matrix is a square matrix where the rows and columns represent the vertices of the graph, and the entries indicate whether there is an edge connecting the corresponding vertices.
> 
> 
> To create the adjacency matrix, we need to have a clear understanding of the graph's structure and connectivity. Hence, the dataset used to generate the adjacency matrix must follow some specific rules. For instance, the dataset must contain information about the vertices and edges of the graph, including their labels and properties.
> 

- There are two main keys, and you can name them whatever you like. The keys' names are not fixed and can be easily accessed and altered in the code using a dictionary.
    - The first key identified in the example, named "Linha," represents the name of the line and contains all the stations associated with that particular line.
    - The second key is an array that contains objects representing the stations. Each object contains variables that provide information about the station and its connections to other stations, including integration points. These variables help to identify the station and its properties within the overall transportation system.
- Another rule to keep in mind when working with this the dataset is that the order of the elements in the array matters. If you place "Station 1" before "Station 2" in the array, the dataset is telling us that "Station 1" comes before "Station 2" in the sequence of stations along the line. Therefore, the order of the stations in the array affects the formation of the adjacency matrix and the overall representation of the graph.
- Inside the object that represents a station in the array, there are typically three keys that provide important information about the station:
    - The name of the Station
    - Where is the address
    - If a station does not have any integration points or connections with other stations or lines, you can represent it with a null value or simply with double quotes: "". This indicates that the station has no connections or integrations with other parts of the transportation system. It is important to represent such stations accurately in the dataset, as they can affect the formation of the adjacency matrix and the overall representation of the graph.

## Code example

```json
[
{
        "Linha": "Linha 1-Azul",
        "Estacoes": [
            {
                "Estação": "Estação Tucuruvi",
                "Endereço": "Av. Dr. Antonio Maria Laet, 100 – Tucuruvi",
                "Integração": ""
            },
            {
                "Estação": "Estação Parada Inglesa",
                "Endereço": "Av. Luiz Dumont Villares, 1721 – Parada Inglesa",
                "Integração": ""
            },
            {
                "Estação": "Estação Jardim São Paulo – Ayrton Senna",
                "Endereço": "Av. Leôncio de Magalhães, 1000 – Jardim São Paulo",
                "Integração": ""
            },
            {
                "Estação": "Estação Santana",
                "Endereço": "Avenida Cruzeiro do Sul, 3173",
                "Integração": ""
            },
            {
                "Estação": "Estação Carandiru",
                "Endereço": "Av. Cruzeiro do Sul, 2487 – Santana",
                "Integração": ""
            },
            {
                "Estação": "Estação Portuguesa – Tietê",
                "Endereço": "Av. Cruzeiro do Sul, 1777 – Santana",
                "Integração": ""
            },
            {
              "Estação": "Estação Armênia",
              "Endereço": "Rua Pedro Vicente, 47 – Bom Retiro",
              "Integração": ""
            },
            {
                "Estação": "Estação Tiradentes",
                "Endereço": "Av. Tiradentes, 551 – Bom Retiro",
                "Integração": ""
            },
            {
                "Estação": "Estação Luz",
                "Endereço": "Av. Prestes Maia, 925 – Luz",
                "Integração": "Linha 4-Amarela,Linha 7-Rubi,Linha 11-Coral"
            },
            {
                "Estação": "Estação São Bento",
                "Endereço": "Largo São Bento,109",
                "Integração": ""
            },
            {
                "Estação": "Estação Sé",
                "Endereço": "Praça da Sé , s/nº",
                "Integração": "Linha 3- Vermelha"
            },
            {
                "Estação": "Estação Liberdade",
                "Endereço": "Praça da Liberdade, 133 – Liberdade",
                "Integração": ""
            },
            {
                "Estação": "Estação São Joaquim",
                "Endereço": "Av. Liberdade, 1033, Liberdade",
                "Integração": ""
            },
            {
                "Estação": "Estação Vergueiro",
                "Endereço": "Rua Vergueiro, 790",
                "Integração": ""
            },
            {
                "Estação": "Estação Paraíso",
                "Endereço": "Rua Vergueiro, 1465 – Paraíso",
                "Integração": "Linha 2-Verde"
            },
            {
                "Estação": "Estação Ana Rosa",
                "Endereço": "Rua Vergueiro, 505 – Vila Mariana",
                "Integração": "Linha 2-Verde"
            },
            {
                "Estação": "Estação Vila Mariana",
                "Endereço": "Av. Profº. Noé Azevedo, 255",
                "Integração": ""
            },
            {
                "Estação": "Estação Santa Cruz",
                "Endereço": "Rua Domingos de Morais, 2564, Vila Mariana",
                "Integração": "Linha 5-Lilás"
            },
            {
              "Estação": "Estação Praça da Árvore",
              "Endereço": "Praça da Árvore, 39 – Praça da Árvore",
              "Integração": ""
            },
            {
                "Estação": "Estação Saúde",
                "Endereço": "Avenida Jabaquara, 1634",
                "Integração": ""
            },
            {
                "Estação": "Estação São Judas",
                "Endereço": "Avenida Jabaquara, 2438",
                "Integração": ""
            },
            {
                "Estação": "Estação Conceição",
                "Endereço": "Avenida Engº. Armando de Arruda Pereira, 919",
                "Integração": ""
            },
            {
                "Estação": "Estação Jabaquara",
                "Endereço": "Rua dos Jequitibás, 80 – Jabaquara",
                "Integração": ""
            }
           ]
    },
]
```