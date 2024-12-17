import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ModelBot:
    """ModelBot crew"""

    # File paths for YAML configurations
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../config"))
    agents_config = os.path.join(base_dir, "agents")
    tasks_config = os.path.join(base_dir, "tasks")
    shared_config = os.path.join(base_dir, "shared_config.yaml")
    process_config = os.path.join(base_dir, "processes/sequential_process.yaml")

    # Define agents
    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config=os.path.join(self.agents_config, "project_manager_agents.yaml"),
            verbose=True
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=os.path.join(self.agents_config, "research_agents.yaml"),
            verbose=True
        )

    @agent
    def qa_agent(self) -> Agent:
        return Agent(
            config=os.path.join(self.agents_config, "quality_assurance_agents.yaml"),
            verbose=True
        )

    # Define tasks
    @task
    def clarification_task(self) -> Task:
        return Task(
            config=os.path.join(self.tasks_config, "project_manager_tasks.yaml"),
        )

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=os.path.join(self.tasks_config, "research_tasks.yaml"),
        )

    @task
    def qa_review_task(self) -> Task:
        return Task(
            config=os.path.join(self.tasks_config, "quality_assurance_tasks.yaml"),
            output_file="qa_review.md",
        )

    # Define the crew
    @crew
    def crew(self) -> Crew:
        """Creates the ModelBot crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by @task decorators
            process=Process.sequential,  # Default process
            verbose=True,
        )
