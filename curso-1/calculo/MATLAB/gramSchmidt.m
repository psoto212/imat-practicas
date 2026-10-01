function BON = gramSchmidt(g,B)
%gramSchmidt Algoritmo de ortonormalización de Gram-Schmidt
%Input:
%   g   : Producto escalar. Función que recibe dos vectores y devuelve un
%         real
%   B   : Base de vectores escritos en columnas
%Output:
%   BON : Base de vectores ortonormalizada

    
    BON=B; %Comenzamos tomando como base la original, B
    n=size(B,2); % El número de vectores es el número de columnas de B
    
    %Primero calculamos la base ortogonal
    for i=2:n
        %Cuando llegamos a este punto, BON(i)=B(i)
        %Al vector B(i) le restamos su proyección sobre los vectores
        %anteriores de la base BON(1)...BON(i-1)
        for j=1:i-1
            BON(:,i)=BON(:,i)-g(B(:,i),BON(:,j))/g(BON(:,j),BON(:,j))*BON(:,j);
        end
    end
    
    %Normalizammos el vector
    for i=1:n
        BON(:,i)=BON(:,i)/sqrt(g(BON(:,i),BON(:,i)));
    end
end

