## Proof that the gradient is perpendicular to a level curve


The final step taken in finding the tangent vector in `analyse_level_curves` performs the following simple step:

Say we have computed the gradient vector as:


$$
\nabla w = \langle a,b\rangle
$$

Then, the tangent vector can be written as:

$$
\langle -b,a\rangle
$$

The tangent vector has a slope equal to the negative reciprocal of the gradient's slope. But why is this the case? Here is a proof


Take a multivariable function:

$$
w=f(x,y)
$$

Now imagine we are moving along one of its level curves. We can describe our position using:

$$
x=x(t), y=y(t)
$$

Since we are moving along a level curve, the value of $w$ stays constant:

$$
w=f(x(t),y(t))=c
$$

where $c$ is some constant.

This means:

$$
\frac{dw}{dt}=0
$$

Using the multivariable chain rule:

$$
\frac{dw}{dt}
=
\frac{\partial w}{\partial x}\frac{dx}{dt}
+
\frac{\partial w}{\partial y}\frac{dy}{dt}
=
0
$$

Now let's say, at the point we are interested in we have gradient $\langle a,b\rangle$:

$$
\nabla w
=
\left\langle
\frac{\partial w}{\partial x},
\frac{\partial w}{\partial y}
\right\rangle
=
\langle a,b\rangle
$$

So we can rewrite the chain rule equation as:

$$
a\frac{dx}{dt}
+
b\frac{dy}{dt}
=
0
$$

Now rearrange:

$$
b\frac{dy}{dt}
=
-a\frac{dx}{dt}
$$

Dividing through gives:

$$
\frac{dy/dt}{dx/dt}
=
-\frac{a}{b}
$$


$$
\frac{dy}{dx}
=
-\frac{a}{b}
$$

The slope of the tangent to the level curve is therefore:

$$
-\frac{a}{b}
$$

The gradient vector is:

$$
\langle a,b\rangle
$$

Therefore, the slope is given by:

$$
\frac{b}{a}
$$

Multiplying the two slopes:

$$
\frac{b}{a}
\left(-\frac{a}{b}\right)
=
-1
$$

So the two slopes are negative reciprocals, meaning they are perpendicular.

This explains why the function can take:

$$
\langle a,b\rangle
$$

and turn it into:

$$
\langle -b,a\rangle
$$

Alternatively, we can also see that this is true with the dot product:

$$
\langle a,b\rangle
\cdot
\langle -b,a\rangle
=
-a b + ab
=
0
$$

Two vectors are perpendicular if their dot product is $0$, (provided the gradient is non-zero)

Therefore the gradient is normal to the level curve:

$$
\nabla w \perp \text{level curve}
$$

Q.E.D.