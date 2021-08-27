# redir-balancer

## Запуск сервиса

### С помощью docker-compose:
```shell
git clone https://github.com/cyber-chuvash/redir-balancer.git
cd redir-balancer
docker-compose up -d --build
```
В `docker-compose.yml` можно поменять конфиг через переменные окружения. 

### "Bare-metal":
```shell
git clone https://github.com/cyber-chuvash/redir-balancer.git
cd redir-balancer
# На этом этапе стоит создать виртуальное окружение Вашим любимым способом (venv, pyenv и т.д.)
pip install -r requirements/production.txt
# Изменить конфиг можно через переменные окружения (здесь дефолтные):
export SANIC_CDN_HOST="cdn.test"
export SANIC_CDN_REDIRECT_RATIO=9

sanic balancer.server.app --host=127.0.0.1 --port=8080 --workers=4
```


## Testing
```shell
pip install -r requirements/testing.txt
pytest
```

## Нагрузочное тестирование
Нагружал с помощью [locust](https://github.com/locustio/locust), locustfile в корне репозитория.

На MacBook Pro 15" 2017 (4 ядра) с 3-мя locust-worker'ами удалось выжать из одного воркера сервиса 7000 RPS.
При увеличении числа воркеров сервиса locust упирался в CPU и не мог дать больше нагрузки. 
Поэтому думаю, что без locust на той же машине, сервис, уже с 2-мя воркерами спокойно выдержит 10к RPS.  


## Улучшения
1. Потенциальное улучшение производительности — добавить кэширование результатов метода `CDNURLBuilder.make_cdn_url()` с помощью `@lru_cache` или другого алгоритма.
   Эффективность такого решения обратно пропорциональна тому, насколько разнообразны входящие запросы.

2. В данном виде сервис никак не проверяет переданную ссылку, и в 1 из 10 случаев просто редиректит на нее,
   а в других 9 генерирует на ее основе ссылку к CDN. Здесь срабатывает моя секьюрити-чуйка, 
   и кажется, что это можно как-нибудь по-хитрому использовать в неблагородных целях. Лишняя attack surface.

3. Улучшить конфигурацию и логику запуска сервиса: в текущем виде это скорее POC, до production-ready далеко.
