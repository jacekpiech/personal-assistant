# Celery configuration
## Redis run 

```
sudo /etc/init.d/redis-server stop 
docker run -p "6379:6379" redis
```
## Celery run
```shell
poetry shell
cd assistant
celery -A assistant worker -l info
celery -A assistant beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```