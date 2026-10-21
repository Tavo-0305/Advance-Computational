Let $F(x): f_3 ° f_2 ° f_1 (x)$

Where $f_1 = Wx + b $, $f_2=(x_1^{2},...,x_n^{2})$, $\sum_{i=1}^{n} x_i$. 

With $W \in \mathbb{R}^{5 \times 5}$, $b$,$x$ $\in \mathbb{R}^{5}$. 

The we have: $x \rightarrow z = Wx + b \rightarrow y = z^{2} \rightarrow F = \sum_{} y$

Calculating the gradient with respect to W: 
$\frac{\partial F}{\partial W} = \frac{\partial F}{\partial y} \frac{\partial y}{\partial z} \frac{\partial z}{\partial W}$

$\frac{\partial F}{\partial W} = 2zx = 2(Wx+b)x^{T}$

And then with respect to b: 

$\frac{\partial F}{\partial b} = \frac{\partial F}{\partial y} \frac{\partial y}{\partial z} \frac{\partial z}{\partial b}$

$\frac{\partial F}{\partial W} = 2z = 2(Wx+b)$

See the code implementation in backprop.py