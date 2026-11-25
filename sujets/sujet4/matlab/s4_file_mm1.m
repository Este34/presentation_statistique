% Sujet 4 : loi de Poisson par comptage et file M/M/1 (Matlab ou Octave)
if exist('OCTAVE_VERSION', 'builtin'), rand('twister', 2026); else, rng(2026); end

% Simulation Q2 : P(4) en comptant les sommes d'exponentielles <= 1
T = 10000;  N = zeros(1, T);
for i = 1:T
  N(i) = nb_points_poisson(4, 1);
end
fprintf('P(4) : moyenne %.4f, variance %.4f\n', mean(N), var(N));

% Q2 et Q5 : file M/M/1, lambda = 100, mu = 120, 5 minutes, file vide au départ
lambda = 100;  mu = 120;  duree = 300;  rho = lambda / mu;
Ta = zeros(1, 40000);  L = zeros(1, 40000);
t = -log(1 - rand) / lambda;  l = 0;  n = 0;
while t <= duree
  n = n + 1;  Ta(n) = t;  L(n) = l;
  s = -log(1 - rand) / lambda;            % T(n+1) - T(n), loi E(lambda)
  A = nb_points_poisson(mu, s);           % services potentiels, loi P(mu*s)
  l = max(0, l + 1 - A);                  % récurrence de la Q1
  t = t + s;
end
Ta = Ta(1:n);  L = L(1:n);
fprintf('n = %d clients, file max %d\n', n, max(L));
fprintf('E[L]   = %.4f (théorie %.4f)\n', mean(L), rho / (1 - rho));
fprintf('Var L  = %.4f (théorie %.4f)\n', var(L), rho / (1 - rho)^2);
fprintf('P(L=0) = %.4f (théorie %.4f)\n', mean(L == 0), 1 - rho);
fprintf('P(L>5) = %.4f (théorie %.4f)\n', mean(L > 5), rho^6);

% Figure : trajectoire et loi de L comparée à (1 - rho) rho^k, sauvée en SVG
k = 0:40;  freq = histc(L, k) / n;
figure('position', [100 100 1100 400]);
subplot(1, 2, 1);
plot(Ta, L, 'color', [0.52 0.15 0.47]);  hold on
plot([0 duree], [1 1] * rho / (1 - rho), '--', 'color', [0.88 0.03 0.09], 'linewidth', 2);  hold off
xlabel('temps (s)');  ylabel('L_n');
set(gca, 'fontsize', 12);
subplot(1, 2, 2);
semilogy(k(freq > 0), freq(freq > 0), 'o', 'color', [0.52 0.15 0.47], 'markerfacecolor', [0.52 0.15 0.47], 'markersize', 4);  hold on
semilogy(k, (1 - rho) * rho.^k, '-', 'color', [0.88 0.03 0.09], 'linewidth', 2);  hold off
xlabel('k');  ylabel('P(L_n = k)');
lg = legend('simulation', 'théorie');  set(lg, 'fontsize', 11);
set(gca, 'fontsize', 12);
print('-dsvg', 'octave_resultat.svg');
