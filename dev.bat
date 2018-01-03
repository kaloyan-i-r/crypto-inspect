@echo off
SET opt=%1

if "%opt%"=="up" goto up
if "%opt%"=="down" goto down

echo usage: dev [OPTION]
echo 	- up - start docker compose
echo 	- down - destroy docker compose
goto end


:up
docker-compose -f docker-compose-dev.yml up -d --build
goto end

:down
docker-compose -f docker-compose-dev.yml down --remove-orphans
goto end

:end