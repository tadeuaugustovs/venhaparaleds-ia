# Escritor IA - Projeto de Extração e Processamento de Textos

Este projeto foi desenvolvido para extrair e processar textos de arquivos PDF de forma eficiente, utilizando técnicas de Inteligência Artificial para análise e síntese de conteúdos.

## **Objetivo do Projeto**
O objetivo deste projeto é automatizar a extração de informações relevantes de documentos PDF e processá-los para facilitar sua análise e utilização em diferentes contextos.

## **Tecnologias Utilizadas**
- **Python** - Linguagem principal para desenvolvimento
- **CrewAI** - Framework para organização de tarefas com agentes de IA
- **PyPDF2** - Biblioteca para extração de texto de PDFs
- **LiteLLM** - Interface otimizada para chamadas de modelos OpenAI
- **Pydantic** - Validação de entrada de dados

## 🧠 **Arquitetura do Sistema**
O Escritor Crew é composto por agentes especialistas, cada um com um papel fundamental no processamento e transformação de conteúdo.

### 👨‍🏫 **Agentes Inteligentes**
Cada agente tem uma especialização e um papel bem definido dentro do fluxo de trabalho.

| Agente | Função |
|--------|--------|
| 🏛 **Leitor de PDF** | Doutor em Processamento de Linguagem Natural. Extrai o conteúdo dos arquivos PDF com precisão. |
| 📊 **Analista Textual** | Especialista em estruturação e organização de texto. Processa e melhora a legibilidade do conteúdo extraído. |
| ✍️ **Resumidor** | Profissional renomado em síntese de informações. Condensa os principais pontos do texto em um resumo claro e objetivo. |
| 📝 **Formatador de Blog** | Redator sênior especializado em escrita para web. Transforma o conteúdo em um post otimizado para SEO e engajamento. |

Cada agente colabora dentro de um fluxo de trabalho definido em `tasks.yaml`, garantindo uma automação eficiente.

## 🔍 **Detalhamento das Tarefas**
As tarefas são projetadas para maximizar a qualidade do texto gerado e garantir que cada etapa do processo ocorra com precisão.

| Tarefa | Descrição |
|--------|-----------|
| 📖 **ler_pdf** | Utiliza técnicas avançadas de extração de texto para recuperar informações de arquivos PDF. |
| 🔎 **analisar_texto** | Processa e estrutura o conteúdo, removendo ruídos e organizando informações-chave. |
| ✍️ **resumir_texto** | Cria um resumo conciso e objetivo, destacando os principais pontos do documento. |
| 📰 **escrever_post** | Formata o texto em um artigo de blog envolvente, otimizado para leitura e SEO. |

O fluxo de execução do Escritor Crew segue essa sequência, garantindo um resultado final refinado e pronto para publicação.

## **Estrutura do Projeto**
```
projeto_escrever_blog/
│── escritor/
│   ├── main.py                # Arquivo principal para execução do Crew
│   ├── custom_tool.py          # Código para extração de texto dos PDFs
│   ├── crew/                   # Módulo de gerenciamento de tarefas
│── README.md                   # Documentação do projeto
```

## **Como Executar o Projeto**
### **1️⃣ Configurar o Ambiente**
Antes de iniciar, certifique-se de instalar as dependências necessárias. No terminal, execute:
```bash
pip install -r requirements.txt
```

### **2️⃣ Executar a Extração e Processamento**
Para rodar o **Crew**, execute:
```bash
python -m escritor.main
```


### **3️⃣ Testar a Extração Manualmente**
Se desejar testar a extração de texto sem rodar o Crew, use:
```bash
python -c "from escritor.custom_tool import ExtratorPDF; print(ExtratorPDF()._run())"
```

## ⚙️ **Configuração**

### 🔑 **Defina a Chave de API da OpenAI**
Antes de executar o projeto, adicione sua API Key da OpenAI no arquivo `.env`, para que os agentes possam utilizar os modelos de IA.

### 📁 **Configuração dos Agentes e Tarefas**
Este projeto permite personalizar os agentes e tarefas de acordo com sua necessidade:

📌 **Definição dos agentes** → `src/escritor/config/agents.yaml`  
📌 **Definição das tarefas** → `src/escritor/config/tasks.yaml`  
📌 **Lógica e ferramentas personalizadas** → `src/escritor/crew.py`  
📌 **Entrada de dados e execuções customizadas** → `src/escritor/main.py`  


Os arquivos YAML podem ser modificados para definir novos agentes, ajustar parâmetros ou adicionar novas funcionalidades.

## **Otimizações Implementadas**
- **Redução do consumo de tokens** ao diminuir o tamanho dos trechos e o número máximo de trechos processados.
- **Organização das importações e modularização do código** para facilitar manutenção e extensibilidade.
