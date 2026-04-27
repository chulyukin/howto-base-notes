# Шаг 6. Установка и настройка Jupter Notebook
## Установка jupyter Notebook
### Подготовка к установке
```console
sudo apt update
sudo apt upgrade
```
Необходимо установить пакеты:
- python3 - стандартный интерпретатор Python
- python3-dev - файлы разработки Python, заголовочные файлы и библиотеки для компиляции и сборки Python-пакетов из исходного кода
- python3-venv - модуль для создания виртуальных окружений Python
- python3-pip - менеджер пакетов для Python
 
```console
sudo apt install python3 python3-dev python3-venv python3-pip
```
## Создание виртуального окружения Python для установки Jupyter Notebook
Создание рабочих директорий (не обязательно, предназначено для удобства)
```console
mkdir -p ~/WORKSHOP # для проектов разработки
mkdir -p ~/WORKSHOP/DEVPYTHON # для общих проектов Python (будущее ядро "DevPython 3.1x")
mkdir -p ~/WORKSHOP/MLPYTHON # для проектов ML Python (будущее ядро "ML Python 3.1x") 
mkdir -p ~/WORKSHOP/PYTORCH # для проектов PyTorch (будущее ядро "PyTorch")
mkdir -p ~/WORKSHOP/PYSPARK # для проектов PySpark (будущее ядро "PySpark")
```
Основное виртуальное окружение Python (без окружения, начиная с версии Ubuntu 23.10, установить Juprter Notebook будет затруднительно)
```console
python3 -m venv mainenv # Окружение mainenv
source mainenv/bin/activate # Активация окружения
pip install --upgrade pip # Обновление пакета pip
pip install jupyter # Установка пакета Jupyter
deactivate
```
## Создание файла запуска Jupyter Notebook на рабочем столе (по желанию):
```console
nano "$(xdg-user-dir DESKTOP)/Jupyter_launch.sh"
```
В файл необходимо записать:
```bash
#!/bin/bash

full_path="WORKSHOP"

cd ~/$full_path

source ../mainenv/bin/activate

jupyter notebook --ip=0.0.0.0
```
Cделать файл исполняемым через меню по "правой кнопки мыши" или командой:
```console
sudo chmod +x "$(xdg-user-dir DESKTOP)/Jupyter_launch.sh"
```
Файл будет на рабочем столе и теперь можно запустить Jupyter Notebook (правая кнопка мыши -> Запустить как программу)  
(Рекомендуется проверить работоспособность)  

## Создание целевых окружений для использования
Будут созданы 4 окружения:
- Окружение python dev
- Окружение ml dev
- Окружение pytorch
- Окружение Spark

### Окружение Python Dev
Окружение общего назначения для работы в Python - с установкой модулей
```console
python3 -m venv pydevenv
source pydevenv/bin/activate
python3 -m pip install ipykernel
python -m ipykernel install --user --name=pydevenv --display-name "DevPython 3.1x"
pip install pandas fastparquet matplotlib
deactivate
```
![_kernel_devpython.ipynb](notebooks/DEVPYTHON/__kernel_devpython.ipynb) - Notebook с подсказками по параметрам ядра (положить в ~/WORKSHOP/DEVPYTHON/)  
```console
wget https://raw.githubusercontent.com/chulyukin/howto-base-notes\refs\configure-workplace/steps/notebooks/DEVPYTHON/__kernel_devpython.ipynb -O ~/WORKSHOP/DEVPYTHON/__kernel_devpython.ipynb
```

