import importlib.metadata

packages = [
    "ipykernel>=7.3.0",
    "python-dotenv",
    "langchain==1.2.18",
    "langchain-core",
    "langgraph==1.1.10",
    "langsmith==0.8.3",
    "langchain-groq==1.1.2",
    "langchain-community==0.4.1",
    "langchain-huggingface==1.2.2",
    ]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")