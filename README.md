# Radar Range Equation Calculator
The **Radar Range Equation** is used to calculate the theoretical **range of the target**.

<br>

## Power Received - Radar
### Linear:
$\displaystyle \boldsymbol{
{P_r} = \frac{{P_t}\ {G_t}\ {G_r}\ {\lambda^2}\ {\sigma}} {{(4\pi)^3}\ {R^4}} \ \ \ 
= \ \ \ 
      \frac{{P_t}\ {G_t}\ {G_r}\ {c^2}\ {\sigma}} {{(4\pi)^3}\ {f^2} \ {R^4}}
}$

<br>

### Logarithmic:
$\displaystyle \boldsymbol{
{P_r} = 10\log_{10}(P_t) + 10\log_{10}(G_t) + 10\log_{10}(G_r) + 20\log_{10}(\lambda) + 10\log_{10}(\sigma) - 30\log_{10}(4\pi) - 40\log_{10}(R)
}$  
<br>
$\displaystyle \boldsymbol{
{P_r} = 10\log_{10}(P_t) + 10\log_{10}(G_t) + 10\log_{10}(G_r) + 20\log_{10}(c) + 10\log_{10}(\sigma) - 30\log_{10}(4\pi) - 20\log_{10}(f) - 40\log_{10}(R)
}$

<br>

<p style="margin-bottom: 5px;"><b>Units:</b></p>

$P_r$ : Power Received ( $W$ )  
$P_t$ : Power Transmitted ( $W$ )  
$G_t$ : Gain Transmitted  
$G_r$ : Gain Received  
$λ$ : Wavelength ( $m$ )  
$c$ : Speed of Light ( $299,792,458 \space m/s$ )  
$f$ : Frequency ( $Hz$ )  
$σ$ : Radar Cross Section ( $m^2$ )  
$R$ : Range ( $m$ )  

<br>

## Doppler Shift
$\displaystyle \boldsymbol{
f_d = \frac{2 \ V f_t}{c}}
$

<br>

<p style="margin-bottom: 5px;"><b>Units:</b></p>

$V$ : Velocity ( $m/s$ )  
$f_d$ : Doppler Frequency ( $Hz$ )  
$f_t$ : Transmit Frequency ( $Hz$ )  
$c$ : Speed of Light ( $299,792,458 \ m/s$ )

<br>

## Max Unambiguous Range

$\displaystyle \boldsymbol{
R = \frac{2}{c \ PRF}}
$  
<br>
$\displaystyle \boldsymbol{
R = \frac{c \ PRI}{2}}
$

<br>

<p style="margin-bottom: 5px;"><b>Units:</b></p>

$R$ : Range ( $m$ )  
$PRF$ : Pulse Repetition Frequency ( $Hz$ )  
$PRI$ : Pulse Repetition Interval ( $s$ )  
$c$ : Speed of Light ( $299,792,458 \space m/s$ )

<br>

## Known Bugs/Issues
- If "-" is found within an input, no logged error will be raised, as negative numbers are enabled.
- If "e" is found within an input (not including "E"), no logged error will be raised, as some calculations result in a scientific notation output.

<br>

##  

<b>Davis Guest</b>
