from setuptools import setup, find_packages

setup(
    name="model_bot",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "crewai",  # Include other dependencies here
        "pyyaml",  # Add more packages if needed
    ],
    python_requires=">=3.8",
    author="Your Name",
    description="A CrewAI project for building business models.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-repo-url",  # Optional: Replace with your repo
)