### Окружение Python ML
```console
python3 -m venv pymlenv
source pymlenv/bin/activate
python3 -m pip install ipykernel
python -m ipykernel install --user --name=pymlenv --display-name "MLPython 3.1x"
pip install pandas fastparquet matplotlib numpy scipy scikit-learn seaborn
deactivate 
```
![_kernel_mlpython.ipynb](notebooks/MLPYTHON/__kernel_mlpython.ipynb) - Notebook с подсказками по параметрам ядра (положить в ~/WORKSHOP/MLPYTHON/)  
```console
wget https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/MLPYTHON/__kernel_mlpython.ipynb -O ~/WORKSHOP/MLPYTHON/__kernel_mlpython.ipynb
```
### Окружение PyTorch
```console
python3 -m venv pytorchenv
source pytorchenv/bin/activate
python3 -m pip install ipykernel
python -m ipykernel install --user --name=pytorchenv --display-name "PyTorch"
pip install pandas fastparquet matplotlib numpy scipy scikit-learn seaborn
deactivate
```
![_kernel_pytorch.ipynb](notebooks/PYTORCH/__kernel_pytorch.ipynb) Notebook с установкой torch (положить в ~/WORKSHOP/MLPYTHON/)  
```console
wget https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/PYTORCH/__kernel_pytorch.ipynb -O ~/WORKSHOP/PYTORCH/__kernel_pytorch.ipynb
```
### Окружение PySpark
```console
python3 -m venv pysparkenv
source pysparkenv/bin/activate
python3 -m pip install ipykernel
python -m ipykernel install --user --name=pysparkenv --display-name "PySpark"
pip install pyspark==4.1.1 # Установить PySpark 4.1.1
pip install pandas fastparquet matplotlib pyarrow
deactivate
```
Установить переменные виртуального окружения
```console
echo 'export SPARK_HOME=/opt/spark' >> pysparkenv/bin/activate
echo 'export PYSPARK_PYTHON=$(which python)' >> pysparkenv/bin/activate
```
По указанным путям отредактировать файл kernel.json
```console
nano ~/.local/share/jupyter/kernels/pysparkenv/kernel.json
```
```json
{
 "argv": [
  "~/pysparkenv/bin/python",
  "-Xfrozen_modules=off",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "env":{
        "SPARK_HOME":"/opt/spark",
        "PYSPARK_PYTHON":"$HOME/pysparkenv/bin/python"
},
 "display_name": "PySpark",
 "language": "python",
 "metadata": {
  "debugger": true
 }
}
```
![_kernel_pyspark.ipynb](notebooks/PYSPARK/__kernel_pyspark.ipynb) Notebook с подсказками по параметрам ядра (положить в ~/WORKSHOP/PYSPARK/)  
![__example_pyspark.ipynb](notebooks/PYSPARK/__example_pyspark.ipynb) Notebook с пирмером запуска spark сессии  (положить в ~/WORKSHOP/PYSPARK/)  
```console
wget https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/PYSPARK/__kernel_pyspark.ipynb -O ~/WORKSHOP/PYSPARK/__kernel_pyspark.ipynb
wget https://raw.githubusercontent.com/chulyukin/howto-base-notes/refs/heads/main/configure-workplace/steps/notebooks/PYSPARK/__example_pyspark.ipynb -O ~/WORKSHOP/PYSPARK/__example_pyspark.ipynb
```
Пример запуска spark сессии:
```python
import os
import sys
spark_home = os.environ.get('SPARK_HOME', None)
sys.path.insert(0, spark_home + "python")
os.environ["SPARK_LOCAL_IP"]='localhost'
from pyspark import SparkContext, SparkConf#, HiveContext
conf = SparkConf()\
             .setAppName("Example Spark")\
             .setMaster("local[2]")\
             .setAppName("CountingSheep")\
             .set("spark.sql.catalogImplementation", "hive")
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
```
```python
exec(open(os.path.join(spark_home, 'python/pyspark/shell.py')).read())
```
Результат запуска:
```shell
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.5.8
      /_/

Using Python version 3.14.4 (main, Apr  8 2026 04:02:31)
Spark context Web UI available at http://localhost:4040
Spark context available as 'sc' (master = local[2], app id = local-1777224633991).
SparkSession available as 'spark'.
```
