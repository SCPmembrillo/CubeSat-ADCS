# Kinematics & Dynamics

## Dynamics
The main principle behind reaction wheels is the **conservation of angular momentum**, which is the sum of the satellite's angular momentum and the rotors' angular momentum, as shown below.
<div align="center">
  <img src="images/H.svg" alt="images/H.svg" width="300"/>
</div>

Since there are no external torques, we can set the derivative of the total angular momentum to zero:
<div align="center">
  <img src="images/dH.svg" alt="images/dH.svg" width="700"/>
</div>

We can then rearrange the equation to: 

<div align="center">
  <img src="images/dH_arrenge.svg" alt="images/dH_arrenge.svg" width="900"/>
</div>

S(ω)<sup>[1](#footnote1)</sup>

And its explicit component-wise form is:
<div align="center">
  <img src="images/dwdt_explicit.svg" alt="images/dwdt_explicit.svg" width="1000"/>
</div>

## Kynematics

There are many ways to represent the attitude of the spacecraft, such as Euler Angles, Rodrigues Parameters, quaternions, etc. For this application, we'll focus on the nonsingular quaternion representation, defined as:





---

<a name="footnote1">[1]</a> **Skew-Symmetric Matrix**:  
S(ω) is the skew-symmetric matrix associated with the angular velocity vector ω, defined as:

<div align="center">
  <img src="images/skew.svg" alt="Skew-symmetric Matrix" width="400"/>
</div>
