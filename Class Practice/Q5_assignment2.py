from datetime import datetime
from dataclasses import dataclass


@dataclass
class Task:
    """
    A class to represent a task being
    done by a student or for a meeting.
    """
    task_name: str
    task_description: str
    due_date: datetime

    @property
    def status(self):
        """
        Returns the status of the task at hand.
        :return:
        """
        current_date = datetime.now()
        if self.due_date > current_date:
            return "Pending"
        else:
            return "Completed"


@dataclass
class Homework(Task):
    """
    A class to represent a task being done by a student,
    inheriting from Task class.
    """
    subject: str
    task_status: str

    @property
    def status(self):
        """
        Returns the status of the task being
        done or completed by the student individually.
        :return:
        """
        if self.task_status == "Not started":
            return "Not started"
        elif self.task_status == "In progress":
            return "In progress"
        else:
            return super().status


@dataclass
class Meeting(Task):
    """
    A class to represent a task being done by someone involved with a meeting.
    Inheriting from Task class.
    """
    location: str

    @property
    def status(self):
        """
        Returns the status of the task being
        done or completed by someone that has a meeting.
        :return:
        """
        current_date = datetime.now()
        if self.due_date > current_date:
            return "Scheduled"
        else:
            return "Happened"


# Example usage for the code with random information.

homework_task = Homework("Math Homework", "Complete exercises 1-5", datetime(2024, 3, 15), "Math", "In progress")
meeting_task = Meeting("Team Meeting", "Discuss project updates", datetime(2024, 3, 12), "Conference Room")

# Print statement for the homework done by a student.

print("Homework:")
print("Task Name:", homework_task.task_name)
print("Task Description:", homework_task.task_description)
print("Due Date:", homework_task.due_date)
print("Subject:", homework_task.subject)
print("Status:", homework_task.status)
print()

# Print statements for the meeting.

print("Meeting:")
print("Task Name:", meeting_task.task_name)
print("Task Description:", meeting_task.task_description)
print("Due Date:", meeting_task.due_date)
print("Location:", meeting_task.location)
print("Status:", meeting_task.status)
print()