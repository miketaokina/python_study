# Install VS Code (Cask): 
## Homebrew: 
```
brew install --cask visual-studio-code
```
###### Use --cask to install GUI software
### Expected Output: 
```
==> Downloading https://update.code.visualstudio.com/...
==> Installing Cask visual-studio-code
==> Moving App 'Visual Studio Code.app' to '/Applications/Visual Studio Code.app'
🍺  visual-studio-code was successfully installed!
```
# Install Python: 
## Homebrew: 
```
brew install python
```
###### It installs the latest stable version of python and corresponding package manager 'pip'
### Expected Output: 
```
==> Fetching downloads for: python@3.x
==> Installing dependencies for python@3.x: ...
==> Installing python@3.x
🍺  /opt/homebrew/Cellar/python@3.x/...: xx files, xxMB
```
###### To check different version of python: 
```
brew search python@
```
### Expected Output: 
```
==> Downloading Homebrew API data
✔︎ JSON API packages.arm64_golden_gate.jws.json                                                                                                                                           Downloaded   16.0MB/ 16.0MB
==> Formulae
python@3.10 (deprecated)  python@3.12               python@3.14               python@3.9 (disabled)     ipython                   pythran                   jython                    pythia
python@3.11               python@3.13               python@3.15               bpython                   wxpython                  cython                    ptpython
```

```
brew info python
```
### Expected Output: 
```
==> python@3.15: stable 3.15.2 (bottled)
Interpreted, interactive, object-oriented programming language
https://www.python.org/
Aliases: python, python3, python@3
Not installed
Bottle Size: 20.3MB
Installed Size: 79.7MB
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/p/python@3.15.rb
License: Python-2.0
==> Dependencies
Required (6): ca-certificates, mpdecimal, openssl@4, sqlite, xz, zstd
==> Caveats
Python is installed as
  /opt/homebrew/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, are installed into
  /opt/homebrew/opt/python@3.15/libexec/bin

`idle3.15` requires tkinter, which is available separately:
  brew install python-tk@3.15

`dbm.gnu` is available separately:
  brew install python-gdbm@3.15

For more information about Homebrew and Python, see: https://docs.brew.sh/Homebrew-and-Python
==> Analytics
install: 254,866 (30 days), 254,911 (90 days), 254,914 (365 days)
install-on-request: 25,083 (30 days), 25,128 (90 days), 25,128 (365 days)
build-error: 40,004 (30 days)
```

```
which python3
```
### Expected Output: 
```
/opt/homebrew/bin/python3
```
```
python3 --version
```
### Expected Output: 
```
Python 3.15.2     # or current latest stable version
```