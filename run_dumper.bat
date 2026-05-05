@echo off
title Deadlock Nightmare Dumper - 0xThiagoAmaral
color 0D

echo ==========================================
echo    DEADLOCK NIGHTMARE DUMPER - PRO
echo ==========================================
echo [*] Checking for requirements...
pip install pymem requests --quiet

echo [*] Starting the Dumper Engine...
python nightmare_dumper.py

echo.
echo ==========================================
echo [v] Dump Completed! 
echo Check nightmare_offsets.json/hpp/cs
echo ==========================================
pause
