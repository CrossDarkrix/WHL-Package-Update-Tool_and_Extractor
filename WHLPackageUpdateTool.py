#!/usr/bin/env python3

"""
Name : whl Package Update Tool(whl packages only)
Author: DarkRix
Version: 3.6
"""

import json, sys, subprocess, argparse, concurrent.futures
from time import time as ti
from os import chdir as cd, getcwd as pwd

currentdir = pwd()

def pip_json():
	global json_data
	_process = subprocess.Popen([sys.executable, '-m', 'pip', 'list', '--outdated', '--format=json'], stdout=subprocess.PIPE)
	outputs, _ = _process.communicate()
	json_data = json.loads(outputs.decode('utf-8'))

def pip(command):
	_process = subprocess.Popen([sys.executable, '-m', 'pip'] + command, stdout=subprocess.PIPE)
	outputs, _ = _process.communicate()
	return outputs.decode('utf-8')

def List():
	start = ti()
	print("Getting Update Package List....")
	with concurrent.futures.ThreadPoolExecutor() as EXC:
		EXC.submit(pip_json())
	print("\n########## Package List ##########\n")
	for i in range(int(len(json_data))):
		Package_Name = json_data[i]['name']
		File_Type = json_data[i]['latest_filetype']
		print("  ◆ " + Package_Name + ' (Install Type: ' + File_Type + ')')
	print("\n##################################\n")
	elst = ti() - start
	print("\nElapsed Time:{0}".format(round(elst)) + "[sec]")

def Download():
	start = ti()
	print("Getting Update Package List....")
	with concurrent.futures.ThreadPoolExecutor() as EXC:
		EXC.submit(pip_json())
	print("\n########## Package List ##########\n")
	for i in range(int(len(json_data))):
		cd(currentdir)
		Package_Name = json_data[i]['name']
		File_Type = json_data[i]['latest_filetype']
		print("  ◆ " + Package_Name + ' (Install Type: ' + File_Type + ')')
	print("\n##################################\n")

	for i in range(int(len(json_data))):
		cd(currentdir)
		Package_Name = json_data[i]['name']
		File_Type = json_data[i]['latest_filetype']

		if File_Type == 'sdist':
			Package_Name = """"""
		else:
			pass
		if Package_Name == '':
			pass
		else:
			with concurrent.futures.ThreadPoolExecutor() as EXC2:
				print(concurrent.futures.Future.result(EXC2.submit(pip, ['download','--no-deps','--no-cache-dir',Package_Name])))
	elst = ti() - start
	print("\nElapsed Time:{0}".format(round(elst)) + "[sec]")
	print("All Wheel Packages Downloaded.")

def Update():
	start = ti()
	print("Getting Update Package List....")
	with concurrent.futures.ThreadPoolExecutor() as EXC:
		EXC.submit(pip_json())
	for i in range(int(len(json_data))):
		cd(currentdir)
		Package_Name = json_data[i]['name']
		File_Type = json_data[i]['latest_filetype']

		if File_Type == 'sdist':
			Package_Name = """"""
		else:
			pass
		if Package_Name == '':
			pass
		else:
			with concurrent.futures.ThreadPoolExecutor() as EXC3:
				print(concurrent.futures.Future.result(EXC3.submit(pip, ['install', '--upgrade','--no-deps', Package_Name])))
		cd(currentdir)
	elst = ti() - start
	print("\nElapsed Time:{0}".format(round(elst)) + "[sec]")
	print("All Wheel Packages Updated.")

def main(argument):
	Ap = argparse.ArgumentParser()

	Ap.add_argument("-l", "--List", action="store_true", help="only listup update lists")
	Ap.add_argument("-d", "--Download", action="store_true", help="only download update packages")
	Ap.add_argument("-u", "--Update", action="store_true", help="only update packages")
	Ap.add_argument("-v", "--version", action="version", version="3.6", help="this script version")
	Ap.add_argument("list", nargs='?', help="only listup update lists")
	Ap.add_argument("download", nargs='?', help="only download update packages")
	Ap.add_argument("update", nargs='?', help="only update packages")
	Arguments = Ap.parse_args()

	if Arguments.List:
		List()
	elif Arguments.Download:
		Download()
	elif Arguments.Update:
		Update()
	elif Arguments.list == 'download' and Arguments.download == None:
		Download()
	elif Arguments.list == 'update' and Arguments.update == None:
		Update()
	elif Arguments.list == 'list':
		List()

if __name__ == '__main__':
	main(sys.argv[1:])

