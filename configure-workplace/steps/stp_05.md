# Шаг 5. Apache Spark. Установка
**Apache Spark** - фреймворк для реализации распределённой обработки данных, входящий в экосистему проектов Hadoop. Представлен интерфейсами языков Java, Scala, Python, R. https://spark.apache.org  


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
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 4.1.1
      /_/
         
Using Scala version 2.13.17 (OpenJDK 64-Bit Server VM, Java 17.0.18)
Type in expressions to have them evaluated.
Type :help for more information.
26/04/27 20:33:57 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Spark context Web UI available at http://192.168.88.252:4040
Spark context available as 'sc' (master = local[*], app id = local-1777311237799).
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
