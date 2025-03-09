from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from escritor.tools.custom_tool import ExtratorPDF

@CrewBase
class Escritor():
    """Escritor crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # Inicializa a ferramenta de extração de PDF
    extrator_pdf = ExtratorPDF()

    @agent
    def leitor_pdf(self) -> Agent:
        return Agent(
            config=self.agents_config['leitor_pdf'],
            tools=[self.extrator_pdf],  
            verbose=True
        )

    @agent
    def analista_textual(self) -> Agent:
        return Agent(
            config=self.agents_config['analista_textual'],
            verbose=True
        )

    @agent
    def resumidor(self) -> Agent:
        return Agent(
            config=self.agents_config['resumidor'],
            verbose=True
        )

    @agent
    def formatador_blog(self) -> Agent:
        return Agent(
            config=self.agents_config['formatador_blog'],
            verbose=True
        )

    @task
    def ler_pdf(self) -> Task:
        return Task(
            config=self.tasks_config['ler_pdf'],
            tools=[self.extrator_pdf],  # Usa a ferramenta na tarefa
        )

    @task
    def analisar_texto(self) -> Task:
        return Task(
            config=self.tasks_config['analisar_texto'],
        )

    @task
    def resumir_texto(self) -> Task:
        return Task(
            config=self.tasks_config['resumir_texto'],
        )

    @task
    def escrever_post(self) -> Task:
        return Task(
            config=self.tasks_config['escrever_post'],
            output_file='post_final.md'
        )

    @crew
    def crew(self) -> Crew:
        """Cria o Crew de Escrita"""

        return Crew(
            agents=self.agents,  
            tasks=self.tasks,  
            process=Process.sequential,
            verbose=True,
        )