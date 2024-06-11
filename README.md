# Radar Range Equation Calculator
The **Radar Range Equation** is used to calculate the theoretical **range of the target**.



## Power Received - Radar
$\displaystyle \boldsymbol{
{P_r} = \frac{{P_t}\ {G_t}\ {G_r}\ {\lambda^2}\ {\sigma}} {{(4\pi)^3}\ {R^4}}}
$

<br>
<p style="margin-bottom: 5px;"><b>Units:</b></p>

$P_r$ : Power Received ( $W$ )  
$P_t$ : Power Transmitted ( $W$ )  
$G_t$ : Gain Transmitted  
$G_r$ : Gain Received  
$λ$ : Wavelength ( $m$ )  
$σ$ : Radar Cross Section ( $m^2$ )  
$R$ : Range ( $m$ )  


## Power Received - Jammer
$\displaystyle \boldsymbol{
{P_r} = \frac{{P_t}\ {G_t}\ {G_r}\ {\lambda^2}} {{(4\pi)^2}\ {R^2}\ {Lt}\ {La}\ {Lr}}}
$

<br>
<p style="margin-bottom: 5px;"><b>Units:</b></p>

$P_r$ : Power Received ( $W$ )  
$P_t$ : Power Transmitted ( $W$ )  
$G_t$ : Gain Transmitted  
$G_r$ : Gain Received  
$λ$ : Wavelength ( $m$ )  
$R$ : Range ( $m$ )  
$Lt$ : Loss - Transmit Path
$La$ : Loss - Propogation Medium  
$Lr$ : Loss - Receiver Component 


## Frequency
$\displaystyle \boldsymbol{
λ = \frac{c}{v}}
$

<br>
<p style="margin-bottom: 5px;"><b>Units:</b></p>

$λ$ : Wavelength ( $m$ )  
$v$ : Frequency ( $Hz$ )  
$c$ : Speed of Light ( $299,792,458 \space m/s$ )  


## Known Bugs/Issues
- If an input has "-" in the middle of a string of numbers, an error will not be thrown. This is caused due to enabling the use of negative numbers.