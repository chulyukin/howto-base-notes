# Шаг 3. Scala Build Tool (SBT). Установка

```console
# Добавить репозитории
echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list  
echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
# Добавить ключ
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo tee /etc/apt/trusted.gpg.d/sbt.asc
# Установить **sbt**
sudo apt-get update
sudo apt-get install sbt
```
Проверка версии:
```console
sbt -version
```
_По неизвестным причинам, файл **sbt-launch-....jar** не загружался. Определить требуемый файл, можно через **sbt -version** или **sbt**._  
_**Пример сообщения об ошибке с отсутствющим файлом :**_  
``` 
cat: /home/user/.cache/sbt/boot/sbt-launch/1.12.9/sbt-launch-1.12.9.jar.sha1: Нет такого файла или каталога
shasum: standard input: no properly formatted SHA checksum lines found
failed to download launcher jar: https://repo1.maven.org/maven2/org/scala-sbt/sbt-launch/1.12.9/sbt-launch-1.12.9.jar (shasum mismatch) 
```
_В этом случае, файл загружается в ручную (в текущем примере это:)_
```console
sudo wget https://repo1.maven.org/maven2/org/scala-sbt/sbt-launch/1.12.9/sbt-launch-1.12.9.jar 
```
_Файл нужно скопировать в папку по пути из сообщения:_
```console
cp sbt-launch-1.12.9.jar ~/.cache/sbt/boot/sbt-launch/1.12.9/sbt-launch-1.12.9.jar
```  

**[Решение проблем при установке и настройка sbt](stp_03_install_sbt.md)**  
**[Сборка тестового проекта через sbt](stp_03_test_project_sbt.md)**  
