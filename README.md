# Te Reo Number Converter
This program is written in Python 3.6. To compile it yourself you need `PyQt5` [(here)](https://pypi.org/project/PyQt5/) and to create an executable file you need `pyinstaller` [(here)](http://www.pyinstaller.org/), which you can install with
```
pip install PyQt5==5.9.2
pip install pyinstaller
```

The main file `TeReoNumberConverter_GUI.py` works without `pyinstaller` and can be run with
```
python ./build_files/TeReoNumberConverter_GUI.py
```

Otherwise, to build the single-file executable program, run
```
pyinstaller --onefile --windowed --icon=./build_files/Icon.ico --name="Te Reo Number Converter" ./build_files/TeReoNumberConverter_GUI.py
```

The icon used (animal-dog.png) is taken from the Fugue Icons set by [Yusuke Kamiyamane](https://p.yusukekamiyamane.com/) under [Creative Commons Attribution 3.0 License](https://creativecommons.org/licenses/by/3.0/). It was converted to an `.ico` file with [IcoConvert](https://icoconvert.com/Multi_Image_to_one_icon/) tool.

## Screenshots
### Windows
![Windows](https://github.com/jnga773/TeReoNumberConverter/blob/master/dist/screencap_windows.PNG)
### Linux (Ubuntu 18.04)
![Linux](https://github.com/jnga773/TeReoNumberConverter/blob/master/dist/screencap_linux.png)
### macOS (Big Sur 11.4)
![macOS](https://github.com/jnga773/TeReoNumberConverter/blob/master/dist/screencap_macos.png)

## Update History
 - v1.0 - Initial Release
 - v1.1 - Fixed bug where "10" would be printed as "kotahi tekau". Also changed "1" in ones column from "kotahi" to "tahi".
 - v1.2 - Increased range to < 10 billion (max 9,999,999,999). The character limit in the input box is 10 characters.
 - v1.2.1 - Fixed typo
 - v1.2.1 - Added commas to format of input string (1234 -> 1,234)
 - v1.3 - Fixed the conversion so it correctly translates the numbers. Thousands are now grouped correctly.
