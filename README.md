# Prime checker utility

This repository provides a small Python script, `prime_checker.py`, that reports whether an integer is prime.

## Usage

### Basic usage

From a terminal where Python is available on the `PATH`:

```powershell
python prime_checker.py 11
```

If you omit the number, the script will prompt you to enter one interactively.

### Windows PowerShell paths containing spaces or non-ASCII characters

When invoking Python (or the script path) via PowerShell's call operator (`&`), you must wrap each path that contains spaces or non-ASCII characters in quotes. For example, if your username contains a full-width space character, use:

```powershell
& "C:/Users/村上　陸/AppData/Local/Microsoft/WindowsApps/python3.11.exe" "C:/Users/村上　陸/OneDrive/work/repository/prime_checker.py" 17
```

Notice that both the Python executable and the script path are quoted individually.

On systems where `python` or `py` is already on the `PATH`, you can avoid long paths entirely:

```powershell
py prime_checker.py 17
```

This typically works without additional quoting.
