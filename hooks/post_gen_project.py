import shutil

ci_provider = "{{ cookiecutter.__ci }}"
if ci_provider != "github":
    shutil.rmtree(".github")
