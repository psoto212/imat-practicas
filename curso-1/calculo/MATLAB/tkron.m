function T = tkron(u,v)
%tkron Producto de Kronecker de dos tensores u y v
%   T=tkron(u,v)
%
%Input:
%   u,v : arrays multidimensionales de dimensiones a1x...xan y b1x...xbm
%Output:
%   T   : array de dimensión a1x...xanxb1x...xbm que contiene las
%         coordenadas del producto tensorial de u y v
%
%Autor:
%   David Alfaya
%
%Organización:
%   Grado en Ingeniería Matemática e Inteligencia Artifical (IMAT)
%   Departamento de Matemática Aplicada, ICAI
%   Universidad Pontificia Comillas

    if(length(size(v))==2 && min(size(v))==1)
        if(length(size(u))==2 && min(size(u))==1)
            % Si v es un vector columna y u también, producto matricial
            T=u(:)*v(:)';
        else
            % Si v es un vector columna pero u no, reajusta v como un
            % vector 1x1x...x1xd y multiplica u por dicho tensor usando
            % broadcasting
            T=u.*reshape(v,[ones(1,length(size(u))),length(v)]);
        end
    else
        if(length(size(u))==2 && min(size(u))==1)
            %Si u es un vector columna, es necesario linearizarlo antes de
            %multiplicar. Si v tiene dimensión d1x...xdn, reajusta v como
            %un tensor 1xd1x...xdn y multiplica u por él usando
            %broadcasting
            T=u(:).*reshape(v,[1,size(v)]);
        else
            %En otro caso, el producto puede hacerse directamente. Reajusta
            %v como un tensor 1x...x1xd1x...xdn, con tantos 1's como el
            %orden de u y multiplica por broadcasting.
            T=u.*reshape(v,[ones(1,length(size(u))),size(v)]);
        end
    end
end

