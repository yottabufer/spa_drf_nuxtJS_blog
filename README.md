# О данном блоге

* bacd-end написан мной самостоятельно, в процессе уже понимал допушенные ошибки, что лучше нужно сделать по другому, но что взять с первого **самостоятельного** проекта
* front-end написан не полностью самостоятельно, с помощью интернета, курсов и видео

# Устанока back-end
1. Клонируем проект с репозитория
```python
git clone https://github.com/yottabufer/spa_drf_nuxtJS_blog.git
```
2. Переходим в папку созданную папку
```python
cd spa_drf_nuxtJS_blog
```
3. Создаём виртуально окружение для работы с проектом
```python
python -m venv venv_spa_drf_blog
```
4. Активируем виртуальное окружение
	
+ Linux
```python
source venv_spa_drf_blog/bin/activate
```
+ Windows
```python
venv\Scripts\activate.bat 
```
5. Устанавливаем пакеты для проекта
```python
pip install -r requirements.txt
```
6. Проверяем всё ли в порядке
```python
python manage.py runserver
```
> ВАЖНО
>> Проект может начать ругаться на невозмонжность импорта "ugettext_lazy". Это из-за модуля taggit_serializer, хоть и "ugettext_lazy" не используется с 3 версии джанго, taggit до сих пор не исправили это
7. ПРОФИТ! Вы велеколепны, с бэк-ендом покончено



