function poliedro(V,A)
%poliedro Dibuja un poliedro 3D a partir de una lista de vértices
%y una lista de aristas que los conectan
%Input:
%   vert  : Matriz n x 3. Cada fila contiene las coordenadas
%           3D de un vértice.
%   arist : Matriz m x 2. Cada fila es un vector [i,j] que
%           que representa que existe una arista entre el
%           vértice i y el vértice j de la lista.
%
%Autor:
%   David Alfaya
%
%Organización:
%   Grado en Ingeniería Matemática e Inteligencia Artifical (IMAT)
%   Departamento de Matemática Aplicada, ICAI
%   Universidad Pontificia Comillas

    %Creamos un gráfico nuevo
    figure(1);
    %Limpiamos el contenido
    clf;
    %Fijamos la vista, el rango de los ejes y su relación de aspecto para
    %que la figura no se deforme al variar las coordenadas de los puntos
    view(30,30);
    axis([-1,1,-1,1,-1,1]);
    daspect([1,1,1]);
    % Dibujamos cada arista del poliedro
    for i=1:length(A)
        segmento(V(A(i,1),:),V(A(i,2),:))
    end
end


function segmento(p,q)
%segmento Dibuja un segmento entre los puntos p y q
%Input:
%   p, q : Vectores 3D. Extremos del segmento.
    line([p(1);q(1)],[p(2);q(2)], [p(3);q(3)]);
end