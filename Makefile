installer:
	pyinstaller --onefile shell.py --name cm

windows:
	echo "create a program for windows"
	pyinstaller --onefil cloudmesh_cmd/shell.py --name cm

linux:
	echo "create a program for linux"
	pyinstaller --onefile cloudmesh_cmd/shell.py --name cm

osx: 
	echo "create a program for osx"
	pyinstaller cloudmesh_cmd/shell.py --name cm
