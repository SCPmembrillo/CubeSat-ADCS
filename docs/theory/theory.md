# Kinematics & Dynamics

## Dynamics
The main principle behind reaction wheels is the **conservation of angular momentum**, which is the sum of the satellite's angular momentum and the rotors' angular momentum, as shown below.
<div align="center">
  <img src="docs/images/H.svg" alt="docs/images/H.svg" width="300"/>
</div>

Since there are no external torques, we can set the derivative of the total angular momentum to zero:
<div align="center">
  <img src="docs/images/dH.svg" alt="docs/images/dH.svg" width="700"/>
</div>

We can then rearrange the equation to: 

<div align="center">
  <img src="docs/images/dH_arrenge.svg" alt="docs/images/dH_arrenge.svg" width="900"/>
</div>

S(ω)<sup>[1](#footnote1)</sup>

And its explicit component-wise form is:
<div align="center">
  <img src="docs/images/dwdt_explicit.svg" alt="docs/images/dwdt_explicit.svg" width="1000"/>
</div>

## Kynematics

There are many ways to represent the attitude of the spacecraft, such as Euler Angles, Rodrigues Parameters, quaternions, etc. For this application, we'll focus on the nonsingular quaternion representation, defined as:
<div align="center">
  <img src="docs/images/quaternion.svg" alt="docs/images/quaternion.svg" width="300"/>
</div>

Here, \(c_{ij}\) denotes the elements of the rotation matrix, constructed using a **3-1-3 Euler rotation sequence**:

<div align="center">
  <img src="docs/images/313rot.svg" alt="docs/images/313rot.svg" width="750"/>
</div>

And the attitude kinematics of the spacecraft, expressed in terms of the quaternion, are given by:
<div align="center">
  <img src="docs/images/quat_kyne.svg" alt="docs/images/quat_kyne.svg" width="300"/>
</div>

Ω<sup>[2](#footnote2)</sup>

---

<a name="footnote1">[1]</a> **Skew-Symmetric Matrix**:  
S(ω) is the skew-symmetric matrix associated with the angular velocity vector ω, defined as:

<div align="center">
  <img src="docs/images/skew.svg" alt="docs/images/skew.svg" width="300"/>
</div>

<a name="footnote2">[2]</a> **Skew-Symmetric Matrix**:  
Ω is the skew-symmetric matrix associated with the angular velocity vector ω, defined as:

<div align="center">
  <img src="docs/images/skew_4x4.svg" alt="docs/images/skew_4x4.svg" width="300"/>
</div>
