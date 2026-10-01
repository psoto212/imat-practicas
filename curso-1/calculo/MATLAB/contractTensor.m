function EV=contractTensor(T,i,j)
%contractTensor.m Calcula la contracción de un tensor en dos índices
%      EV=contractTensor(T,i,j) Calcula la contracción del tensor T en los índices i y j
%Se asume que 1<=i<j<=d, y que T es un array multidimensional de orden d
%
%Inputs:
%   T   : array d-dimensional que representa un tensor de orden d>=2
%   i   : índice de la primera componente
%   j   : índice de la segunda componente
%
%Outputs:
%   EV  : array (d-2)-dimensional
%
%Autor:
%   David Alfaya
%
%Organización:
%   Grado en Ingeniería Matemática e Inteligencia Artifical (IMAT)
%   Departamento de Matemática Aplicada, ICAI
%   Universidad Pontificia Comillas


    % Calcula el tamaño y orden de T
    ind=size(T);
    d=length(ind);
    % Calcula la lista de índices sobre los que no se contrae
    newind=ind([1:i-1,i+1:j-1,j+1:d]);
    %Reordena T para que los índices que deben contraerse sean los dos
    %primeros y los que no queden al final
    Tperm=permute(T,[i,j,1:i-1,i+1:j-1,j+1:d]);
    %Calcula la traza respecto a los dos primeros índices
    EV=0;
    for k=1:ind(i)
        EV=EV+Tperm(k,k,:);
    end
    if (d>3)
        %Si el tensor original tiene más de orden 3, se reescribe el
        %resultado como un tensor con las dimensiones adecuadas
        EV=reshape(EV,newind);
    else
        %En caso contrario, el tensor resultante tiene orden 0 o 1, con lo
        %que basta con linearizarlo
        EV=EV(:);
    end
end
