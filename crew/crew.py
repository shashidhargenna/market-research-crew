from crewai import Crew, Process

from config.config import manager_llm

from crew.agents import (
    researcher,
    analyst,
    writer
)

from crew.tasks import (
    research_task,
    analysis_task,
    writing_task
)


market_research_crew = Crew(

    agents=[
        researcher,
        analyst,
        writer
    ],

    tasks=[
        research_task,
        analysis_task,
        writing_task
    ],

    process=Process.hierarchical,

    manager_llm=manager_llm,

    verbose=True
)


def run_market_research(inputs):

    result = market_research_crew.kickoff(
        inputs=inputs
    )

    print("\n========== INDIVIDUAL TASK OUTPUTS ==========\n")

    tasks = [
        ("RESEARCH TASK", research_task),
        ("ANALYSIS TASK", analysis_task),
        ("WRITING TASK", writing_task)
    ]

    for task_name, task in tasks:

        print(f"\n========== {task_name} ==========\n")

        if task.output:
            print(task.output.raw)
        else:
            print("No output generated for this task.")

    print("\n========== FINAL MANAGER OUTPUT ==========\n")

    print(result.raw)

    return result

