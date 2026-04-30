# Шаг 7. Jupyter Notebook. Установка и настройка Scala kernel Almond 
Создать директорию для проектов Scala
```console
mkdir -p ~/WORKSHOP/SCALA_ALMOND # для проектов Scala
```
Устновить kernel Scala
```console
curl -Lo coursier https://git.io/coursier-cli
chmod +x coursier
sudo mv coursier /usr/local/bin
coursier launch --fork almond --scala 2.13.17 -- --install --force
```  

**Notebooks** (положить в ~/WORKSHOP/SCALA_ALMOND/):
|Notebook|Комментарий|Установка|
|:-|:-|:-|
|[__kernel_scalalmond.ipynb](notebooks/SCALA_ALMOND/__kernel_scalalmond.ipynb)|Тестовый Notebook с параметрами ядра|```wget https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/SCALA_ALMOND/__kernel_scalalmond.ipynb -O ~/WORKSHOP/SCALA_ALMOND/__kernel_scalalmond.ipynb```|
|[__spark_scalalmond.ipynb](notebooks/SCALA_ALMOND/__spark_scalalmond.ipynb)|Тестовый Notebook с примером запуска Spark - сессии|```https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/SCALA_ALMOND/__spark_scalalmond.ipynb -O ~/WORKSHOP/SCALA_ALMOND/__spark_scalalmond.ipynb```|
|[__scalalmond_example_add_external_code.ipynb](notebooks/SCALA_ALMOND/__scalalmond_example_add_external_code.ipynb)|Тестовый Notebook c примерами добавления внешних файлов кода для Almond Scala (magics Ammonite)||
