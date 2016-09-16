fileID = fopen('calibIR.txt','r');
formatSpec = '%f';
A  = fscanf(fileID,formatSpec)
t = 1 : size(A);
figure(1)
plot(t, A);

fileIDmeans = fopen('means.txt', 'r');
Nums = fscanf(fileIDmeans, formatSpec)
Means = [];
e = 1;
for n = 1 : 2 : length(Nums)
    Means(e) = (Nums(n) + Nums(n+1)) / 2;
    e = e + 1;
end

figure(2)
a = (2 : length(Means) + 1) - 27/16;
hold on
plot(a, Means.* (5/1023), '*');

plot(Distance, Output, 'o');

syms x
a = 289.3228;
b = -18.02785;
c = 39.33564;
d = -6.829414;
e = 0.4095285;
f = -0.008243875;
ezplot((a+b*x + c*x^2+d*x^3+e*x^4+f*x^5) .* (5/1023), [0, 20])

syms x
a = 0.1009671;
b = 0.9405964;
c = -0.118291;
d = 0.005815738;
e = -0.0001267703;
f = 0.000001019072;
ezplot((a+b*x + c*x^2+d*x^3+e*x^4+f*x^5), [0, 20])
axis([0, 20, 0, 5])