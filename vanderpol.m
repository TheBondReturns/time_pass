% vander pol (beautiful limit cycle)
mu = 0.5;
f = @(t,y) [y(2); -y(1) - mu*y(2)*(y(1)^2 -1)];

[t,y]= ode45(f,0:0.001:60,[10,10]);

plot(y(:,1),y(:,2))