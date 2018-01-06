@echo off
SET opt=%1

if "%opt%"=="up" goto up
if "%opt%"=="down" goto down
if "%opt%"=="restart" goto restart

echo usage: dev [OPTION]
echo 	- up - start docker compose
echo 	- down - destroy docker compose
echo    - restart - restart docker compose services
goto end


:up
docker-compose -f docker-compose-dev.yml up -d --build
goto end

:down
docker-compose -f docker-compose-dev.yml down --remove-orphans
goto end

:restart
docker-compose -f docker-compose-dev.yml restart
goto end

:end