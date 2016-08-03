from distutils.core import setup

setup(
    name="fleet",
    version="0.1.0",
    description="Talk to CoreOS Fleet with Cog",
    author="Brand Networks",
    author_email="oss@bn.co",
    url="https://bn.co",
    packages=["fleet", "fleet.commands"],
    install_requires=[
        "pycog3>=0.1.27",
        "requests>=2.10.0",
        "requests_unixsocket>=0.1.5"
    ],
    keywords=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License"
    ]
)
