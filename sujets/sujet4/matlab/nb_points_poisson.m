function n = nb_points_poisson(lambda, duree)
  % Nombre de points d'un processus de Poisson d'intensité lambda dans [0, duree] :
  % on additionne des durées E(lambda) tant que la somme reste <= duree (loi P(lambda*duree)).
  n = 0;
  Z = -log(1 - rand) / lambda;            % inversion, 1 - rand évite log(0)
  while Z <= duree
    n = n + 1;
    Z = Z - log(1 - rand) / lambda;
  end
end
