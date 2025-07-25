from sandyie_read import read

file_path = "C:/Users/sanja/Downloads/regression.xlsx" # Put your PDF file path here
output = read(file_path)
print(output.head())
print(type(output))