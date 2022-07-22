# itmo-rating

## Веб-сервис, созданный мною в 20-х числах июля 2022 года, чтобы отслеживать своё положение в рейтинге абитурентов ИТМО.

Интерфейс:
<img width="1352" alt="Снимок экрана 2022-07-22 в 10 28 02" src="https://user-images.githubusercontent.com/60572329/180387337-7690dd57-a24b-4147-8cc2-4b723c64b793.png">

## Использованные технологии:
* Django(прошёл половину курса на Stepik)
* requests(для AJAX запроса к API итмо, чтобы получить список заявлений)
* nginx(для обработки http запросов)
* screen(чтобы django сервер работал бесконечно, это плохо - нужно использовать Gunicorn)
* ...

## Мысли по данному проекту
Локально всё получилось так как и планировал, но на проде пришлось неистово костылить. 
- CSS перенёс прямо в html файлы из-за того, что django на проде сам не работает со статикой.
- Использовл screen вместо gunicorn
- Мало работал с Git
- Не самый высокий уровень качества кода (parser.py, ну что это за функция на 70 строк?)
- ...

### Однако, проект работает *бесперебойно*, я реализовал его за *2 дня*, вполне доволен результатом.
*Все глобальное начинается с мелочей.
Конфуций*
