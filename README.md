#Tasks Manager
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

##Запуск программы (RUN)
Создайте папку .env
```.env
DATABASE_URL=postgresql+asyncpg://postgres:123@localhost:5432/database
ACCESS_TOKEN_EXPIRE_DAYS=30
SECRET_KEY=supersecret
HESHALGORITHM=HS256
```

Создайте виртуальный окружение и загрузите зависимое библотеки и фреймворки
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

После запустите alembic
```bash
alembic upgrade head
```