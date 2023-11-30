import matplotlib.pyplot as plt

# Defina todas as áreas e possíveis áreas com base nos cursos
areas = [
    "Cientista de Dados/Analista de Dados",
    "Cibersegurança",
    "Gestão Financeira de Empresas",
    "Desenvolvimento Seguro de Software",
    "Cloud Fundamentals, Administration and Solution Architect",
    "Linux Fundamentos",
    "Lógica de programação: mergulhe em programação com JavaScript",
    "Noções básicas de hardware de computador",
    "Noções básicas de sistemas operacionais",
    "Webinar como a ISO 27001 Acelera a Implantação de um SOC",
    "Webinar Defesa Cibernética: Gestão de Incidentes",
    "Business Intelligence (BI)",
    "Ciência de Dados",
    "DevOps & Culture",
    "Sergurança da Informação: Identificando Ataques Cybernéticos",
    "Front-End Design Essencial - HTML, CSS e JS Completo do Zero",
    "Desenvolvimento Web Full Stack com Python e Django",
    "Desenvolvimento Web Completo - 20 cursos + 20 projetos",
    "Outras Áreas",
    "Outros Tipos de Cursos"
]

# Defina as contagens de cursos em cada área
contagens = [7, 14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 6]

# Crie o gráfico de barras empilhadas
plt.figure(figsize=(12, 8))
bottom = [0] * len(areas)

for i, contagem in enumerate(contagens):
    plt.bar(areas[i], contagem, bottom=bottom[i])
    bottom[i] += contagem

# Configurações de rótulos e título
plt.xlabel('Áreas de Cursos')
plt.ylabel('Número de Cursos')
plt.title('Cursos por Área e Tipo')
plt.xticks(rotation=90)
plt.tight_layout()

# Exiba o gráfico
plt.show()
