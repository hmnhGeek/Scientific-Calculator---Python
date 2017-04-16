import cx_Freeze

executables = [cx_Freeze.Executable('calculator.py', icon = "calculator.ico")]

cx_Freeze.setup(
    name='Calculator',
    options={"build_exe": {"packages":["Tkinter", "math", "os"], "include_files":["About.txt", "history.txt", "calculator.ico"]}},

    description="Caluculator",
    executables = executables
    )
