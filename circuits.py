import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    logger = Logging.setup_logging()

    circuit = Circuit('Voltage Divider')
    circuit.V('input', 'in', circuit.gnd, 10 @ u_V)
    circuit.R(1, 'in', 'out', 9 @ u_kΩ)
    circuit.R(2, 'out', circuit.gnd, 1 @ u_kΩ)

    simulator = circuit.simulator(temperature=25, nominal_temperature=25)

    analysis = simulator.operating_point()
    analysis
    for node in (analysis['in'], analysis.out):  # .in is invalid !
        print('Node {}: {} V'.format(str(node), float(node)))
