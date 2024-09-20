rd /s /q dist
rd /s /q build
python  -m PyInstaller --noconfirm --noconsole -i econ.ico -F --name Mat_new main.py