# tg bot
# Руководство по работе с Git и GitHub

## 🚀 Основные команды и порядок действий

### 1. Первоначальная настройка

**Установка Git:**
```bash
# Для Windows: скачайте с git-scm.com
# Для Linux:
sudo apt-get install git
# Для macOS:
brew install git
```

**Настройка пользователя:**
```bash
git config --global user.name "Ваше Имя"
git config --global user.email "ваш.email@example.com"
```

### 2. Создание репозитория и первый коммит

```bash
# Инициализация репозитория
git init

# Добавление файлов
git add .

# Создание коммита
git commit -m "Initial commit: базовая структура проекта"

# Добавление удаленного репозитория
git remote add origin https://github.com/username/repository-name.git

# Отправка кода на GitHub
git push -u origin main
```

### 3. Основной рабочий процесс

**Перед началом работы:**
```bash
# Получить последние изменения
git pull origin main
```

**В процессе работы:**
```bash
# Проверить статус
git status

# Посмотреть изменения
git diff

# Добавить файлы
git add filename.py

# Создать коммит
git commit -m "Описание изменений"

# Отправить изменения
git push origin main
```

### 4. Полезные команды

**Просмотр истории:**
```bash
git log
git log --oneline
git log --graph --oneline
```

**Отмена изменений:**
```bash
# Отменить изменения в файле
git checkout -- filename.py

# Отменить добавление файла
git reset filename.py

# Отменить последний коммит
git reset --soft HEAD~1
```

**Работа с ветками:**
```bash
# Создать новую ветку
git branch feature-name

# Переключиться на ветку
git checkout feature-name

# Создать и переключиться
git checkout -b feature-name

# Слить ветки
git checkout main
git merge feature-name

# Удалить ветку
git branch -d feature-name
```

### 5. Файл .gitignore

Создайте файл `.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# Sensitive data
.env
*.env
secrets.py
config.py

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

### 6. Порядок действий для нового проекта

1. **Создать репозиторий на GitHub**
   - Перейти на github.com
   - Нажать "New repository"
   - Заполнить название и описание
   - Выбрать Public/Private
   - Не добавлять README и .gitignore

2. **Локальная настройка:**
```bash
mkdir project-name
cd project-name
git init
echo "# Project Name" > README.md
# Создать .gitignore
# Создать файлы проекта
```

3. **Первый коммит:**
```bash
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/username/project-name.git
git branch -M main
git push -u origin main
```

### 7. Конвенция коммитов

**Хорошие примеры:**
- `feat: добавить новую функциональность`
- `fix: исправить баг в обработке ошибок`
- `docs: обновить документацию`
- `refactor: улучшить структуру кода`
- `style: форматирование кода`

**Плохие примеры:**
- `123`
- `fix`
- `много изменений`

### 8. Решение常见问题

**Если забыли файл в коммите:**
```bash
git add forgotten-file.py
git commit --amend
```

**Обновление репозитория:**
```bash
git pull origin main
git push origin main
```

**Решение конфликтов:**
```bash
# Решить конфликты вручную
git add .
git commit -m "Разрешить конфликты слияния"
```

## 📋 Best Practices

1. **Частые коммиты** - делайте небольшие осмысленные коммиты
2. **Перед push всегда pull** - избегайте конфликтов
3. **Пишите понятные сообщения** - описывайте что изменилось
4. **Используйте .gitignore** - защищайте敏感 данные
5. **Работайте в ветках** - для новых функций используйте отдельные ветки

## 🔗 Полезные ресурсы

- [Официальная документация Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)

---

*Это руководство покрывает 90% повседневных задач при работе с Git и GitHub* 🎯