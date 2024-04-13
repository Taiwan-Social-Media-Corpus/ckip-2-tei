from setuptools import (
    find_namespace_packages,
    setup,
)


def main():
    with open("README.md", encoding="utf-8") as file:
        readme = file.read()

    setup(
        name="ckip2tei",
        version="1.1.2",
        description="A Python package that asynchronously segments JSON data into TEI XML format.",
        packages=find_namespace_packages(
            include=[
                "ckip2tei",
                "ckip2tei.*",
            ]
        ),
        long_description=readme,
        long_description_content_type="text/markdown",
        url="https://github.com/Taiwan-Social-Media-Corpus/ckip-2-tei.git",
        author="Retr0327",
        author_email="lixingyang.dev@gmail.com",
        license="Apache License 2.0",
        classifiers=[
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.10",
            "Operating System :: OS Independent",
        ],
        install_requires=[
            "ckip-transformers >= 0.3.4",
            "pydantic >= 2.7.0",
            "pydantic-settings >= 2.2.1",
        ],
        extras_require={
            "dev": ["pytest>=7.0", "twine>=4.0.2"],
        },
        python_requires=">=3.10",
    )


if __name__ == "__main__":
    main()
