class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        """Добавление новой задачи."""
        task = {
            'description': description,
            'deadline': deadline,
            'completed': False
        }
        self.tasks.append(task)
        print(f"Задача добавлена: {description}")

    def mark_completed(self, description):
        """Отметка задачи как выполненной."""
        for task in self.tasks:
            if task['description'] == description:
                task['completed'] = True
                print(f"Задача '{description}' ✅ отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена.")

    def show_current_tasks(self):
        """Вывод списка текущих (не выполненных) задач."""
        current_tasks = [task for task in self.tasks if not task['completed']]
        if current_tasks:
            print("Текущие задачи:")
            for task in current_tasks:
                print(f"- {task['description']} (Срок: {task['deadline']})")
        else:
            print("Нет текущих задач.")

# Пример использования класса Task
if __name__ == "__main__":
    task_manager = Task()
    task_manager.add_task("Купить продукты", "2025-04-12")
    task_manager.add_task("Помыть машину", "2025-04-15")
    task_manager.show_current_tasks()
    task_manager.mark_completed("Купить продукты")
    task_manager.show_current_tasks()