#! /usr/bin/env python3
# coding: utf-8

import argparse
import pdb
import os

import csv_analysis as ana_csv
import xml_analysis as ana_xml

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--extension", help="Type of the file to analyse. CSV of XML ?")
	return parser.parse_args()

def launch_analysis(data_file):
	directory = os.path.dirname(os.path.dirname(__file__))

if __name__ == "__main__":
	args = parse_arguments()
	if args.extension == "csv":
		ana_csv.launch_analysis('current_mp.csv')
	elif args.extension == "xml":
		ana_csv.launch_analysis('SysceronBrut.xml')