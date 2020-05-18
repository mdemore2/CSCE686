function G = graph_gen(n, filename)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
fileID = fopen(filename,'w');
fprintf(fileID,'N     // Directed\r\n');
fprintf(fileID,'N     // Weighted\r\n');
fprintf(fileID,'%d    // Number of Verticies\r\n', n);

G = round(rand(n));
G = triu(G) + triu(G,1)';
G = G - diag(diag(G));

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

