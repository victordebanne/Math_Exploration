# Calculatrice_Complexe

*Ce code et ce texte visent a manipuler experimentalement la formule d'Euler, sans jamais l'utiliser. 
il serait evidemement plus simple de calculer*

$$
e^z \quad \text{comme} \quad e^{Re(z)} \times \left(\cos\left(Im(z)\right) + i \ \sin\left(Im(z)\right)\right)
$$

# Représentation matricielle

On peut manipuler les nombers complexes à la fois intuitivement et informatiquement en utilisant la forme matricielle de $i$.

$$
i = 
\begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}
$$

Cette représentation permet de manipuler des nombres complexes de cette manière : 

$$
z = 
\begin{pmatrix}
Re(z) & -Im(z) \\
Im(z) & Re(z)
\end{pmatrix}
$$

Etant donné que le complexe $a + ib$ avec 

$$
A = 
a \times ID = 
a \times
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix} = 
\begin{pmatrix}
a & 0 \\
0 & a
\end{pmatrix} 
$$

et 


$$
iB =
i \times b \times ID = 
i \times B = 
\begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}
\times
\begin{pmatrix}
b & 0 \\
0 & b
\end{pmatrix} = 
\begin{pmatrix}
0 & -b \\
b & 0
\end{pmatrix}
$$

d'ou $z = a + ib$ peut se représenter de cette manière

$$
z = 
\begin{pmatrix}
a & -b \\
b & a
\end{pmatrix}
$$

# Séries de Taylor

De cette manière, nous pouvons calculer les séries de Taylor pour les fonctions suivantes : $exp(z), \ cos(z), \ sin(z), \ log(z)...$

nous allons noter $Z$ la matrice représentant le complexe $z$.

$$
e^z = \sum_{k=0}^{\infty} \frac{Z^k}{k!}  
$$

J'ai choisi de calculer $Z^k$ à l'aide du binome de newton. 

$$
\begin{align}
Z^k &= 
\sum_{k = 0}^{n} 
\begin{pmatrix} 
n \\ 
k 
\end{pmatrix}
\ Re(Z)^k Im(Z)^{n-k} \\
&= 
\sum_{k = 0}^{n} 
\begin{pmatrix} 
n \\ 
k 
\end{pmatrix} 
\ (a^k \times ID) \times (b^{n-k} \times i{n-k})
\end{align}
$$

il n'est pas nécessaire de calculer $i^k$ avec $A^k = PD^kP^{-1}$.
étant donné que i est une matrice de rotation $\pi / 2$ : 

$$
i^1 = 
\begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix} \quad
i^2 = 
\begin{pmatrix}
-1 & 0 \\
0 & -1
\end{pmatrix} \quad
i^3 = 
\begin{pmatrix}
0 & 1 \\
-1 & 0
\end{pmatrix} \quad
i^4 = 
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix} \quad
i^5 = i^1
$$

on a alors $i^k = i^{\ k \mod 4}$

on peut alors calculer facilement la série de Taylor pour $Z$ et un $N$ défini pour chacune des fonctions : 

$$
\begin{align}
e^z &= \sum_{k=0}^{N} \frac{Z^k}{k!}\\
sin(z) &= \sum_{k=0}^{N} \frac{k[n \mod 4] \ Z^k}{k!} \quad \text{avec} \quad k = \[0, 1, 0, -1\]\\
cos(z) &= \sum_{k=0}^{N} \frac{k[n \mod 4] \ Z^k}{k!} \quad \text{avec} \quad k = \[1, 0, -1, 0\]  \\ 
\end{align}
$$

On peut simplifier algorithmiquement de sorte à ne pas faire les multiplications par $0$. 

$$
\begin{align}
sin(z) &= \sum_{k=0}^{N} \frac{(-1)^k \ Z^{2k + 1}}{(2k + 1)!} \\
cos(z) &= 1 - \sum_{k=1}^{N} \frac{(-1)^{k + 1} \ Z^{2k}}{(2k)!} \\
\end{align}
$$

# Démonstration de la formule d'Euler

à partir d'ici, il est possible de démontrer la formule d'Euler en utilisant les puissances de $i$ ainsi que les séries de Taylor pour le sinus et le cosinus. 
la puissance de $Z$ ne nécessite plus le binome de newton étant donné qu'il n'y a pas de partie réelle. 
on pose $z = ix$ les puissances de $z$ deviennet donc comme vu précédemment : 

$$
z^k = (x \ i)^k = x^k \ i^{\ k \mod 4}
$$

il y a deux cas : 
- quand la puissance est paire
  
$$
z^{2k} = (-1)^{k}\ x^{2k}
$$

- quand la puissance est impaire
  
$$
z^{2k + 1} = (-1)^{k}\ i\ x^{2k+1}
$$

on a donc la série de Taylor pour l'exponentielle : 

$$
\begin{align}
e^{i\ x} &= \sum_{k=0}^{\infty} \frac{(i\ x)^k}{k!}\\
&= \sum_{k=0}^{\infty} 
\frac{(-1)^{k}\ x^{2k}}{(2k)!}\\ + 
\sum_{k=0}^{\infty} 
\frac{(-1)^{k}\ i\ x^{2k+1}}{(2k + 1)!}\\ 
&\ \\
&\ \\
&\text{première somme :}\\
&\sum_{k=0}^{\infty} 
\frac{(-1)^{k}\ x^{2k}}{(2k)!}\\ 
&= 1 - \sum_{k=1}^{\infty}
\frac{(-1)^{k}\ x^{2k}}{(2k)!}\\ 
&= \cos(x) \quad \text{par identification de la série de Taylor}\\
&\ \\
&\ \\
&\text{deuxième somme :}\\
&\sum_{k=0}^{\infty} 
\frac{(-1)^{k}\ i\ x^{2k+1}}{(2k + 1)!}\\ 
&= i\ \sum_{k=0}^{\infty} 
\frac{(-1)^{k}\ x^{2k+1}}{(2k + 1)!}\\ 
&= i\ \sin(x) \quad \text{par identification de la série de Taylor}\\
&\ \\
&\ \\
&\text{donc : }\\
&e^{i\ x} = \cos(x) + i\ \sin(x)\\
\end{align}
$$








