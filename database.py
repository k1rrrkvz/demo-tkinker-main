import mysql.connector
from datetime import datetime

import mysql.connector

def create_connection():
    """
    Создает и возвращает соединение с базой данных MySQL.

    Возвращает:
        conn (mysql.connector.connection.MySQLConnection): Объект соединения с базой данных.
    
    Для повышения безопасности:
        - Используйте шифрование (SSL) для защиты данных при передаче.
        - Избегайте использования учетных записей с привилегиями администратора для приложений.
        - Храните учетные данные (имя пользователя и пароль) в защищенном виде, например, в переменных окружения или в менеджере секретов.
    """
    conn = mysql.connector.connect(
        host="",  # Адрес сервера базы данных. Например, "localhost" или "127.0.0.1".
        user="",  # Имя пользователя для подключения к базе данных.
        password="",  # Пароль для подключения к базе данных.
        database="",  # Название базы данных, к которой нужно подключиться.
      #  ssl_ca="/path/to/ca-cert.pem",  # Путь к файлу сертификата CA для проверки подлинности сервера.
      #  ssl_cert="/path/to/client-cert.pem",  # Путь к клиентскому сертификату (если требуется).
      # ssl_key="/path/to/client-key.pem"  # Путь к закрытому ключу клиента (если требуется).
    )
    return conn


def create_table():
    """
    Создает таблицу requests, если она не существует.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS requests (
                         id INT AUTO_INCREMENT PRIMARY KEY,
                         data TEXT NOT NULL,
                         created_at DATETIME NOT NULL,
                         completed_at DATETIME
                      )''')
    conn.commit()
    conn.close()

def add_request(data):
    """
    Добавляет новую заявку в таблицу requests.
    
    Args:
        data (str): Данные заявки.
    """
    conn = create_connection()
    cursor = conn.cursor()
    created_at = datetime.now().isoformat()
    cursor.execute("INSERT INTO requests (data, created_at) VALUES (%s, %s)", (data, created_at))
    conn.commit()
    conn.close()

def fetch_requests():
    """
    Извлекает все заявки из таблицы requests.
    
    Returns:
        list: Список всех заявок.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, data, created_at, completed_at FROM requests")
    requests = cursor.fetchall()
    conn.close()
    return requests

def update_request(request_id, new_data):
    """
    Обновляет данные конкретной заявки.
    
    Args:
        request_id (int): ID заявки.
        new_data (str): Новые данные для заявки.
    
    Returns:
        bool: True, если обновление прошло успешно, иначе False.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE requests SET data = %s WHERE id = %s", (new_data, request_id))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated > 0

def complete_request(request_id):
    """
    Помечает заявку как выполненную, устанавливая дату выполнения.
    
    Args:
        request_id (int): ID заявки.
    
    Returns:
        bool: True, если обновление прошло успешно, иначе False.
    """
    conn = create_connection()
    cursor = conn.cursor()
    completed_at = datetime.now().isoformat()
    cursor.execute("UPDATE requests SET completed_at = %s WHERE id = %s", (completed_at, request_id))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated > 0

def remove_request(request_id):
    """
    Удаляет заявку из таблицы requests.
    
    Args:
        request_id (int): ID заявки.
    
    Returns:
        bool: True, если удаление прошло успешно, иначе False.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM requests WHERE id = %s", (request_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted > 0

def fetch_completed_requests():
    """
    Извлекает все выполненные заявки из таблицы requests.
    
    Returns:
        list: Список выполненных заявок.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, data, created_at, completed_at FROM requests WHERE completed_at IS NOT NULL")
    requests = cursor.fetchall()
    conn.close()
    return requests
