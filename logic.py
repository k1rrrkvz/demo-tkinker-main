from database import create_table, add_request, fetch_requests, update_request, remove_request, complete_request, fetch_completed_requests
from datetime import datetime

# Создание таблицы в базе данных
create_table()

def process_request(data):
    """
    Обрабатывает добавление новой заявки.
    
    Args:
        data (str): Данные заявки.
    
    Returns:
        str: Сообщение о результате добавления заявки.
    """
    if data == "":
        return "Ошибка: данные заявки не должны быть пустыми"
    add_request(data)
    return f"Заявка '{data}' добавлена в базу данных"

def get_all_requests():
    """
    Извлекает и форматирует все заявки из базы данных.
    
    Returns:
        list: Список заявок или сообщение о том, что заявок нет.
    """
    requests = fetch_requests()
    if not requests:
        return ["Нет заявок"]
    return [f"Заявка {request[0]}: {request[1]} (Создана: {request[2]}, Завершена: {request[3]})" for request in requests]

def edit_request(request_id, new_data):
    """
    Обновляет данные существующей заявки.
    
    Args:
        request_id (int): ID заявки.
        new_data (str): Новые данные для заявки.
    
    Returns:
        str: Сообщение о результате обновления заявки.
    """
    updated = update_request(request_id, new_data)
    if updated:
        return f"Заявка {request_id} успешно обновлена"
    return f"Заявка с ID {request_id} не найдена"

def delete_request(request_id):
    """
    Удаляет заявку из базы данных.
    
    Args:
        request_id (int): ID заявки.
    
    Returns:
        str: Сообщение о результате удаления заявки.
    """
    deleted = remove_request(request_id)
    if deleted:
        return f"Заявка {request_id} успешно удалена"
    return f"Заявка с ID {request_id} не найдена"

def mark_request_as_completed(request_id):
    """
    Помечает заявку как выполненную.
    
    Args:
        request_id (int): ID заявки.
    
    Returns:
        str: Сообщение о результате выполнения заявки.
    """
    completed = complete_request(request_id)
    if completed:
        return f"Заявка {request_id} отмечена как выполненная"
    return f"Заявка с ID {request_id} не найдена"

def count_completed_requests():
    """
    Подсчитывает количество выполненных заявок.
    
    Returns:
        int: Количество выполненных заявок.
    """
    requests = fetch_completed_requests()
    return len(requests)

def calculate_average_completion_time():
    """
    Вычисляет среднее время выполнения заявок.
    
    Returns:
        str: Сообщение со средним временем выполнения заявок.
    """
    requests = fetch_completed_requests()
    if not requests:
        return "Нет выполненных заявок"
    
    total_time = 0
    count = 0
    for request in requests:
        created_at = request[2]
        completed_at = request[3]
        total_time += (completed_at - created_at).total_seconds()
        count += 1
    
    average_time = total_time / count if count > 0 else 0
    return f"Среднее время выполнения заявки: {average_time / 60:.2f} минут"
