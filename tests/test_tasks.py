from crew.tasks import (
    research_task,
    analysis_task,
    writing_task
)

print("\nTASKS CREATED SUCCESSFULLY\n")

print("Task 1:", research_task.description[:60])
print("Task 2:", analysis_task.description[:60])
print("Task 3:", writing_task.description[:60])
