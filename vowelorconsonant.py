vox=input()
if(len(vox)==1):
	if(vox=='a' or vox=='A' or vox=='e' or vox=='E' or vox=='i' or vox=='I' or vox=='o' or vox=='O' or vox=='u' or vox=='U'):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("Invalid")
