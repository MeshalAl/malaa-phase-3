from dotenv import load_dotenv

def load_env(path: str | None = None):
    load_dotenv(dotenv_path=path)
