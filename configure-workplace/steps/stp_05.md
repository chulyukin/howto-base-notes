# Шаг 5. Apache Spark. Установка
```console
sudo apt update
sudo apt upgrade
```
Скачать Apache Spark версии 4.1.1
```console
cd ~
wget https://dlcdn.apache.org/spark/spark-4.1.1/spark-4.1.1-bin-hadoop3.tgz
# Распаковать архив
tar xvf spark-4.1.1-bin-hadoop3.tgz
```
Переместить в папку **/opt**
```console
sudo mv spark-4.1.1-bin-hadoop3 /opt/spark
```
Прописать системные переменные
```console
echo 'export SPARK_HOME=/opt/spark' >> ~/.bashrc
echo 'export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin' >> ~/.bashrc
```
```console
source ~/.bashrc
```
Далее необходимо завершить сессию в терминале, затем зайти снова в терминал и выполнить
```console
spark-shell
```
Появится вывод:
```console
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.8
      /_/
         
Using Scala version 2.13.8 (OpenJDK 64-Bit Server VM, Java 17.0.18)
Type in expressions to have them evaluated.
Type :help for more information.
26/04/26 10:07:17 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Spark context Web UI available at http://192.168.88.252:4040
Spark context available as 'sc' (master = local[*], app id = local-1777193248296).
Spark session available as 'spark'.
scala> 
```
Выход из оболочки **Spark**
```scala
scala> :q
```
Можно так же проверить доступность spark-submit (файла-сценария запуска приложений Spark)
```console
spark-submit
```
