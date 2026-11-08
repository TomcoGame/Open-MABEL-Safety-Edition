// Open MABEL Safety Edition — illustrative SysML v2-style sketch
// NOT validated against a SysML v2 parser or semantic model.
// All safety components are proposed unless stated otherwise.
package OpenMabelSafetyEdition {
    part def MobileBase;
    part def Manipulators;
    part def Lift;
    part def ApplicationController;
    part def PowerSystem;
    part def SafetyController;

    part def Robot {
        part base : MobileBase;
        part manipulators : Manipulators;
        part lift : Lift;
        part application : ApplicationController;
        part power : PowerSystem;
        // Proposed addition — not an implemented subsystem:
        part safety : SafetyController;
    }

    part robot : Robot;
}
