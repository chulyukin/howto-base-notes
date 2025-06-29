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
coursier launch --fork almond:0.14.1 --scala 2.12.20 -- --install 
```  
![__kernel_scalalmond.ipynb](notebooks/SCALA_ALMOND/__kernel_scalalmond.ipynb) Тестовый Notebook с параметрами ядра (положить в ~/WORKSHOP/SCALA_ALMOND/)  
