# Radar Range Equation Calculator
The **Radar Range Equation** is used to calculate the theoretical **range of the target**.

## Power Received - Radar

### Linear:
$\displaystyle \boldsymbol{
{P_r} = \frac{{P_t}\ {G_t}\ {G_r}\ {\lambda^2}\ {\sigma}} {{(4\pi)^3}\ {R^4}}
}$

<br>

### Logarithmic:
$\displaystyle \boldsymbol{
{P_r} = 10\log_{10}(P_t) + 10\log_{10}(G_t) + 10\log_{10}(G_r) + 20\log_{10}(\lambda) + 10\log_{10}(\sigma) - 30\log_{10}(4\pi) - 40\log_{10}(R)
}$

<br>

<p style="margin-bottom: 5px;"><b>Units:</b></p>

$P_r$ : Power Received ( $W$ )  
$P_t$ : Power Transmitted ( $W$ )  
$G_t$ : Gain Transmitted  
$G_r$ : Gain Received  
$λ$ : Wavelength ( $m$ )  
$σ$ : Radar Cross Section ( $m^2$ )  
$R$ : Range ( $m$ )  

<br>

## Power Received - Jammer

### Linear:
$\displaystyle \boldsymbol{
{P_r} = \frac{{P_t}\ {G_t}\ {G_r}\ {\lambda^2}} {{(4\pi)^2}\ {R^2}\ {Lt}\ {La}\ {Lr}}}
$

<br>

### Logarithmic:
$\displaystyle \boldsymbol{
{P_r} = 10\log_{10}(P_t) + 10\log_{10}(G_t) + 10\log_{10}(G_r) + 20\log_{10}(\lambda)- 20\log_{10}(4\pi) - 20\log_{10}(R) - 10\log_{10}(L_t) - 10\log_{10}(L_a) - 10\log_{10}(L_r)
}$

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

<br>

## Frequency
### Linear:
$\displaystyle \boldsymbol{
λ = \frac{c}{v}}
$

### Logarithmic:

<br>
<p style="margin-bottom: 5px;"><b>Units:</b></p>

$λ$ : Wavelength ( $m$ )  
$v$ : Frequency ( $Hz$ )  
$c$ : Speed of Light ( $299,792,458 \space m/s$ )

<br>

## Known Bugs/Issues
- If "-" is found within an input, no error will be raised, as negative numbers are enabled.