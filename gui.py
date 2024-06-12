import tkinter as tk
from tkinter import messagebox, simpledialog
from logic import (
    process_request, get_all_requests, edit_request, delete_request, 
    mark_request_as_completed, count_completed_requests, calculate_average_completion_time
)

def run_app():
    """
    Инициализирует и запускает приложение для учета заявок на ремонт оборудования.
    """
    # Создание главного окна приложения
    root = tk.Tk()
    root.title("Учет заявок на ремонт оборудования")
    
    # Создание и размещение виджетов
    label = tk.Label(root, text="Введите данные заявки")
    label.pack()
    
    entry = tk.Entry(root)
    entry.pack()
    
    result_label = tk.Label(root, text="")
    result_label.pack()

    # Функции-обработчики для кнопок
    def on_submit():
        """
        Обрабатывает добавление новой заявки.
        """
        data = entry.get()
        result = process_request(data)
        result_label.config(text=result)

    def on_view_requests():
        """
        Отображает все заявки в всплывающем окне.
        """
        requests = get_all_requests()
        messagebox.showinfo("Все заявки", "\n".join(requests))

    def on_edit_request():
        """
        Запрашивает ID и новые данные заявки и обновляет её.
        """
        request_id = simpledialog.askinteger("Редактировать заявку", "Введите ID заявки:")
        new_data = simpledialog.askstring("Редактировать заявку", "Введите новые данные заявки:")
        if request_id and new_data:
            result = edit_request(request_id, new_data)
            messagebox.showinfo("Результат", result)

    def on_delete_request():
        """
        Запрашивает ID заявки и удаляет её.
        """
        request_id = simpledialog.askinteger("Удалить заявку", "Введите ID заявки:")
        if request_id:
            result = delete_request(request_id)
            messagebox.showinfo("Результат", result)

    def on_complete_request():
        """
        Запрашивает ID заявки и помечает её как выполненную.
        """
        request_id = simpledialog.askinteger("Завершить заявку", "Введите ID заявки:")
        if request_id:
            result = mark_request_as_completed(request_id)
            messagebox.showinfo("Результат", result)

    def on_count_completed_requests():
        """
        Отображает количество выполненных заявок.
        """
        count = count_completed_requests()
        messagebox.showinfo("Количество выполненных заявок", f"Всего выполненных заявок: {count}")

    def on_average_completion_time():
        """
        Отображает среднее время выполнения заявок.
        """
        average_time = calculate_average_completion_time()
        messagebox.showinfo("Среднее время выполнения заявок", average_time)

    # Создание кнопок и их размещение
    button_submit = tk.Button(root, text="Отправить", command=on_submit)
    button_submit.pack()

    button_view = tk.Button(root, text="Посмотреть заявки", command=on_view_requests)
    button_view.pack()
    
    button_edit = tk.Button(root, text="Редактировать заявку", command=on_edit_request)
    button_edit.pack()

    button_delete = tk.Button(root, text="Удалить заявку", command=on_delete_request)
    button_delete.pack()

    button_complete = tk.Button(root, text="Завершить заявку", command=on_complete_request)
    button_complete.pack()

    button_count_completed = tk.Button(root, text="Количество выполненных заявок", command=on_count_completed_requests)
    button_count_completed.pack()
    
    button_average_time = tk.Button(root, text="Среднее время выполнения заявок", command=on_average_completion_time)
    button_average_time.pack()
    
    # Запуск главного цикла обработки событий
    root.mainloop()

# Запуск приложения, если скрипт запущен напрямую
if __name__ == "__main__":
    run_app()
