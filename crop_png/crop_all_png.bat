@echo off
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Cropping all PNG files in current directory...
python crop_png_images.py . -p "*.png" -m 10

echo.
echo Done! Press any key to exit.
pause 