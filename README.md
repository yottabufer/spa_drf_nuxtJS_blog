# О данном блоге

* bacd-end написан мной **самостоятельно**, в процессе уже понимал допушенные ошибки, что лучше нужно сделать по другому, но что взять с первого **самостоятельного** проекта
* front-end написан не полностью самостоятельно, с помощью интернета, курсов и видео

# Устанока
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
```python
source venv_spa_drf_blog/bin/activate
```
5. Устанавливаем пакеты для проекта
```python
pip install -r requirements.txt
```

> [!IMPORTANT]
> Проект может начать ругаться на отсутствие "ugettext_lazy", это изза модуля taggit_serializer, хоть и "ugettext_lazy" не используется с 3 версии джанго, > taggit до сих пор не исправили это

> [!NOTE]
> Information the user should notice even if skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Essential information required for user success.

> [!CAUTION]
> Negative potential consequences of an action.

> [!WARNING]
> Dangerous certain consequences of an action.
