import sys
#file1 = open(sys.argv[0], 'r')
#myfile = open(sys.argv[1], 'w')
file1 = open('peptidederivativemixture.xyz', 'r')
myfile = open('peptidederivative.fdf', 'w')
elements = {'C' : 1, 'O' : 2, 'N' : 3, 'H' : 4}
timesteps = 50

atomicnumber = {'C' : 6, 'O': 8, 'N': 7, 'H': 1}

num_species = len(elements)
lines = file1.readlines()



atoms = lines[0].split()
num_atoms = atoms[0]
lines.pop(0)
lines.pop(0)


thelines = []


myfile.write("NumberOfAtoms " + num_atoms + "\n")
myfile.write("SpinPolarized yes" + "\n")
myfile.write("#FixSpin .true." + "\n")
myfile.write("#TotalSpin" + "\n")
myfile.write("NumberOfSpecies " + "\n" +"\n" + "\n")
myfile.write("MD.TypeOfRun  nose" + "\n")
myfile.write("MD.FinalTimeStep " + str(timesteps) + "\n")
myfile.write("MD.LengthTimeStep 1.0  fs" + "\n")
myfile.write("MD.InitialTemperature 300 K" + "\n")
myfile.write("MD.TargetTemperature  300  K" +"\n" +"\n" + "\n")
myfile.write("%block ChemicalSpeciesLabel" + "\n")

for i in elements:
    myfile.write(str(elements[i]) + ' ' + str(atomicnumber[i]) + ' ' + i )
    myfile.write("\n")
myfile.write("%endblock ChemicalSpeciesLabel" + "\n")
myfile.write("PAO.BasisSize dzp " + "\n")
myfile.write(" PAO.EnergyShift 0.02 Ry " + "\n")
myfile.write("MeshCutoff          100 Ry" + "\n")
myfile.write("MaxSCFIterations    100" + "\n")
myfile.write("DM.NumberPulay       3" + "\n")
myfile.write("DM.Tolerance         1e-3" + "\n")
myfile.write("WriteDenchar	.true." + "\n")
myfile.write("%block ProjectedDensityOfStates" + "\n")
myfile.write("-10.0 10.0 0.200 500 eV" + "\n")
myfile.write("%endblock ProjectedDensityOfStates" + "\n")
myfile.write("NetCharge 0.00" + "\n" + "\n")
myfile.write("%block BandLines" + "\n")
myfile.write("1  1.000  1.000 1.000  L" + "\n")
myfile.write("20 0.00   0.00   0.00  \Gamma" + "\n")
myfile.write("25 2.00   0.000  0.00  X" + "\n")
myfile.write("30 2.00   2.00   2.00  \Gamma" + "\n")
myfile.write("%endblock BandLines" + "\n" + "\n" + "\n")
myfile.write("LongOutput .true." + "\n")
myfile.write("WriteCoorXmol .true." + "\n")
myfile.write("LatticeConstant 1 Ang" + "\n")
myfile.write("%block LatticeVectors" + "\n")
myfile.write("  30 0.0 0.0" + "\n")
myfile.write("  0.0 30 0.0" + "\n")
myfile.write("0.0 0.0 30" + "\n")
myfile.write("%endblock LatticeVectors" + "\n" + "\n" + "\n" + "\n" + "\n")
myfile.write("#UseSaveData .true." + "\n")
myfile.write("%block kgrid_Monkhorst_Pack" + "\n")
myfile.write("1 0 0 0.0 " + "\n")
myfile.write(" 0 1 0 0.0 " + "\n")
myfile.write(" 0 0 1 0.0" + "\n" + "\n")
myfile.write("%endblock kgrid_Monkhorst_Pack" + "\n")
myfile.write("WriteMDXmol .true." + "\n")
myfile.write("AtomicCoordinatesFormat Ang" + "\n")
myfile.write("%block AtomicCoordinatesAndAtomicSpecies" + "\n")


for line in lines:
    new = []
    current = line.split()
    elem = str(elements[current[0]])
    myfile.write(current[1] + "  " + current[2] + " " + current[3] + "  " + elem )
    myfile.write("\n")
myfile.write("%block AtomicCoordinatesAndAtomicSpecies")

