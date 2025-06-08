##Архитектура проекта

.env Нужно добавить самому
```architecture
tasks/
     /main.py     # Точка входа
     /config.py   # Конфигурация
     /.env        # Данные для конфигураций
     /routers/    # Controller
             /auth.py     # Регистрация и авторизация
             /create_tasks.py # Добавляет задач
             /tasks_edit.py   # Изменения задач
             /tasks_search.py # Пойск данных
     /models/     # Model: ORM, Pydantic, CRUD
     		/tables.py     # SQLAlchemy модели
            /schemas.py    # Pydantic-схемы
            /crud.py       # CRUD-операции
            /view_datas.py # Читает данные
     /views/      # View
     	   /user_view.py
     /utils/      # Утилиты (отдельные задачи, фоновые проверки)
           /check_due_date.py # Проверка просрочки
     /service/    # Service layer / общая логика
     		/auth.py			 # Проверка пользвателья по JWT
     		/JWT.py 			 # Генерация и обратно
     		/password_hashing.py # Хэширование и проверка пароля
     /database.py # Подключение к БД
```