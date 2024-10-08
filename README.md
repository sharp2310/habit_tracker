# habit_trackerДля запуска проекта через docker необходимо выполнить ниже указанную команду и заполнить файл .env_sample
docker-compose up -d --build
Описание задач Добавьте необходимые модели привычек. Реализуйте эндпоинты для работы с фронтендом. Создайте приложение для работы с Telegram и рассылками напоминаний. Модели В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше 2 минут. Исходя из этого получаем первую модель — Привычка.

Привычка: Пользователь — создатель привычки. Место — место, в котором необходимо выполнять привычку. Время — время, когда необходимо выполнять привычку. Действие — действие, которое представляет из себя привычка. Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки. Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных. Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях. Вознаграждение — чем пользователь должен себя вознаградить после выполнения. Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки. Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки. Обратите внимание, что в проекте у вас может быть больше, чем одна описанная здесь модель.

Валидаторы Исключить одновременный выбор связанной привычки и указания вознаграждения. Время выполнения должно быть не больше 120 секунд. В связанные привычки могут попадать только привычки с признаком приятной привычки. У приятной привычки не может быть вознаграждения или связанной привычки. Нельзя выполнять привычку реже, чем 1 раз в 7 дней. Пагинация Для вывода списка привычек реализовать пагинацию с выводом по 5 привычек на страницу.

Права доступа Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD. Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять. Эндпоинты Регистрация Авторизация Список привычек текущего пользователя с пагинацией Список публичных привычек Создание привычки Редактирование привычки Удаление привычки Интеграция Для полноценной работы сервиса необходим реализовать работу с отложенными задачами для напоминания о том, в какое время какие привычки необходимо выполнять.

Для этого потребуется интегрировать сервис с мессенджером Telegram, который будет заниматься рассылкой уведомлений.

Безопасность Для проекта необходимо настроить CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.

Документация Для реализации экранов силами фронтенд-разработчиков необходимо настроить вывод документации. При необходимости эндпоинты, на которые документация не будет сгенерирована автоматически, описать вручную.