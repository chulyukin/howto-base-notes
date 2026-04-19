# Шаг 1. Установка JDK (Openjdk-17) 

**Обновление репозитория**
```console
sudo apt update
sudo apt upgrade
```

**Установка openjdk-17**
```console
sudo apt-cache search openjdk | grep openjdk-17
sudo apt install openjdk-17-jre
sudo apt install openjdk-17-jdk
```  
**Вывод версии Java**
```console
java --version
# openjdk 17.x.xx 2026-xx-xx
# OpenJDK Runtime Environment (build 17.x.xx-ea+8-Ubuntu-1)
# OpenJDK 64-Bit Server VM (build 17.x.xx-ea+8-Ubuntu-1, mixed mode, sharing)
```
