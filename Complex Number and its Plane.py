import numpy as np 
import matplotlib.pyplot as plt 
complex_numbers=[1+1j,-1+1j,-1-1j,1-1j,2+2j]
real_parts=[z.real for z in complex_numbers]
imaginary_parts=[z.imag for z in complex_numbers]
plt.plot(real_parts,imaginary_parts,color='blue')
for z in complex_numbers:
    plt.text(z.real,z.imag,f'{z}',fontsize=12,ha='right')
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0,color='black',linewidth=0.5)
plt.grid(color='grey',linestyle='--',linewidth=0.5)
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Complex Numbers in the Complex Plane')
plt.show()
polar_coordinates=[(abs(z),np.angle(z)) for z in complex_numbers]
for z, (r,theta) in zip(complex_numbers,polar_coordinates):
    print(f'Complex number:{z},Magnitude:{r:.2f},Angle(radians):{theta:.2f}')