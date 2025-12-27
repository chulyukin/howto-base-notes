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
coursier launch --fork almond:0.14.1 --scala 2.13.16 -- --install 
```  

**Notebooks** (положить в ~/WORKSHOP/SCALA_ALMOND/):
|Notebook|Комментарий|
|:-|:-|
|[__kernel_scalalmond.ipynb](notebooks/SCALA_ALMOND/__kernel_scalalmond.ipynb)|Тестовый Notebook с параметрами ядра|
|[__scalalmond_example_add_external_code.ipynb](notebooks/SCALA_ALMOND/__scalalmond_example_add_external_code.ipynb)|Тестовый Notebook c примерами добавления внешних файлов кода для Almond Scala (magics Ammonite)|
