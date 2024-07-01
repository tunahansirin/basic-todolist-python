from typing import List

# TaskValidator sınıfı, görevle ilgili bilgilerin doğruluğunu kontrol eder.
class TaskValidator:

    def __init__(self) -> None:
        pass
    
    # Görev adının istenilen kuralları sağlayıp sağlamadığını kontrol eden metot.
    def ValidateTaskName(self, taskName: str):
        if not taskName:
            raise ValueError("Görev adı boş olamaz")
        
        if len(taskName) < 3:
            raise ValueError("Görev adı en az 3 karakter uzunluğunda olmalıdır")
    
    # Görev sayısının istenilen kuralları sağlayıp sağlamadığını kontrol eden metot.
    def ValidateTaskCount(self, taskListCount: int):
        if taskListCount < 3:
            raise ValueError("En az 3 görev eklemelisiniz")
        
    # Görev adlarının birbirinden farklı olup olmadığını kontrol eden metot.
    def ValidateTaskUnique(self, taskList: List[str]):
        seen_tasks = set()
        for task in taskList:
            if task in seen_tasks:
                raise ValueError("Görev adları birbirinden farklı olmalıdır")
            seen_tasks.add(task)