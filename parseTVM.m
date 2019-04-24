% Supose A = 500 x 11 matrix

% Calculate Number of products and number of variables
lenX = 100;
[Nprod,Nvar] = size(A);
Nprod = Nprod / lenX;

% Initialize 3-dimensional matrix
out = zeros(lenX, Nvar, Nprod);

% Fill in 'out' Matrix
for i = 1:Nprod
  indexFirst = (lenX*(i-1))+1;
  indexSecond = lenX*i; 
  out(:,:,i) = A(indexFirst:indexSecond,:); 
