import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    NVIDIA_API_KEY: str | None = os.getenv("NVIDIA_API_KEY")
    NVIDIA_BASE_URL: str = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
    NVIDIA_MODEL: str = os.getenv("NVIDIA_MODEL", "meta/llama-3.1-70b-instruct")


settings = Settings()