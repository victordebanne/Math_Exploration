# Calcul des puissances réelles positives sans exponentielle ni logarithme

Mon idée ici est d'explorer le calcul des puissances positives ou nulles de x par des methodes ne faisant pas intervenir l'exponentielle ni le logarithme. 
Le calcul des puissances entières positives est un problème simple à résoudre. il s'agit simplement de multiplications itératives sur la base. 

$$ 
\begin{align}
\text{pour} \quad n \in \mathbb{N} \\
x^n = 
\begin{cases}
\prod_{1}^n x \quad \text{pour} \quad n > 0 \\
1 \quad \text{sinon}
\end{cases}
\end{align}
$$

```python
def power_int(x, n):
    total = 1
    for i in range(1, n + 1):
        total *= x
    return total
```

pour des puissances non-entières, la solution est moins triviale. 

## Intuitions 

Ma première intuition est de décomposer l'exposant en partie entière et partie fractionnaire.

$$ 
\begin{align}
\text{on peut noter}\\
&x^k = x^n \cdot x^l \\
\text{avec} \\
&k, \quad \text{un réel positif ou nul} \\
&n = \lfloor k \rfloor \quad \text{(la partie entière de k)}\\
&l = k - \lfloor k \rfloor \quad \text{(la partie fractionnaire de k)}
\end{align}
$$

Ma seconde intuition est le calcul des racines. 

$$
\begin{align}
\sqrt{x} = y \quad \text{pour} \quad y^2 = x \\
\text{on peut généraliser} \\
x^{1/k} = y \quad \text{pour} \quad y^k = x \\
\end{align}
$$

on peut donc considérer $x^l$ comme une racine $l-ième$ de $x$ et la trouver grace à 

$$
x^l = y \quad \text{pour} \quad y^{\frac{1}{l}} = x
$$

On peut effectuer cette recherche de plusieurs façon. ici j'ai choisi une methode par dichotomie.

```python
def dichotomie(x, exp):
    min_val = 0
    max_val = max(x, 1)
    while True:
        mid = (max_val + min_val) / 2
        f = power_int(mid, exp)
        if abs(x - f) < 0.00001 : 
            return mid
        if f > x : 
            max_val = mid
        elif f < x : 
            min_val = mid
```


à nouveau, on peut noter 

$$ 
\begin{align}
&y^{\frac{1}{l}} = y^{\lfloor \frac{1}{l} \rfloor} \cdot y^{\frac{1}{l} - \lfloor \frac{1}{l} \rfloor}  \\
\text{ou} \\
&y^{k_2} = y^{n_2} \cdot y^{l_2}  \\
\text{avec} \\
&k_2 = \frac{1}{l} \\
&n_2 = \lfloor k_2 \rfloor \quad \text{(la partie entière de k)}\\
&l_2 = k_2 - \lfloor k_2 \rfloor \quad \text{(la partie fractionnaire de k)}
\end{align}
$$

il y a donc une partie fractionnaire que l'on peut calculer à chaque fois afin d'afiner l'approximation de notre puissance. 

## Structure

on peut construire une ligne recursive de cette manière : 

$$
x^{k_1} = x^{n_1} \times
\begin{cases}
y \quad \text{pour} \quad y^{k_2} = y^{n_2} \times 
\begin{cases} z \quad \text{pour} \quad z^{k_3} = z^{n_3} \times 
\begin{cases}
\cdots \times \begin{cases} \cdots \end{cases} \\
= z
\end{cases} \\ 
= y \end{cases}\\
= x
\end{cases}
$$ 

$$
\begin{align}
\text{avec}\\
&k_1 = k\\
&k_{n+1} = \frac{1}{l_n} \\
\end{align}
$$

## Code

la fonction finale $PowerFloat(x, k)$, visant à cacluler les puissances réelles d'un nombre se définit donc de cette façon : 

$$
\begin{align}
PowerFloat(x, k) &= 
x^{\lfloor k \rfloor} \cdot Dichotomie(x, \frac{1}{k - \lfloor k \rfloor})\\
\text{et}\\
Dichotomie(x, k) &=
y \quad \text{pour} \quad PowerFloat(y,k) = x
\end{align}
$$

J'ai rajouté un controle de récursion et une précision de la partie fractionnaire. 

