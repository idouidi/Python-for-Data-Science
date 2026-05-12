# 📦 Create a Python Package

This guide walks you through every step to create, build, install, test, and distribute a Python package.

---

## 📁 Recommended Project Structure

Before getting started, here is the typical file structure of a Python package:

```
my_project/
├── ft_package/
│   ├── __init__.py        # Makes the folder importable as a module
│   └── module.py          # Your source code
├── setup.py               # Package configuration
├── README.md              # Project description
├── LICENSE                # Project license
└── tester.py              # Test script
```

### `__init__.py`
A required file that tells Python the folder is a package. It can be empty, or expose symbols from submodules:
```python
from .module import my_function
```

### `setup.py`
The main configuration file for your package:
```python
from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    packages=find_packages(),
    description="A short description of my package",
    author="Your Name",
    author_email="email@example.com",
    url="https://github.com/you_repo/ft_package",
    python_requires=">=3.10",
)
```

---

## 🔧 Step 1 — Install Required Tools

```bash
pip install setuptools wheel twine
```

### What each package does:

| Tool | Role |
|---|---|
| `setuptools` | Provides the `setup()` function and all packaging utilities. It is the backbone of Python's packaging system. |
| `wheel` | Enables building `.whl` archives (a modern binary format that installs faster than `.tar.gz`). |
| `twine` | A secure tool for uploading your package to PyPI (the Python Package Index). |

> **Why not just `pip`?** `pip` is for *installing* packages. `setuptools`, `wheel`, and `twine` are for *creating* and *distributing* them.

---

## 🏗️ Step 2 — Build the Package

```bash
python setup.py sdist bdist_wheel
```

### Command breakdown:

| Fragment | Meaning |
|---|---|
| `python setup.py` | Runs your `setup.py` file, which describes your package. |
| `sdist` | **Source Distribution** — Creates a `.tar.gz` archive containing raw source code. Portable across all platforms. |
| `bdist_wheel` | **Binary Distribution Wheel** — Creates a `.whl` archive, a modern pre-built format that installs faster. |

### What gets generated:

```
dist/
├── ft_package-0.0.1.tar.gz           ← source distribution
└── ft_package-0.0.1-py3-none-any.whl ← wheel (binary)
```

### Breaking down the `.whl` filename:
```
ft_package - 0.0.1 - py3 - none - any .whl
    │           │      │      │     │
    │           │      │      │     └─ CPU architecture (any = all platforms)
    │           │      │      └─────── ABI tag (none = pure Python, no C extensions)
    │           │      └────────────── Python version (py3 = any Python 3.x)
    │           └───────────────────── Package version
    └───────────────────────────────── Package name
```

> 💡 **Note**: `build/` and `*.egg-info/` folders may also appear — these are intermediate build artifacts and can be safely ignored or deleted.

---

## 📥 Step 3 — Install the Package Locally

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

### Command breakdown:

| Fragment | Meaning |
|---|---|
| `pip install` | Installs a package via pip. |
| `./dist/...` | A local path to the `.whl` file. The `./` prefix tells pip this is a local file, not a package name to look up on PyPI. |
| `.whl` | The preferred format: faster to install than the `.tar.gz` source distribution. |

### Useful variants:

```bash
# Install from the source distribution instead
pip install ./dist/ft_package-0.0.1.tar.gz

# Install in editable mode (for development) — code changes are reflected immediately
pip install -e .

# Force reinstall even if the package is already installed
pip install --force-reinstall ./dist/ft_package-0.0.1-py3-none-any.whl
```

> ⚠️ **Editable mode** (`-e .`) is extremely useful during development: it creates a symbolic link to your source code, so any change you make is instantly available without reinstalling.

---

## 🔍 Step 4 — Display Package Information

```bash
pip3 show -v ft_package
```

### Command breakdown:

| Fragment | Meaning |
|---|---|
| `pip3` | Explicitly uses pip for Python 3 — useful when Python 2 is also installed on the system. |
| `show` | Subcommand that displays metadata about an installed package. |
| `-v` | **Verbose** — Shows additional details such as the list of installed files and classifiers. |
| `ft_package` | The name of the package to inspect. |

### Example output:
```
Name: ft_package
Version: 0.0.1
Summary: A short description of my package
Home-page: https://github.com/you_repo/ft_package
Author: Your Name
Author-email: email@example.com
License: UNKNOWN
Location: /usr/local/lib/python3.10/site-packages
Requires:
Required-by:
```

### Other useful inspection commands:

```bash
# List all installed packages
pip list

# Check that the package is importable
python -c "import ft_package; print('OK')"

# Find where the package is installed on disk
pip show ft_package | grep Location
```

---

## 🧪 Step 5 — Test the Package

```bash
python tester.py
```

### Command breakdown:

| Fragment | Meaning |
|---|---|
| `python` | Launches the Python interpreter. |
| `tester.py` | A test script that imports and exercises your package to verify it works correctly. |

### Example `tester.py`:
```python
# tester.py
import ft_package

result = ft_package.my_function()
print(f"Result: {result}")
assert result == "expected_value", "Test failed!"
print("✅ All tests passed.")
```


---

## 🗑️ Step 6 — Uninstall the Package

```bash
pip3 uninstall ft_package
```

### Command breakdown:

| Fragment | Meaning |
|---|---|
| `pip3` | Uses pip for Python 3. |
| `uninstall` | Subcommand that removes the package. pip will list the files to be deleted and ask for confirmation. |
| `ft_package` | The name of the package to remove — this is the name declared in `setup.py`, not necessarily the folder name. |

### Useful variants:

```bash
# Uninstall without being prompted for confirmation (-y = yes)
pip3 uninstall -y ft_package

# Uninstall multiple packages at once
pip3 uninstall -y ft_package another_package
```

---

## 🌍 Bonus — Publish to PyPI (optional)

If you want your package to be installable by anyone with `pip install ft_package`:

```bash
# 1. Create an account at https://pypi.org

# 2. Upload to TestPyPI first (sandbox environment — recommended before going live)
twine upload --repository testpypi dist/*

# 3. Upload to PyPI (production)
twine upload dist/*
```

### Breaking down `twine upload dist/*`:

| Fragment | Meaning |
|---|---|
| `twine` | Secure upload tool (uses HTTPS and verifies package integrity before sending). |
| `upload` | Subcommand that sends files to PyPI. |
| `dist/*` | Uploads all files in the `dist/` folder (both `.tar.gz` and `.whl`). |

> 💡 `twine` is preferred over the deprecated `python setup.py upload` because it validates your packages before uploading and ensures a secure connection.

---

## 🔄 Full Workflow Summary

```bash
# 1. Install tools
pip install setuptools wheel twine

# 2. Build
python setup.py sdist bdist_wheel

# 3. Install locally
pip install ./dist/ft_package-0.0.1-py3-none-any.whl

# 4. Inspect
pip3 show -v ft_package

# 5. Test
python tester.py

# 6. Uninstall
pip3 uninstall ft_package

# (Optional) 7. Publish to PyPI
twine upload dist/*
```

---

## 📚 Useful Resources

- [Official setuptools documentation](https://setuptools.pypa.io/)
- [PyPA Packaging Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [PyPI — Python Package Index](https://pypi.org/)
- [TestPyPI — sandbox environment](https://test.pypi.org/)