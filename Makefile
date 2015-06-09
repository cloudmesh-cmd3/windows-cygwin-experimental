installer:
	pyinstaller --onefile --icon=shellicon.ico shell.py --name cm

windows:
	echo "create a program for windows"
	pyinstaller --onefil --icon=shellicon.ico cloudmesh_cmd/shell.py --name cm

linux:
	echo "create a program for linux"
	pyinstaller --onefile --icon=shellicon.ico cloudmesh_cmd/shell.py --name cm

osx: 
	echo "create a program for osx"
	pyinstaller --icon=shellicon.ico cloudmesh_cmd/shell.py --name cm
