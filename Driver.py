import converter
import cspbase
import propagators

def main():
    Input = []
    CSP = converter.toCSP(Input)
    assignments = propagators.prop_GAC(CSP)

if __name__ == "__main__":
    main()