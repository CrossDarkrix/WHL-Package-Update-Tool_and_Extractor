# -*- coding: utf-8 -*-
"""
Name : whl Package Update Tool(whl packages only)
Author: DarkRix
Version: 3.0
"""
import json, sys, subprocess, argparse
from time import time as ti
from os import chdir as cd
from os import getcwd as pwd

currentdir = pwd()

def pip_json():
	_process = subprocess.Popen([sys.executable, '-m', 'pip', 'list', '--outdated', '--format=json'], stdout=subprocess.PIPE)
	outputs, _ = _process.communicate()
	json_data = json.loads(outputs.decode('utf-8'))
	return json_data

def pip(command):
	_process = subprocess.Popen([sys.executable, '-m', 'pip'] + command, stdout=subprocess.PIPE)
	outputs, _ = _process.communicate()
	return outputs.decode('utf-8')

def Update():
	start = ti()
	print("Getting Update Package List....")
	jdata = pip_json()
	for i in range(int(len(jdata))):
		cd(currentdir)
		Package_Name = jdata[i]['name']
		File_Type = jdata[i]['latest_filetype']

		if File_Type == 'sdist':
			Package_Name = """"""
		else:
			pass
		if Package_Name == '':
			pass
		else:
			print(pip(['install', '--upgrade','--no-deps', Package_Name]), flush=True)
		cd(currentdir)
	elst = ti() - start
	print("\nElapsed Time:{0}".format(round(elst)) + "[sec]")
	print("All Wheel Packages Updated.")

def Download():
	start = ti()
	print("Getting Update Package List....")
	jdata = pip_json()
	print("\n########## Package List ##########\n")
	for i in range(int(len(jdata))):
		cd(currentdir)
		Package_Name = jdata[i]['name']
		File_Type = jdata[i]['latest_filetype']
		print("  ◆ " + Package_Name + ' (Install Type: ' + File_Type + ')')
	print("\n##################################\n")

	for i in range(int(len(jdata))):
		cd(currentdir)
		Package_Name = jdata[i]['name']
		File_Type = jdata[i]['latest_filetype']

		if File_Type == 'sdist':
			Package_Name = """"""
		else:
			pass
		if Package_Name == '':
			pass
		else:
			print(pip(['download','--no-deps','--no-cache-dir',Package_Name]), flush=True)
	elst = ti() - start
	print("\nElapsed Time:{0}".format(round(elst)) + "[sec]")
	print("All Wheel Packages Downloaded.")

def List():
	start = ti()
	print("Getting Update Package List....")
	jdata = pip_json()
	print("\n########## Package List ##########\n")
	for i in range(int(len(jdata))):
		Package_Name = jdata[i]['name']
		File_Type = jdata[i]['latest_filetype']
		print("  ◆ " + Package_Name + ' (Install Type: ' + File_Type + ')')
	print("\n##################################\n")
	elst = ti() - start
	print("\nElapsed Time:{0}".format(round(elst)) + "[sec]")

def main(argument):
	Ap = argparse.ArgumentParser()
	Ap.add_argument("-l", "--list", action="store_true", help="only listup update lists")
	Ap.add_argument("-d", "--download", action="store_true", help="only download update packages")
	Ap.add_argument("-u", "--update", action="store_true", help="only update packages")
	Ap.add_argument("-v", "--version", action="version", version="3.0", help="this script version")
	Arguments = Ap.parse_args()

	if Arguments.list:
		List()
	elif Arguments.download:
		Download()
	elif Arguments.update:
		Update()

if __name__ == '__main__':
	main(sys.argv[1:])
