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