```python
def dichotomie(x, exp, recursion):
    min_val = 0
    max_val = max(x, 1)
    while True:
        mid = (max_val + min_val) / 2
        f = power_float(mid, exp, recursion)
        if abs(x - f) < 0.00001 : 
            return mid
        if f > x : 
            max_val = mid
        elif f < x : 
            min_val = mid
        
def power_float(x, k, recursion = 4):
    n = int(k)
    l = k - n
    
    if l < 0.01:
        return power_int(x, n)
    if recursion <= 0 :
        return power_int(x, n)
    else :
        global i
        i += 1
        return power_int(x, n) * dichotomie(x, 1/l, recursion - 1)
```

## Résultats

avec 
```python
Y = [power_float(2, i/1000) for i in range(0, 1000)]
Y2 = [2 ** (i/100) for i in range(0, 100)]
Y3 = [Y2[i] - Y[i] for i in range(len(Y))]

X = list(range(len(Y)))

plt.plot(X, Y)
plt.show()
plt.plot(X, Y2)
plt.show()
plt.plot(X, Y3)
plt.show()
```

l'erreur entre ma fonction et la fonction de la librairie standard de Python montre une structure particulière. 
on remarque pour une faible récursivité (1 - 2) des motifs en dent de scie avec un maximum autour de 0.6 
ces motifs se resserent en pics pour une recursivité plus grande (4 - 5)

```python
moyenne erreur recursion 1 base 2 =  -0.16911906647413347 
moyenne erreur recursion 1 base 3 =  -0.16911906647413347 
moyenne erreur recursion 2 base 2 =  0.02354893517763045
moyenne erreur recursion 2 base 3 =  0.02354893517763045
moyenne erreur recursion 3 base 2 =  -0.005009817359143231
moyenne erreur recursion 3 base 3 =  -0.005009817359143231
moyenne erreur recursion 4 base 2 =  0.0009713704612913387
moyenne erreur recursion 4 base 3 =  0.0009713704612913387
moyenne erreur recursion 5 base 2 =  -0.0002475397559938175
moyenne erreur recursion 5 base 3 =  -0.0002475397559938175
moyenne erreur recursion 6 base 2 =  4.529547960188562e-05
moyenne erreur recursion 6 base 3 =  4.529547960188562e-05
```


on remarque que l'erreur ne dépend pas de la base (comme on peut s'y attendre)

elle resemble a une suite alternée qui tend vers 0. 

## Interprétation et conclusion

Ce code n'est pas très interessant du point de vu de l'optimisation. en effet, les recursions ammènent une compléxité exponentielle. Par contre la structure récursive sous jacente de la puissance ma interessé. 
Il reste pour l'instant beaucoup à explorer, sur la structure de l'erreur qui je pense est digne d'interet. mais aussi des points bloquants pour l'algorithme (0.749 par exemple) 

$$
k = \lfloor k \rfloor + (k - \lfloor k \rfloor) \quad \text{une partie entière et une partie fractionnaire}\\
$$

$$
k - \lfloor k \rfloor = \frac{1}{\frac{1}{k - \lfloor k \rfloor}} \quad \text{comme} \quad k - \lfloor k \rfloor < 0, \frac{1}{k - \lfloor k \rfloor} > 0\\
$$

$$
\frac{1}{k - \lfloor k \rfloor} = \lfloor \frac{1}{k - \lfloor k \rfloor} \rfloor + (\frac{1}{k - \lfloor k \rfloor} - \lfloor \frac{1}{k - \lfloor k \rfloor} \rfloor) \\
$$


$$
\frac{1}{k - \lfloor k \rfloor} - \lfloor \frac{1}{k - \lfloor k \rfloor} \rfloor = \frac{1}{\frac{1}{\frac{1}{k - \lfloor k \rfloor} - \lfloor \frac{1}{k - \lfloor k \rfloor} \rfloor}} \\
$$

$$
k = \lfloor k \rfloor + \frac{1}{\lfloor \frac{1}{k - \lfloor k \rfloor} \rfloor + \frac{1}{\frac{1}{\frac{1}{k - \lfloor k \rfloor} - \lfloor \frac{1}{k - \lfloor k \rfloor} \rfloor}}} \\
$$

$$
\cdots
$$



`
