import matplotlib as mpl
mpl.use('pgf')
import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

x, Air = np.genfromtxt( 'content/DoseProfileAir.txt', unpack=True )
x, Bone = np.genfromtxt( 'content/DoseProfileBone.txt', unpack=True )
x, Fat = np.genfromtxt( 'content/DoseProfileFat.txt', unpack=True )
x, Water = np.genfromtxt( 'content/DoseProfileWater.txt', unpack=True )

#Normieren

Air_norm = Air/max(Air) * 100
Bone_norm = Bone/max(Bone) * 100
Fat_norm = Fat/max(Fat) * 100
Water_norm = Water/max(Water) * 100

plt.plot(x-0.350629, Air_norm, 'r,', label='Air')
plt.plot(x-0.350629, Bone_norm, 'b,', label='Bone')
plt.plot(x-0.350629, Fat_norm, 'g,', label='Fat')
plt.plot(x-0.350629, Water_norm, 'm,', label='Water')
plt.axvline(2.5, color='r', linestyle='--', linewidth='.5', label = 'PTV')
plt.axvline(7.5, color='r', linestyle='--', linewidth='.5')
plt.grid(ls=':')
plt.legend()
plt.xlabel(r'$x \, / \, cm$')
plt.ylabel(r'normierte Dosis / %')
plt.savefig('build/Aufgabe3.2.pdf')
plt.close()
