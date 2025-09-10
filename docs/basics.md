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
<div align="center">
  <img src="images/quaternion.svg" alt="images/quaternion.svg" width="300"/>
</div>

Here, \(c_{ij}\) denotes the elements of the rotation matrix, constructed using a **3-1-3 Euler rotation sequence**:

<div align="center">
  <img src="images/313rot.svg" alt="images/313rot.svg" width="750"/>
</div>

And the attitude kinematics of the spacecraft, expressed in terms of the quaternion, are given by:
<div align="center">
  <img src="images/quat_kyne.svg" alt="images/quat_kyne.svg" width="300"/>
</div>

Ω<sup>[2](#footnote2)</sup>

---

<a name="footnote1">[1]</a> **Skew-Symmetric Matrix**:  
S(ω) is the skew-symmetric matrix associated with the angular velocity vector ω, defined as:

<div align="center">
  <img src="images/skew.svg" alt="images/skew.svg" width="300"/>
</div>

<a name="footnote2">[2]</a> **Skew-Symmetric Matrix**:  
Ω is the skew-symmetric matrix associated with the angular velocity vector ω, defined as:

<div align="center">
  <img src="images/skew_4x4.svg" alt="images/skew_4x4.svg" width="300"/>
</div>
