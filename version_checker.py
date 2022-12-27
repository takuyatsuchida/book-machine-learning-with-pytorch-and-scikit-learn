import platform

from packaging.version import Version


def get_version(package):
    try:
        return __import__(package).__version__
    except ImportError:
        return None


def check_version(python_version, package_to_suggested_version):
    if Version(platform.python_version()) < Version(python_version):
        print(f"[NG] We recommend Python {python_version} or newer but found version {platform.python_version()}")
    else:
        print(f"[OK] Your Python version is {platform.python_version()}")

    for package, suggested_version in package_to_suggested_version.items():
        actual_version = get_version(package)
        if actual_version is None:
            print(f"[NG] {package} is not installed and/or cannot be imported")
        elif Version(actual_version) < Version(suggested_version):
            print(f"[NG] {package} {actual_version}, please upgrade to >= {suggested_version}")
        else:
            print(f"[OK] {package} {actual_version}")


if __name__ == "__main__":
    check_version("3.8", {
        "numpy": "1.21.2",
        "scipy": "1.7.0",
        "matplotlib": "3.4.3",
        "sklearn": "1.0",
        "pandas": "1.3.2",
    })
