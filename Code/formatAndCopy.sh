#!/bin/bash

#Script that takes the type of machine to load its SD files
#searchs for the sd cards in /dev , format them in the correct format
#mount them and copy the files

#BCN3D Technologies - April 2016
#Marc Cobler - Ostap Petrushchak

#Get the arguments of the command
#echo "$#"
if [[ $# -eq 1 ]]; then
	machine="$1"
else
	echo "Bad argument number, please verify"
fi

#echo "$machine"

cd /dev
sdlist=( $(ls sd[a-w][0-1] | tr " " "\n") )
numberOfSD=${#sdlist[@]}

echo "$numberOfSD"
if [ $numberOfSD -eq 0 ]; then
	echo -e "\e[1m\e[91m==============SD's not detected, please insert and retry============"
	sleep 2
	clear
	exit 1
fi

if [ "$machine" = "Sigma" ]; then
	echo "BCN3D Sigma"
	for sd in "${sdlist[@]}";
	do
		sudo rm -rf /mnt/sd/*
		sd2=${sd:0:3}
		echo "$sd"
		sudo umount /dev/$sd2 > /dev/null
		sudo parted -s /dev/$sd2 rm 1 > /dev/null
		sudo parted -s /dev/$sd2 rm 2 > /dev/null
		sudo parted -s /dev/$sd2 mkpart primary fat32 1s 100%
		sudo mkfs.vfat /dev/$sd -n BCN3D
		sudo mount /dev/$sd /mnt/sd
		sudo cp -rfv /home/pi/BCN3DSigma/* /mnt/sd/
		sudo umount /mnt/sd > /dev/null
	done
elif [ "$machine" = "Plus" ]; then
	echo "BCN3D Plus"
	for sd in "${sdlist[@]}";
	do
		sudo rm -rf /mnt/sd/*
		sd2=${sd:0:3}
		echo "$sd"
		sudo umount /dev/$sd2 > /dev/null
		sudo parted -s /dev/$sd2 rm 1 > /dev/null
		sudo parted -s /dev/$sd2 rm 2 > /dev/null
		sudo parted -s /dev/$sd2 mkpart primary fat32 1s 100%
		sudo mkfs.vfat /dev/$sd -n BCN3D
		sudo mount /dev/$sd /mnt/sd
		sudo cp -rfv /home/pi/BCN3DPlus/* /mnt/sd/
		sudo umount /mnt/sd > /dev/null
	done
elif [ "$machine" = "LCD" ]; then
	echo "Sigma LCD"
	for sd in "${sdlist[@]}";
	do
		#The micro SD from the LCD is a bit different. format is FAT and it needs a 
		#partition of less than 4Gb
		sudo rm -rf /mnt/sd/*
		sd2=${sd:0:3}
		echo "$sd"
		sudo umount /dev/$sd2 > /dev/null
		sudo parted -s /dev/$sd2 rm 1 > /dev/null
		sudo parted -s /dev/$sd2 rm 2 > /dev/null
		#Better to don't put a name on the format
		sudo parted -s /dev/$sd2 mkpart primary fat16 1s 500Mb
		sudo parted -s /dev/$sd2 align minimal 1
		sudo mkfs.vfat -I -F 16 /dev/$sd2
		sudo mount /dev/$sd2 /mnt/sd
		sudo cp -rfv /home/pi/BCN3DSigmaLCD/* /mnt/sd/
		sudo umount /mnt/sd > /dev/null
	done
elif [ "$machine" = "R" ]; then
	echo "BCN3DR"
	for sd in "${sdlist[@]}";
	do
		sudo rm -rf /mnt/sd/*
		sd2=${sd:0:3}
		echo "$sd"
		sudo umount /dev/$sd2 > /dev/null
		sudo parted -s /dev/$sd2 rm 1 > /dev/null
		sudo parted -s /dev/$sd2 rm 2 > /dev/null
		sudo parted -s /dev/$sd2 mkpart primary fat32 1s 100%
		sudo mkfs.vfat /dev/$sd -n BCN3D
		sudo mount /dev/$sd /mnt/sd
		sudo cp -rfv /home/pi/BCN3DR/* /mnt/sd/
		sudo umount /mnt/sd > /dev/null
	done
fi
