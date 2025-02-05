# Desafio: Agentes Inteligentes para Leitura e Resumo de Documentos PDF

## Objetivo Geral
Desenvolver uma solução baseada em agentes utilizando o framework **CrewaI** para processar documentos em formato PDF. A solução deve gerar resumos dos documentos lidos e apresentar o conteúdo em um formato adequado para publicação em um blog.

## Descrição do Desafio
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

## Entrega
- **Código fonte** do projeto.
- **Documentação breve** explicando a arquitetura do sistema e o papel de cada agente.
- **Exemplo de texto de blog** gerado a partir de pelo menos **3 documentos PDF**.
- Para enviar o resultado, basta realizar um Fork deste repositório e abrir um Pull Request com seu nome.
  

## Critérios de Avaliação
- **Funcionalidade:** O sistema deve realizar todas as etapas descritas (**leitura, resumo e criação do blog**).
- **Qualidade do Resumo:** Os resumos devem ser **precisos** e capturar os pontos principais dos documentos.
- **Formatação do Blog:** O texto final deve estar **bem formatado** e ser adequado para publicação.
- **Código e Organização:** O código deve estar **bem organizado, modular e documentado**.
