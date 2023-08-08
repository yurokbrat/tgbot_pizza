@echo off

call %~dp0tg_bot/venv/Scripts\activate

cd %~dp0tg_bot

set TOKEN=6029713105:AAEwBfAFBPxj08c-rpXikj9TEieJoQXtN_Q

python telegram_bot.py

pause