function G = turan_gen(n,r,filename)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
size = n/r;

if mod(n,r) ~= 0
    fprintf('INVALID INPUT')
    return
end


fileID = fopen(filename,'w');
fprintf(fileID,'N     // Directed\r\n');
fprintf(fileID,'N     // Weighted\r\n');
fprintf(fileID,'%d    // Number of Vertices\r\n', n);

G = ones(n,n);
for i=1:r
    G(i*size-size+1:i*size, i*size-size+1:i*size) = 0;
end

for i = 1:n
    degree = sum(G(i,:));
    fprintf(fileID,'%d    // Degree of vertex %d\r\n', degree,i);
    for j = 1:n
        if G(i,j) == 1
            fprintf(fileID,'%d\r\n', j);
        end;
    end;
end;

end