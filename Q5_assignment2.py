from datetime import datetime

class Task:
    def __init__(self, task_name, task_description, due_date):
        self.task_name = task_name
        self.task_description = task_description
        self.due_date = due_date

    def status(self):
        current_date = datetime.now()
        if self.due_date > current_date:
            return "Pending"
        else:
            return "Completed"

class Homework(Task):
    def __init__(self, task_name, task_description, due_date, subject, task_status):
        super().__init__(task_name, task_description, due_date)
        self.subject = subject
        self.task_status = task_status

    def status(self):
        if self.task_status == "Not started":
            return "Not started"
        elif self.task_status == "In progress":
            return "In progress"
        else:
            return super().status()

class Meeting(Task):
    def __init__(self, task_name, task_description, due_date, location):
        super().__init__(task_name, task_description, due_date)
        self.location = location

    def status(self):
        current_date = datetime.now()
        if self.due_date > current_date:
            return "Scheduled"
        else:
            return "Happened"

# Example usage
homework_task = Homework("Math Homework", "Complete exercises 1-5", datetime(2024, 3, 15), "Math", "In progress")
meeting_task = Meeting("Team Meeting", "Discuss project updates", datetime(2024, 3, 12), "Conference Room")

print("Homework:")
print("Task Name:", homework_task.task_name)
print("Task Description:", homework_task.task_description)
print("Due Date:", homework_task.due_date)
print("Subject:", homework_task.subject)
print("Status:", homework_task.status())
print("\n")
print("Meeting:")
print("Task Name:", meeting_task.task_name)
print("Task Description:", meeting_task.task_description)
print("Due Date:", meeting_task.due_date)
print("Location:", meeting_task.location)
print("Status:", meeting_task.status())