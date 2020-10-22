#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import re
import shutil

CONFLICT_REGEX = re.compile(' \(conflicted copy.*\)')
count = 0
total_conflict_count = 0
total_dir_count = 0
max_dir_count = 1000
matching_file_found = []
no_matching_file_found = []
for root, dirs, files in os.walk('.'):
	conflict_found = False
	conflict_count = 0
	for file in files:
		if "conflicted" in file:
			conflict_found = True
			conflict_count += 1
			conflicted_filename = file
			guessed_filename = CONFLICT_REGEX.sub('',conflicted_filename)
			if guessed_filename in files:
				matching_file_found.append((os.path.join(root,conflicted_filename), os.path.join(root,guessed_filename)))
			else:
				no_matching_file_found.append((conflicted_filename, guessed_filename))
	if conflict_found:
		total_dir_count += 1
		total_conflict_count += conflict_count
		print('-'*200)
		print(f"dir {total_dir_count}: {conflict_count} conflict(s) found:")
		print(f"\nROOT: {root}\n\nDIRS: {dirs}\n\nFILES: {files}\n")
	if total_dir_count > max_dir_count:
		break

print('*'*200)
print(f"{total_conflict_count} conflicts found in {total_dir_count} directories")
print(f"Matching files found: {len(matching_file_found)} | Files missing a match: {len(no_matching_file_found)}")
print('*'*200)
for cf, gf in matching_file_found:
	print(f"moving {cf} --> {gf}")
	try:
		shutil.move(cf,gf)	
	except PermissionError:
		print(f"PERMISSION DENIED. Continuing...")
print(f"All done. Good luck.")
