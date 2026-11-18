function x = recuit(h, x0, N, T0, alpha, a, b)
% Recuit simulé : z ~ U[x_n - pi/2, x_n + pi/2], T_n = T0 * alpha^n.
% On accepte z si h baisse, sinon avec la probabilité exp(-(h(z) - h(x_n)) / T_n).
  x = zeros(1, N + 1);  x(1) = x0;  hx = h(x0);
  for n = 1:N
    T = T0 * alpha^n;
    z = x(n) - pi/2 + pi*rand;          % loi instrumentale g_n
    u = rand;
    x(n + 1) = x(n);                    % par défaut : z refusé
    if z >= a && z <= b                 % hors de [-8pi, 8pi] : refusé
      hz = h(z);
      if hz <= hx || u < exp(-(hz - hx) / T)
        x(n + 1) = z;  hx = hz;         % z accepté
      end
    end
  end
end
