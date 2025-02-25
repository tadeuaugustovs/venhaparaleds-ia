# Desafio IA - LEDS | Agentes Inteligentes para Leitura e Resumo de Documentos PDF
*Bem-vindo!* 👋

Neste desafio, você terá a oportunidade de demonstrar que possui as habilidades necessárias para atuar no time de IA do laboratório.

# Objetivo Geral

Desenvolver uma solução baseada em agentes utilizando o framework **CrewaI** para processar documentos em formato PDF. A solução deve gerar resumos dos documentos lidos e apresentar o conteúdo em um formato adequado para publicação em um blog.

# Contextualização

Você foi contratado para criar um sistema inteligente de leitura e resumo de documentos PDF. O objetivo é construir uma solução modular composta por diferentes agentes, cada um responsável por uma etapa do processo. O sistema final deve ser capaz de:

- Ler documentos PDF de forma eficiente.
- Gerar resumos curtos e informativos.
- Formatar o texto gerado no estilo de um post de blog.

## Tarefas

### 1. Configuração e Arquitetura de Agentes no CrewaI
Configure uma arquitetura de agentes no **CrewaI**, com papéis bem definidos para cada etapa do desafio:

- **Agente de Leitura de PDF:** Responsável por extrair o texto bruto do arquivo PDF.
- **Agente de Análise e Extração de Informação:** Identifica as informações mais importantes do texto.
- **Agente de Resumo:** Utiliza um modelo de linguagem (ex.: GPT) para criar resumos curtos e coerentes.
- **Agente de Formatação:** Formata o resumo no estilo de um post de blog, incluindo título, subtítulos e uma conclusão.

### 2. Implementação de Funções Específicas
Crie funções que permitam:

- Carregar múltiplos PDFs.
- Processar textos longos em seções.
- Garantir a coesão e fluidez do texto no resumo gerado.

### 3. Integração e Comunicação entre Agentes
Certifique-se de que os agentes se comuniquem eficientemente, passando os dados processados de um para o outro.

- Utilize **logs** ou **indicadores de progresso** para monitorar o desempenho dos agentes.

### 4. Geração do Blog Post Final
O blog deve conter:

- Um título relevante.
- Subtítulos que organizem o conteúdo.
- Texto coeso e formatado com clareza.

## Material Complementar
- [Multi-AI Agent Systems with CrewaI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/)
- [Practical Multi-AI Agents and Advanced Use Cases with CrewaI](https://www.deeplearning.ai/short-courses/practical-multi-ai-agents-and-advanced-use-cases-with-crewai/)
- [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- [Criando um Blog Writer Multi-Agent System com CrewaI e Ollama](https://medium.com/the-ai-forum/create-a-blog-writer-multi-agent-system-using-crewai-and-ollama-f47654a5e1cd)

# O que deve ser entregue?
- **Código fonte** do projeto.
- **Documentação breve** explicando a arquitetura do sistema e o papel de cada agente.
- **Exemplo de texto de blog** gerado a partir de pelo menos **3 documentos PDF**.

## Como entregar?
1. Faça um **fork** do repositório. Nesse fork esperamos encontrar uma documentação completa da solução e a listagem dos diferenciais implementados.
2. Abra um **pull request (PR)** do seu fork para o nome repositório com o seu nome como título. Assim conseguimos te localizar melhor e ver que você já finalizou o desafio!

## Critérios de Avaliação
- **Funcionalidade:** O sistema deve realizar todas as etapas descritas (**leitura, resumo e criação do blog**).
- **Qualidade do Resumo:** Os resumos devem ser **precisos** e capturar os pontos principais dos documentos.
- **Formatação do Blog:** O texto final deve estar **bem formatado** e ser adequado para publicação.
- **Código e Organização:** O código deve estar **bem organizado, modular e documentado**.

| Critério  | Valor | 
|---|---|
| Legibilidade do Código |  10  |
| Documentação do código |  10  |
| Documentação da solução |  10  |
| Tratamento de Erros | 10 | 
| Total | 40 |

## Diferenciais 
Você pode **aumentar sua pontuação** implementando os seguintes diferenciais:

| Item  | Pontos Ganhos | 
|---|---|
| Criar um [serviço](https://martinfowler.com/articles/microservices.html) com o problema |  30  |
| Implementar Clean Code |  20  |
| Implementar o padrão de programação da tecnologia escolhida |  20  |
| Qualidade de [Código com SonarQube](https://about.sonarcloud.io/) |  15  |
| Implementar integração com [Github Action](https://github.com/features/actions)  |  10  |
| Implementar integração com Github Action + SonarQube |  10  |
| Implementar usando Docker | 5 |
| Total| 120 |

A pontuação final será calculada somando os critérios obrigatórios e os diferenciais implementados corretamente.

# Penalizações

Você será desclassificado se:

1. Enviar uma solução que não funcione.
2. Não cumprir os critérios da seção **Avaliação**.
3. For identificado plágio.
   
***Que a força esteja com você. Boa sorte!***

<div align="left">
</div>

###

<br clear="both">

<div align="center">
  <a href="https://www.linkedin.com/school/ledsifes" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="40" alt="linkedin logo"  />
  </a>
  <a href="https://www.instagram.com/ledsifes/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="40" alt="instagram logo"  />
  </a>
  <a href="https://www.youtube.com/@ledsifes/?sub_confirmation=1" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Youtube&logo=youtube&label=&color=FF0000&logoColor=white&labelColor=&style=for-the-badge" height="40" alt="youtube logo"  />
  </a>
</div>

###