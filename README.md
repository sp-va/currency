# Сборка контейнера и зпапуск образа
Сначала собираем контейнер командой:
```docker
docker build -t currency-app .      
```
И запускаем образ контейнера:
```docker
docker run -p 8000:8000 currency-app      
```

# Получение информации о курсе валют
http://127.0.0.1:8000/api_v1/rates/?from_currency=USD&to_currency=RUB&value=123.4567
