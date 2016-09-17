from setuptools import setup, find_packages

setup (
    name             = "webhook",
    version          = "0.1",
    description      = "Example SashiDo WebHook handler.",
    packages         = find_packages(),
    install_requires = ["gunicorn", "Flask"],
)
