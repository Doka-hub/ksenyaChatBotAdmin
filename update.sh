#!/bin/bash

# Первая директория (admin)
ADMIN_DIR="/var/www/admin"
ADMIN_COMPOSE_FILE="docker-compose.prod.yml"

# Вторая директория (tgbot)
TGBOT_DIR="/var/www/tgbot"
TGBOT_COMPOSE_FILE="docker-compose.yml"

# Функция для обновления репозитория и перезапуска Docker
update_and_restart() {
    local DIR="$1"
    local COMPOSE_FILE="$2"

    echo "🔄 Переход в $DIR"

    # Проверяем, существует ли директория
    if [ -d "$DIR" ]; then
        cd "$DIR" || { echo "❌ Ошибка: Не удалось перейти в $DIR"; exit 1; }

        # Обновляем репозиторий
        echo "🚀 Обновляем репозиторий в $DIR"
        git pull origin master

        # Проверяем, есть ли docker-compose файл
        if [ -f "$COMPOSE_FILE" ]; then
            echo "🐳 Перезапускаем Docker: $COMPOSE_FILE"
            docker compose -f "$COMPOSE_FILE" up -d --build
        else
            echo "⚠️ Файл $COMPOSE_FILE не найден, пропускаем Docker."
        fi

        echo "✅ Репозиторий в $DIR обновлён и сервис запущен!"
    else
        echo "❌ Ошибка: Директория $DIR не найдена!"
    fi
}

# Обновляем и перезапускаем оба сервиса
update_and_restart "$ADMIN_DIR" "$ADMIN_COMPOSE_FILE"
update_and_restart "$TGBOT_DIR" "$TGBOT_COMPOSE_FILE"

echo "🎉 Все репозитории обновлены и сервисы перезапущены!"