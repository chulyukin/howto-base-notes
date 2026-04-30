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

[__kernel_scalalmond.ipynb](notebooks/SCALA_ALMOND/__kernel_scalalmond.ipynb) - Тестовый Notebook с параметрами ядра  

```console
wget https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/SCALA_ALMOND/__kernel_scalalmond.ipynb -O ~/WORKSHOP/SCALA_ALMOND/__kernel_scalalmond.ipynb
```

[__spark_scalalmond.ipynb](notebooks/SCALA_ALMOND/__spark_scalalmond.ipynb) - Тестовый Notebook с примером запуска Spark - сессии

```console
wget https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/SCALA_ALMOND/__spark_scalalmond.ipynb -O ~/WORKSHOP/SCALA_ALMOND/__spark_scalalmond.ipynb
```

[__scalalmond_example_add_external_code.ipynb](notebooks/SCALA_ALMOND/__scalalmond_example_add_external_code.ipynb) - Тестовый Notebook c примерами добавления внешних файлов кода для Almond Scala (magics Ammonite)

```console
cd ~/WORKSHOP/SCALA_ALMOND

wget https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/SCALA_ALMOND/__scalalmond_example_add_external_code.ipynb -O __scalalmond_example_add_external_code.ipynb

mkdir -p __scalalmond_example_add_external_code
cd __scalalmond_example_add_external_code

curl -O https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/SCALA_ALMOND/__scalalmond_example_add_external_code/example.md
curl -O https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/SCALA_ALMOND/__scalalmond_example_add_external_code/html_code_example.sc
curl -O https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/SCALA_ALMOND/__scalalmond_example_add_external_code/markdown_read_example.sc

cd ~/WORKSHOP/SCALA_ALMOND
```
