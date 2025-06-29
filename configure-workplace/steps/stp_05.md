# Шаг 5. Apache Spark. Установка
```console
sudo apt update
sudo apt upgrade
```
Скачать Apache Spark версии 3.5.5
```console
cd ~
wget https://dlcdn.apache.org/spark/spark-3.5.6/spark-3.5.6-bin-hadoop3.tgz
```
Распаковать архив
```console
tar xvf spark-3.5.6-bin-hadoop3.tgz
```
Переместить в папку **/opt**
```console
sudo mv spark-3.5.6-bin-hadoop3 /opt/spark
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
25/06/28 10:17:32 WARN Utils: Your hostname, user-VirtualBox resolves to a loopback address: 127.0.1.1; using 10.0.2.15 instead (on interface enp0s3)
25/06/28 10:17:32 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
25/06/28 10:17:36 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Spark context Web UI available at http://10.0.2.15:4040
Spark context available as 'sc' (master = local[*], app id = local-1751095057951).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.6
      /_/
         
Using Scala version 2.12.18 (OpenJDK 64-Bit Server VM, Java 17.0.15)
Type in expressions to have them evaluated.
Type :help for more information.
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
