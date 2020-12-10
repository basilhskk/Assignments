v = 'GTAGGCTTAAGG';
w = 'TAGATA';

n = length(v);
m = length(w);

matrix = zeros(m+1,n+1);
paths = zeros(m+1,n+1);

for j=2:m+1
    for i=2:n+1
        % Set the list of predecessors
        pred = [matrix(j-1,i-1),matrix(j,i-1)];
        
        % Check for equality
        if v(i-1) == w(j-1)
            pred(1) = pred(1) + 1;    
        else
            pred(1) = pred(1) - 1;
        end
        % Subtract because of left-to-right move
        pred(2) = pred(2) - 1;
        
        % Find greater predecessor
        if pred(1) ~= pred(2)
            [greater,pos] = max(pred);
            matrix(j,i) = greater;
            paths(j,i) = pos;
        else
            matrix(j,i) = pred(1);
            paths(j,i) = 1;
        end
    end
end

% Find max of the last row
[last_row_max,last] = max(matrix(end,:));

% Remove unwanted rows and columns
matrix = matrix(2:end,2:last);
paths = paths(2:end,2:last);
% Resize v
v = v(1:last-1);
% Reset n
n = length(v);
% Create a new w
new_w = [];

% Backtracking
pos = last - 1;
matches = [];
j = m;
while j >=1
    if v(pos) == w(j)
        matches = [matches,'|']; %#ok<*AGROW>
    else   % v(pos) ~= w(j)
        matches = [matches,'X'];
    end
    
    if paths(j,pos) == 1
        j = j - 1;
        new_w = [new_w,v(pos)];
    else   % In case of right-to-left move
        new_w = [new_w,'-'];
    end
    
    % Continue in the next symbol
    pos = pos - 1;
end

% Keep only the matched part
v = v(pos:last-1);
% Flip the order in matches and new
new_w = fliplr(new_w);
matches = fliplr(matches);

disp(v);
disp(matches);
disp(new_w);