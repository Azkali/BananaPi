#!/usr/bin/env python3

import os
import azip
from shutil import copyfile as copyf
from git import Git as git
from subprocess import run as run

packagesInstallState = False
configInstallState = False
rebootState = False
finish = False

repo = 'git://github.com/Azkali/Pi0W-Audio-and-RetroGaming.git'
repoName = os.path.abspath(os.path.splitext(repo.split('/')[4])[0])

packages = {
		'libs' : 	['libdbus-1-dev', 'libglib2.0-dev',
					'libudev-dev', 'libical-dev', 'libreadline-dev',
					'libpopt-dev', 'libdaemon-dev ', 'libconfig-dev',
					'libavahi-client-dev ', 'libasound2-dev',
					'libatlas-base-dev','libtool' ,'libssl-dev', 'libnss-mdns'],
		
		'tools' : 	['automake', 'autoconf', 'xmltoman',
					'git', 'lsb-release', 'build-essential',
					'iw', 'wireless-tools', 'rng-tools'],
		
		'binaries' :  ['bluealsa', 'lxde' ,'mpd' ,'bluez', 'bluez-alsa',
					'mplayer', 'mplayer-gui', 'alsa-base', 'vim',
					'avahi-daemon', 'minidlna', 'raspi-config',
					'emulationstation','dnsmasq', 'hostapd', 'mopidy'],
}


def installPackages():
		
	""" Takes a package object/dict to be installed. 
	Return True if Ok else False and print the error """
	
	def localRun(*aptArgs):

		""" Take one or several list and install them with subprocess"""

		try:
			run(['sudo', 'apt', 'get', 'update', '&&', 'sudo', 'apt', 'get', 'upgrade', '-y'], shell=True, capture_output=True)

			for arg in aptArgs:
				print(arg)
				run(['sudo', 'apt', 'get', 'install', arg, '-y'], shell=True, capture_output=True)

		except Exception as exp:
			print(exp)
			return False

		else:
			return True

	try:
		for keys, values in packages.items():
			if localRun(' '.join(packages[keys])):
				print('\n\nSuccessfully installed all Packages !')

	except Exception as exp:
		print(exp + ' \nFound error during Package installation please try manualy install them !')
		return False

	else:
		packagesInstallState = True
		return True


def addConfigToFs():

	""" Move the acquired configuration 
	from downloadConfigGit() to the Filesystem
	and make a backup of each file if exists """

	def downloadFsConfig():

		""" Downloads all required config 
		file for the system return path"""

		try:
			git('.').clone(repo)

		except Exception as exp:
			print(exp)
			return False

		else:
			os.chdir(repoName)
			print('RepoPath : ' + repoName)
			return repoName

	def bckupCfg():

		""" Make a zip of all current configuartions
		returns True if success otherwise False """

		try:
			azip.makeZip('/etc', '.')
			azip.makeZip('/usr', '.')
			azip.makeZip('/boot/config.txt', '.')
			azip.makeZip('/boot/cmdline.txt', '.')
			
		except Exception as exp:
			print(exp)
			return False
			
		else:
			return True

	try:
		bckupCfg()

		if not os.path.exists(repoName):
			path = downloadFsConfig()

		else:
			os.chdir(repoName)
			path = repoName


		for dirname, dirnames, filenames in os.walk(path):
			# print path to all subdirectories first.
			for subdirname in dirnames:
				if 'root' in dirname:
					print(os.path.join(dirname, subdirname))
					print(subdirname)
					copyf(os.path.abspath(subdirname), '/')

			# print path to all filenames.
			# for filename in filenames:
			# 	print(os.path.join(dirname, filename))

			# Advanced usage:
			# editing the 'dirnames' list will stop os.walk() from recursing into there.
			if '.git' in dirnames:
				# don't go into any .git directories.
				dirnames.remove('.git')

	except Exception as exp:
		print(exp)
		return False
	
	else:
		configInstallState = True
		return True


def setOwnerNPerm():
	
	""" Set correct owner and permissions for config files 
	returns True if success otherwise False"""

	pass

def resizeSDCard():

	def resizeBoot():
		""" resize boot partition for RT_Kernel """

		pass

	def resizeRoot():
		""" resize root partition to half the his available state 
		And create a new one aside for usb mass gadget/datas/samba_share 
		with the empty space """

		pass

def reboot():

	""" Sync and Reboot system """
	
	def checkForErrorOnReboot():

		""" On reboot Check for errors in systemctl, 
		journalctl, and dmesg.
		If these errors are related 
		to previously installed packages
		or configs restore conflicted config 
		from backed up zip """

		pass

	try:
		run(['sudo', 'sync', '&&', 'sudo ', 'reboot'], shell=True, capture_output=True)
		# checkForErrorOnReboot()

	except Exception as exp:
		print(exp)
		return False

	else:
		return True

# def exceptTry(cmd, err = ''):
# 	try:
# 		cmd
# 	except Exception as exp:
# 		print(exp + err)
# 		return False
# 	else:
# 		return True

def main():
	try:
		if not packagesInstallState:
			installPackages()

		if not rebootState:
			reboot()

		if not configInstallState:
			addConfigToFs()

	except  Exception as exp:
		print(exp)
		return False

	else:
		finish = True
		return True

if __name__ == "__main__":
	main()