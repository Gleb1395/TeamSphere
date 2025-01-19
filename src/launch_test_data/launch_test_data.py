from project.models import Project, Team
from task.models import Task
from worker.models import Worker


def launch_test_data(
    worker: int,
    project: int,
    team: int,
    task: int,
) -> None:
    print("Launching test data: starting...")  # TODO delete all prints
    Worker.create_test_worker(worker)
    print("Worker: done.")
    Project.create_test_project(project)
    print("Project: done.")
    Team.create_test_team(team)
    print("Team: done.")
    Task.create_test_task(task)
    print("Task: done.")
    print("Launching test data: done.")
