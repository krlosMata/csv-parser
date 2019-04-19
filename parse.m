% This script aims to load several .csv files and turn it into a 3-dimensional matrix array
path = 'f:\project\dataset'
files = dir(strcat(path,'\*.csv'))
L = length(files);
for i=1:L
   image{i}=csvread(strcat(path,'\',file(i).name));
end