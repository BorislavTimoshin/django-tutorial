## Активация виртуального окружения:
```bash
python3 -m venv djvenv
source djvenv/bin/activate
```

## Установка зависимостей:
```bash
pip3 install -r requirements/prod.txt
```

## Для разработки дополнительно необходимо установить зависимости из
`requirements/dev.txt`
```bash
pip3 install -r requirements/dev.txt
```

## Настройка переменных окружения
Скопируйте файл config.env в .env, если нужно, отредактируйте значения переменных
```bash
cp config.env env
```

## Запуск
```bash
cd sitewomen 
python3 manage.py runserver --insecure
```
