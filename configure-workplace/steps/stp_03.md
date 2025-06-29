# Шаг 3. Scala Build Tool (SBT). Установка

Добавить репозитории
```console
echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list  
echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
```
Добавить ключ
```console
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo tee /etc/apt/trusted.gpg.d/sbt.asc
```
Установить **sbt**
```console
sudo apt-get update
sudo apt-get install sbt
```
Проверка версии:
```console
sbt -version
```
**[Решение проблем при установке и настройка sbt](stp_03_install_sbt.md)**  
**[Сборка тестового проекта через sbt](stp_03_test_project_sbt.md)**  
