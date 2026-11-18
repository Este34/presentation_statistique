% Sujet 3 : gradient simple et recuit simulé (Matlab ou Octave)
h  = @(x) x.^2 + 3*x.*cos(x);
dh = @(x) 2*x + 3*cos(x) - 3*x.*sin(x);
a = -8*pi;  b = 8*pi;  N = 1000;

% Q1 : h sur 5000 points, minimum de la grille
y = linspace(a, b, 5000);  hy = h(y);
[m, i] = min(hy);
xs = fzero(dh, [-1 0]);                  % minimum global exact
fprintf('Q1 grille : h(%.4f) = %.4f ; x* = %.4f\n', y(i), m, xs);

% Q2 : gradient simple, pas 0,025/n
xg = zeros(1, N + 1);  xg(1) = 7.5;
for n = 1:N
  xg(n + 1) = xg(n) - 0.025/n * dh(xg(n));
end
fprintf('Q2 gradient : x_N = %.4f, h = %.4f\n', xg(end), h(xg(end)));

% Q3 : un recuit, T0 = 500, alpha = 0,99
if exist('OCTAVE_VERSION', 'builtin'), rand('twister', 2026); else, rng(2026); end
xr = recuit(h, 7.5, N, 500, 0.99, a, b);
fprintf('Q3 recuit : x_N = %.4f, h = %.4f\n', xr(end), h(xr(end)));

% Q4 : comparaison chiffrée, écart au minimum global h(x_N) - h(x*)
fprintf('Q4 écart : gradient %.4f, recuit %.2e\n', h(xg(end)) - h(xs), h(xr(end)) - h(xs));

% Figure : h, trajectoires du gradient et du recuit, sauvée en SVG
figure('position', [100 100 1000 330]);
plot(y, hy, 'color', [0.42 0.42 0.42]); hold on
plot(xr, h(xr), '.', 'color', [0.52 0.15 0.47], 'markersize', 6);
plot(xg, h(xg), '.', 'color', [0.88 0.03 0.09], 'markersize', 8);
plot(xs, h(xs), 'ko', 'markersize', 3, 'markerfacecolor', 'y'); hold off
xlabel('x'); ylabel('h(x)'); xlim([a b]); ylim([-100 900]);
lg = legend('h', 'recuit (1 lancer)', 'gradient', 'minimum global', 'location', 'north', 'orientation', 'horizontal');
set(lg, 'fontsize', 15);
title('Octave : gradient (piégé en 8,66) et recuit (global)');
set(gca, 'fontsize', 16);
print('-dsvg', 'octave_resultat.svg');
