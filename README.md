# PythonPackagingTemplate
Simple template for how to lay out a python package

Creates a package named `testPackage` with two subpackages - `hello_world` and `myPackage`. If you clone this repository, navigate to it, then run `python -m pip install .`, a copy of this code will be copied to your `site-packages` folder. Since I was working out of an anaconda environment, it ended up in ~/anaconda3/envs/testEnv/lib/python3.7/site-packages/testPackage. With this install command, those are the files that are run when you execute code from the relevant python interpreter.

The `hello_world` module also contains a main() function which is referenced in the setup.py file as an `entry_point`, so that gets set up as a command line utility during the install operation as well.

```.
├── LICENSE
├── README.md
├── setup.py
└── testPackage
    ├── hello_world
    │   ├── __init__.py
    │   └── main.py
    ├── __init__.py
    └── myPackage
        ├── __init__.py
        └── testModule.py
```

In this configuration, there are no actual modules associated with testPackage (no .py files). The two sub-folders (myPackage and hello_world) are sub-packages, and so have to be imported directly before you can access their modules (ie, you can't write `import testPackage`; testPackage.myPackage. ...).
