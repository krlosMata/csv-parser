% Supose A = 500 x 11 matrix

% Calculate Number of products and nuumber of variables
lenX = 100; % We supose normalization of 100 samples
[Nprod,Nvar] = size(A);
Nprod = Nprod / lenX;

% Initialize 3-dimensional matrix
out = zeros(Nprod, Nvar, lenX);

% Fill in 'out' Matrix
for i = 1:lenX
  indexFirst = (Nprod*(i-1))+1;
  indexSecond = Nprod*i; 
  out(:,:,i) = A(indexFirst:indexSecond,:); 
