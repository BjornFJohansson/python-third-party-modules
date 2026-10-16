function dydt=fedbatch(t,y)
global startflag t2 y2
if nargin==0;startflag=1;end
datapoints=1000;% Min nr of datapoints from ODE23s
% INSTRUCTION: Specify simulation after ENTER, DECLARE and EXTRACT
below.
% ENTER THE INITIAL CONDITIONS:
if startflag==1
tspan=[0 20];
% Simulation time span (hrs)
t=tspan(1);
% time for ODE-variables
t2=0;
% Time for other plotted variables
% DECLARE diff equation variables first !
names={'X','S','V'};
X=0.1;
% g/L
S=10;
% g/L
V=10;
% L
y=[X; S; V];
% Pack in a column vector
ymax=[20 10 15];
% Max values for the scale
% DECLARE other plotted variables (constants and from model)
names2={'F', 'mu'};
y2= [ NaN NaN];
% No inital values
ymax2=[0.1 1 ];
% Max values for the scale
% ENTER a legend (same order as names1 and names2 above).
legtxt= {'X (0-20)', 'S (0-10)','V (0-10)', 'F(0-0.1)', 'mu (0-
1)'};
% --------Do not change between dashed lines----
startflag=0;
opt=odeset('MaxStep',diff(tspan)/datapoints);
[tout,yout]=ode23s(mfilename,tspan,y,opt);
plot(tout,100*yout./ymax)
hold on
plot(t2,100*y2./ymax2)
figure(gcf)
hold off
set(gca, 'ylim', [0,100])
xlabel('time (h)')
ylabel( 'See scale in legend' )
legend(legtxt);
end


% EXTRACT THE VARIABLES FROM THE y-VECTOR (same order as above)
X=y(1);
S=y(2);
V=y(3);
% ENTER THE MODEL:
qSmax=1.4;
qm=0.04;
Yem=0.5;
Ks=0.01;
Si=500;
F=0;
% The feed rate
if t>6
% Time for feed start
F=0.05;
end
qS=qSmax*S/(S+Ks);
mu=(qS-qm)*Yem;
% ENTER mass balance equations
dXdt=-F/V*X+mu*X;
dSdt=F/V*(Si-S)-qS*X;
dVdt=F;
dydt=[dXdt;dSdt;dVdt];
% ------- Do not change below --------------
% Collect data for other plotted variables
t2=[t2;t];
y2=[y2;[F,mu]];
end
