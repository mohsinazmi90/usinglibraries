import datetime


class Task:
    """
    Represents a single task object (Encapsulation).
    """

    def __init__(self, task_id: int, title: str, description: str):
        self.task_id = task_id
        self.title = title
        self.description = description

        self.is_completed = False
        self.created_at = datetime.datetime.now()

    def mark_complete(self):
        """
        Changes the internal state of the object.
        """
        self.is_completed = True

    def __str__(self):
        """
        Returns a string representation of the object.
        """

        status = "✓ Done" if self.is_completed else "⚬ Pending"

        return f"[{self.task_id}] {self.title} {status}\nDesc: {self.description}"


class TaskManager:
    """
    Manages the collection of tasks and exposes public behavior.
    """

    def __init__(self):

        # Private-Like attribute tracking task in additional
        self._task = {}

    def add_task(self, title: str, description: str) -> Task:
        """
        Creates a new task object and stores it.
        """
        task_id = len(self._task) + 1
        new_task = Task(task_id, title, description)
        self._task[task_id] = new_task
        print(f"Added task: {title},")
        return new_task

    def complete_task(self, task_id: int) -> bool:
        """
        Find a task by ID and mark it complete.
        """

        if task_id in self._task:
            self._task[task_id].mark_complete()
            print(f"Task #{task_id} marked as completed!")
            return True

        print(f"Error! Task # {task_id} not found")
        return False

    def list_tasks(self, include_completed=True):
        """
        It displays tasks depeneding on their status.
        """

        if not self._task:
            print("No task available.")
            return

        for task in self._task.values():
            if not include_completed and task.is_completed:
                continue
            print(task)
            print("---------------")

            # ---Execution \ App Lifecycle---


if __name__ == "__main__":
    # Initiate the application controller.
    app = TaskManager()

    # Add items, creates independing instances of task
    app.add_task("Buy groceries", "Milk, eggs, and freshly ground coffee beans")
    app.add_task("Finish OOP code", "Write Python snippet demonstrating encapsulation")

    # View pending status
    app.list_tasks()

    # Interact with indivdual object via the manager
    app.complete_task(1)

    # View updated status
    app.list_tasks()


# import datetime

# class Task:
#     """Represents a single task object (Encapsulation)."""

#     def __init__(self, task_id: int, title: str, description: str):
#         self.task_id = task_id
#         self.title = title
#         self.description = description
#         self.is_completed = False
#         self.created_at = datetime.datetime.now()

#     def mark_complete(self):
#         """Changes the internal state of the object."""
#         self.is_completed = True

#     def __str__(self):
#         """Returns a string representation of the object."""
#         status = "✓ Done" if self.is_completed else "⚬ Pending"
#         return f"[{self.task_id}] {self.title} ({status})\n    Desc: {self.description}"


# class TaskManager:
#     """Manages the collection of tasks and exposes public behaviors."""

#     def __init__(self):
#         # Private-like attribute tracking tasks in a dictionary
#         self._tasks = {}

#     def add_task(self, title: str, description: str) -> Task:
#         """Creates a new Task object and stores it."""
#         task_id = len(self._tasks) + 1
#         new_task = Task(task_id, title, description)
#         self._tasks[task_id] = new_task
#         print(f"Added task: '{title}'")
#         return new_task

#     def complete_task(self, task_id: int) -> bool:
#         """Finds a task by ID and marks it complete."""
#         if task_id in self._tasks:
#             self._tasks[task_id].mark_complete()
#             print(f"Task #{task_id} marked as complete!")
#             return True
#         print(f"Error: Task #{task_id} not found.")
#         return False

#     def list_tasks(self, include_completed=True):
#         """Iterates and displays tasks depending on their status."""
#         print("\n--- Current Task List ---")
#         if not self._tasks:
#             print("No tasks available.")
#             return

#         for task in self._tasks.values():
#             if not include_completed and task.is_completed:
#                 continue
#             print(task)
#         print("-------------------------\n")


# # --- Execution / App Lifecycle ---
# if __name__ == "__main__":
#     # Instantiate the application controller
#     app = TaskManager()

#     # Add items (Creates independent instances of Task)
#     app.add_task("Buy groceries", "Milk, eggs, and freshly ground coffee beans")
#     app.add_task("Finish OOP code", "Write Python snippet demonstrating encapsulation")

#     # View pending status
#     app.list_tasks()

#     # Interact with an individual object via the manager
#     app.complete_task(1)

#     # View updated status
#     app.list_tasks()
