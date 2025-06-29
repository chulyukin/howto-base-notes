# Шаг 8. Jupyter Notebook. Установка и настройка Scala Kernel Apache Toree 
Создать директорию для проектов Scala
```console
mkdir -p ~/WORKSHOP/SCALA_TOREE # для проектов Scala
```
Установить kernel
```console
python3 -m venv toreeenv  
source toreeenv/bin/activate  
pip install jupyter apache-toree
```
Прописать переменную SPARK_HOME в kernel
```console
jupyter toree install --spark_home=$SPARK_HOME --user
```
```console
deactivate
```
![__kernel_scalatoree.ipynb](notebooks/SCALATOREE/__kernel_toreescala.ipynb) Тестовый Notebook с параметрами ядра (положить в ~/WORKSHOP/SCALATOREE/)   
Пример запуска **spark** сессии  
![__example_toreespark.ipynb](notebooks/SCALATOREE/__example_toreespark.ipynb) Тестовый Notebook с примером (положить в ~/WORKSHOP/SCALATOREE/)  
Пример инициализации **spark session**:
```scala
import org.apache.spark.sql.SparkSession

val warehouseDir = "~/WORKSHOP/SCALA_TOREE/warehouse"
val spark = SparkSession.builder()
            .appName("My custom Spark")
            .master("local[2]")
            .config("spark.executer.memory", "4g")
            .config("spark.driver.memory", "2g")
            .config("spark.driver.extraJavaOptions","-Derby.system.home=/tmp/derby")
            .config("spark.sql.warehouse.dir", warehouseDir)
            .config("spark.sql.catalogImplementation", "hive")
            .config("javx.jdo.option.ConnectionURL",s"jdbc:derby:;dtatbaseName=$warehouseDir/metasore_db;create=true")
            .config("datanucleus.schema.autoCreateAll", "true")
            .enableHiveSupport()
            .getOrCreate()
```
