% Rossler system
a = 0.2; b = 0.2; c = 4; 

%c=2.5, 1 limit cycle; c=5, chaos. observe period doubling in between

f = @(t,y) [-y(2) - y(3); y(1) + a*y(2); b + y(3)*(y(1) - c) ]; 

[t,y] = ode45(f,[0 10000],[1 1 1]);

figure(1)
plot3(y(:,1),y(:,2),y(:,3))

figure(2)
plot(y(:,1),y(:,2))