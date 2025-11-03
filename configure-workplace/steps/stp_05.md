# Шаг 5. Apache Spark. Установка
```console
sudo apt update
sudo apt upgrade
```
Скачать Apache Spark версии 3.5.7
```console
cd ~
wget https://dlcdn.apache.org/spark/spark-3.5.7/spark-3.5.7-bin-hadoop3-scala2.13.tgz
```
Распаковать архив
```console
tar xvf spark-3.5.7-bin-hadoop3-scala2.13.tgz
```
Переместить в папку **/opt**
```console
sudo mv spark-3.5.7-bin-hadoop3-scala2.13 /opt/spark
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
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.7
      /_/
         
Using Scala version 2.13.8 (OpenJDK 64-Bit Server VM, Java 17.0.17-ea)
Type in expressions to have them evaluated.
Type :help for more information.
25/11/03 09:07:13 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Spark context Web UI available at http://Ubuntu2510:4040
Spark context available as 'sc' (master = local[*], app id = local-1762160834771).
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
