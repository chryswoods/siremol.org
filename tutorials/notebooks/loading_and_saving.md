
# Loading and Saving Molecules

This notebook will show you how to load and save molecules in Sire. Input and output of molecules is handled by the `Sire.IO.MoleculeParser` class in the Sire.IO library, so we first need to import this.


```python
from Sire.IO import MoleculeParser
```

MoleculeParser can recognise different file formats using its `read` function. For example, to load the molecules contained in the Amber format files "input/NA16.top" and "input/NA16.rst" we use the command;


```python
system = MoleculeParser.read( "input/NA16.top", "input/NA16.rst" )
```

Molecules are loaded into a `Sire.System.System`. This is a container for all of the molecules and associated metadata. As with all Python objects, you can get help with this by using `help(object)`, e.g.


```python
help(system)
```

    Help on System in module Sire.System._System object:
    
    class System(Sire.Mol._Mol.MolGroupsBase, Sire.Base._Base.Property)
     |  This is a simulation system. If contains molecules, forcefields that
     |  provide energy functions of those molecules, and monitors that
     |  can monitor the changing state of the system
     |  
     |  Author: Christopher Woods
     |  
     |  Method resolution order:
     |      System
     |      Sire.Mol._Mol.MolGroupsBase
     |      Sire.Base._Base.Property
     |      Boost.Python.instance
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  UID(...)
     |      UID( (System)arg1) -> QUuid :
     |      
     |          C++ signature :
     |              QUuid UID(SireSystem::System {lvalue})
     |  
     |  __copy__(...)
     |      __copy__( (System)arg1) -> System :
     |      
     |          C++ signature :
     |              SireSystem::System __copy__(SireSystem::System)
     |  
     |  __deepcopy__(...)
     |      __deepcopy__( (System)arg1) -> System :
     |      
     |          C++ signature :
     |              SireSystem::System __deepcopy__(SireSystem::System)
     |  
     |  __eq__(...)
     |      __eq__( (System)arg1, (System)arg2) -> object :
     |      
     |          C++ signature :
     |              _object* __eq__(SireSystem::System {lvalue},SireSystem::System)
     |  
     |  __getitem__(...)
     |      __getitem__( (System)arg1, (FFID)ffid) -> FF :
     |      
     |          C++ signature :
     |              SireFF::FF __getitem__(SireSystem::System {lvalue},SireFF::FFID)
     |      
     |      __getitem__( (System)arg1, (MonitorID)monid) -> SystemMonitor :
     |      
     |          C++ signature :
     |              SireSystem::SystemMonitor __getitem__(SireSystem::System {lvalue},SireSystem::MonitorID)
     |      
     |      __getitem__( (System)arg1, (MGID)mgid) -> MoleculeGroup :
     |      
     |          C++ signature :
     |              SireMol::MoleculeGroup __getitem__(SireSystem::System {lvalue},SireMol::MGID)
     |      
     |      __getitem__( (System)arg1, (MolNum)molnum) -> object :
     |      
     |          C++ signature :
     |              SireMol::ViewsOfMol __getitem__(SireSystem::System {lvalue},SireMol::MolNum)
     |      
     |      __getitem__( (System)arg1, (MolID)molid) -> object :
     |      
     |          C++ signature :
     |              SireMol::ViewsOfMol __getitem__(SireSystem::System {lvalue},SireMol::MolID)
     |  
     |  __init__(...)
     |      __init__( (object)arg1) -> None :
     |          Construct an unnamed System
     |      
     |          C++ signature :
     |              void __init__(_object*)
     |      
     |      __init__( (object)arg1, (StringProperty)name) -> None :
     |          Construct a named System
     |      
     |          C++ signature :
     |              void __init__(_object*,QString)
     |      
     |      __init__( (object)arg1, (System)other) -> None :
     |          Copy constructor
     |      
     |          C++ signature :
     |              void __init__(_object*,SireSystem::System)
     |  
     |  __len__(...)
     |      __len__( (System)arg1) -> int :
     |      
     |          C++ signature :
     |              unsigned long __len__(SireSystem::System {lvalue})
     |  
     |  __ne__(...)
     |      __ne__( (System)arg1, (System)arg2) -> object :
     |      
     |          C++ signature :
     |              _object* __ne__(SireSystem::System {lvalue},SireSystem::System)
     |  
     |  __reduce__ = <unnamed Boost.Python function>(...)
     |  
     |  __repr__(...)
     |      __repr__( (System)arg1) -> object :
     |      
     |          C++ signature :
     |              boost::python::api::object __repr__(SireSystem::System)
     |  
     |  __rlshift__(...)
     |      __rlshift__( (System)arg1, (object)arg2) -> object :
     |      
     |          C++ signature :
     |              QDataStream {lvalue} __rlshift__(SireSystem::System,QDataStream {lvalue})
     |  
     |  __rrshift__(...)
     |      __rrshift__( (System)arg1, (object)arg2) -> object :
     |      
     |          C++ signature :
     |              QDataStream {lvalue} __rrshift__(SireSystem::System {lvalue},QDataStream {lvalue})
     |  
     |  __str__(...)
     |      __str__( (System)arg1) -> object :
     |      
     |          C++ signature :
     |              boost::python::api::object __str__(SireSystem::System)
     |  
     |  accept(...)
     |      accept( (System)arg1) -> None :
     |          Tell all of the forcefields that the last move was accepted. This allows
     |          any cacheing or use of temporary workspaces to be committed
     |      
     |          C++ signature :
     |              void accept(SireSystem::System {lvalue})
     |  
     |  add(...)
     |      add( (System)arg1, (StringProperty)name, (SystemMonitor)monitor [, (int)frequency=1]) -> None :
     |          Add a system monitor monitor, identified by the name name, which
     |          will be updated every frequency steps.
     |          Throw: SireSystem::duplicate_monitor
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},QString,SireSystem::SystemMonitor [,int=1])
     |      
     |      add( (System)arg1, (SystemMonitors)monitors) -> None :
     |          Add the monitors in monitors to this system
     |          Throw: SireSystem::duplicate_monitor
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireSystem::SystemMonitors)
     |      
     |      add( (System)arg1, (SystemMonitors)monitors, (int)frequency) -> None :
     |          Add the monitors in monitors, setting the frequency of the
     |          new monitors to frequency
     |          Throw: SireSystem::duplicate_monitor
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireSystem::SystemMonitors,int)
     |      
     |      add( (System)arg1, (FF)forcefield) -> None :
     |          Add the forcefield forcefield to this system. This will raise
     |          an exception if this forcefield (or one with the same name)
     |          is already present in this set. Note that if the added
     |          forcefield will be updated to contain the versions of
     |          any molecules that are already present in any of the
     |          other forcefields.
     |          Throw: SireFF::duplicate_forcefield
     |          Throw: SireMol::duplicate_group
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireFF::FF)
     |      
     |      add( (System)arg1, (MoleculeGroup)molgroup) -> None :
     |          Add the molecule group molgroup to this system. If this is
     |          a molecule group that is part of a forcefield, then the entire
     |          forcefield will be added to this system. This will raise
     |          an exception if this molecule group is already present in
     |          this system. Note that the added molecule group will be
     |          updated to contain the version of the any molecules that
     |          are already present in this system
     |          Throw: SireFF::duplicate_forcefield
     |          Throw: SireMol::duplicate_group
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireMol::MoleculeGroup)
     |      
     |      add( (System)arg1, (Constraint)constraint) -> None :
     |          Add the passed constraint to the system
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireSystem::Constraint)
     |      
     |      add( (System)arg1, (Constraints)constraints) -> None :
     |          Add the passed constraint to the system
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireSystem::Constraints)
     |      
     |      add( (System)arg1, (MoleculeView)molview, (MGID)mgid, (PropertyMap)map) -> None :
     |          Add the molecule viewed in molview to the molecule groups
     |          identified by the ID mgid. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to. The version of the molecule
     |          already present in this system is used, if such a molecule exists.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireMol::MoleculeView,SireMol::MGID,SireBase::PropertyMap)
     |      
     |      add( (System)arg1, (object)molviews, (MGID)mgid, (PropertyMap)map) -> None :
     |          Add the views of the molecule in molviews to the molecule groups
     |          identified by the ID mgid. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to. The version of the molecule
     |          already present in this system is used, if such a molecule exists.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireMol::ViewsOfMol,SireMol::MGID,SireBase::PropertyMap)
     |      
     |      add( (System)arg1, (Molecules)molecules, (MGID)mgid, (PropertyMap)map) -> None :
     |          Add the molecules viewed in molecules to the molecule groups
     |          identified by the ID mgid. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to. The version of the molecule
     |          already present in this system is used, if such a molecule exists.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireMol::Molecules,SireMol::MGID,SireBase::PropertyMap)
     |      
     |      add( (System)arg1, (MoleculeGroup)molgroup, (MGID)mgid, (PropertyMap)map) -> None :
     |          Add the molecules in the molecule group molgroup to the molecule groups
     |          identified by the ID mgid. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to. The version of the molecule
     |          already present in this system is used, if such a molecule exists.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireMol::MoleculeGroup,SireMol::MGID,SireBase::PropertyMap)
     |      
     |      add( (System)arg1, (MoleculeView)molview, (MGID)mgid) -> None :
     |          Convenient overload of System::add that uses the default locations
     |          to find any necessary properties.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireMol::MoleculeView,SireMol::MGID)
     |      
     |      add( (System)arg1, (object)molviews, (MGID)mgid) -> None :
     |          Convenient overload of System::add that uses the default locations
     |          to find any necessary properties.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireMol::ViewsOfMol,SireMol::MGID)
     |      
     |      add( (System)arg1, (Molecules)molecules, (MGID)mgid) -> None :
     |          Convenient overload of System::add that uses the default locations
     |          to find any necessary properties.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireMol::Molecules,SireMol::MGID)
     |      
     |      add( (System)arg1, (MoleculeGroup)molgroup, (MGID)mgid) -> None :
     |          Convenient overload of System::add that uses the default locations
     |          to find any necessary properties.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void add(SireSystem::System {lvalue},SireMol::MoleculeGroup,SireMol::MGID)
     |  
     |  addIfUnique(...)
     |      addIfUnique( (System)arg1, (MoleculeView)molview, (MGID)mgid, (PropertyMap)map) -> None :
     |          Add the view of the molecule in molview to the groups
     |          identified by mgid. This only adds the view to a group
     |          if it doesnt already exist in the group. The version
     |          of the molecule already present in this set is used if
     |          such a molecule already exists. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void addIfUnique(SireSystem::System {lvalue},SireMol::MoleculeView,SireMol::MGID,SireBase::PropertyMap)
     |      
     |      addIfUnique( (System)arg1, (object)molviews, (MGID)mgid, (PropertyMap)map) -> None :
     |          Add the views of the molecule in molviews to the groups
     |          identified by mgid. This only adds the view to a group
     |          if it doesnt already exist in the group. The version
     |          of the molecule already present in this set is used if
     |          such a molecule already exists. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void addIfUnique(SireSystem::System {lvalue},SireMol::ViewsOfMol,SireMol::MGID,SireBase::PropertyMap)
     |      
     |      addIfUnique( (System)arg1, (Molecules)molecules, (MGID)mgid, (PropertyMap)map) -> None :
     |          Add the views of the molecules in molecules to the groups
     |          identified by mgid. This only adds the view to a group
     |          if it doesnt already exist in the group. The version
     |          of the molecule already present in this set is used if
     |          such a molecule already exists. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void addIfUnique(SireSystem::System {lvalue},SireMol::Molecules,SireMol::MGID,SireBase::PropertyMap)
     |      
     |      addIfUnique( (System)arg1, (MoleculeGroup)molgroup, (MGID)mgid, (PropertyMap)map) -> None :
     |          Add the view of the molecules in the group molgroup to the groups
     |          identified by mgid. This only adds the view to a group
     |          if it doesnt already exist in the group. The version
     |          of the molecule already present in this set is used if
     |          such a molecule already exists. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void addIfUnique(SireSystem::System {lvalue},SireMol::MoleculeGroup,SireMol::MGID,SireBase::PropertyMap)
     |      
     |      addIfUnique( (System)arg1, (MoleculeView)molview, (MGID)mgid) -> None :
     |          Convenient overload of System::addIfUnique that uses the default locations
     |          to find any necessary properties.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void addIfUnique(SireSystem::System {lvalue},SireMol::MoleculeView,SireMol::MGID)
     |      
     |      addIfUnique( (System)arg1, (object)molviews, (MGID)mgid) -> None :
     |          Convenient overload of System::addIfUnique that uses the default locations
     |          to find any necessary properties.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void addIfUnique(SireSystem::System {lvalue},SireMol::ViewsOfMol,SireMol::MGID)
     |      
     |      addIfUnique( (System)arg1, (Molecules)molecules, (MGID)mgid) -> None :
     |          Convenient overload of System::addIfUnique that uses the default locations
     |          to find any necessary properties.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void addIfUnique(SireSystem::System {lvalue},SireMol::Molecules,SireMol::MGID)
     |      
     |      addIfUnique( (System)arg1, (MoleculeGroup)molgroup, (MGID)mgid) -> None :
     |          Convenient overload of System::addIfUnique that uses the default locations
     |          to find any necessary properties.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void addIfUnique(SireSystem::System {lvalue},SireMol::MoleculeGroup,SireMol::MGID)
     |  
     |  applyConstraints(...)
     |      applyConstraints( (System)arg1) -> None :
     |          Apply the system (and molecule) constraints
     |      
     |          C++ signature :
     |              void applyConstraints(SireSystem::System {lvalue})
     |  
     |  assign(...)
     |      assign( (System)arg1, (System)other) -> System :
     |      
     |          C++ signature :
     |              SireSystem::System {lvalue} assign(SireSystem::System {lvalue},SireSystem::System)
     |  
     |  at(...)
     |      at( (System)arg1, (FFID)ffid) -> FF :
     |          Return the forcefield with ID ffid in this system
     |          Throw: SireFF::missing_forcefield
     |          Throw: SireFF::duplicate_forcefield
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireFF::FF at(SireSystem::System {lvalue},SireFF::FFID)
     |      
     |      at( (System)arg1, (MonitorID)monid) -> SystemMonitor :
     |          Return the monitor at ID monid
     |          Throw: SireSystem::missing_monitor
     |          Throw: SireSystem::duplicate_monitor
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireSystem::SystemMonitor at(SireSystem::System {lvalue},SireSystem::MonitorID)
     |      
     |      at( (System)arg1, (MGNum)mgnum) -> MoleculeGroup :
     |          overloading MolGroupsBase virtual functions
     |      
     |          C++ signature :
     |              SireMol::MoleculeGroup at(SireSystem::System {lvalue},SireMol::MGNum)
     |  
     |  builtinProperties(...)
     |      builtinProperties( (System)arg1) -> Properties :
     |          Return the values of all built-in properties of this system
     |      
     |          C++ signature :
     |              SireBase::Properties builtinProperties(SireSystem::System {lvalue})
     |  
     |  builtinProperty(...)
     |      builtinProperty( (System)arg1, (StringProperty)name) -> Property :
     |          Return the built-in property at name. This will by-pass any
     |          user-supplied property with this name, and will raise an
     |          exception if there is no built-in property with this name
     |          Throw: SireBase::missing_property
     |          
     |      
     |          C++ signature :
     |              SireBase::Property builtinProperty(SireSystem::System {lvalue},QString)
     |  
     |  clearStatistics(...)
     |      clearStatistics( (System)arg1) -> None :
     |          Completely clear all statistics held in the monitors
     |      
     |          C++ signature :
     |              void clearStatistics(SireSystem::System {lvalue})
     |      
     |      clearStatistics( (System)arg1, (MonitorID)monid) -> None :
     |          Clear the statistics of the monitors that match the ID monid.
     |          This does nothing if there are no matching monitors
     |      
     |          C++ signature :
     |              void clearStatistics(SireSystem::System {lvalue},SireSystem::MonitorID)
     |  
     |  clone(...)
     |      clone( (System)arg1) -> System :
     |      
     |          C++ signature :
     |              SireSystem::System clone(SireSystem::System)
     |  
     |  collectStats(...)
     |      collectStats( (System)arg1) -> None :
     |          Collect statistics about the current configuration
     |      
     |          C++ signature :
     |              void collectStats(SireSystem::System {lvalue})
     |  
     |  componentExpression(...)
     |      componentExpression( (System)arg1, (Symbol)symbol) -> Expression :
     |          Return the expression that defines the component represented
     |          by the symbol symbol
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              SireCAS::Expression componentExpression(SireSystem::System {lvalue},SireCAS::Symbol)
     |  
     |  componentExpressions(...)
     |      componentExpressions( (System)arg1, (object)symbols) -> object :
     |          Return the expressions that define the components whose
     |          symbols are in symbols
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              QHash<SireCAS::Symbol, SireCAS::Expression> componentExpressions(SireSystem::System {lvalue},QSet<SireCAS::Symbol>)
     |      
     |      componentExpressions( (System)arg1) -> object :
     |          Return all of the expressions that define all of the components
     |          of this system
     |      
     |          C++ signature :
     |              QHash<SireCAS::Symbol, SireCAS::Expression> componentExpressions(SireSystem::System {lvalue})
     |  
     |  componentSymbols(...)
     |      componentSymbols( (System)arg1) -> object :
     |          Return all of the symbols that represent the constant and
     |          energy components of this system
     |      
     |          C++ signature :
     |              QSet<SireCAS::Symbol> componentSymbols(SireSystem::System {lvalue})
     |  
     |  componentValue(...)
     |      componentValue( (System)arg1, (Symbol)symbol) -> float :
     |          Return the value of the energy or constant component
     |          with symbol symbol
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              double componentValue(SireSystem::System {lvalue},SireCAS::Symbol)
     |  
     |  componentValues(...)
     |      componentValues( (System)arg1) -> Values :
     |          Return the values of all components of this system
     |          (constant components and energies)
     |      
     |          C++ signature :
     |              SireCAS::Values componentValues(SireSystem::System {lvalue})
     |      
     |      componentValues( (System)arg1, (object)symbols) -> Values :
     |          Retunr the value of the energy or constant component values
     |          whose symbols are in symbols
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              SireCAS::Values componentValues(SireSystem::System {lvalue},QSet<SireCAS::Symbol>)
     |  
     |  compoundProperty(...)
     |      compoundProperty( (System)arg1, (StringProperty)name) -> Property :
     |          Return the raw compound property with name name - this returns
     |          the property representing the link, or the combined property,
     |          and raises an exception if a compound property with this name
     |          does not exist
     |          Throw: SireBase::missing_property
     |          
     |      
     |          C++ signature :
     |              SireBase::Property compoundProperty(SireSystem::System {lvalue},QString)
     |  
     |  constant(...)
     |      constant( (System)arg1, (Symbol)component) -> float :
     |          Return the constant value for the constant component component
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              double constant(SireSystem::System {lvalue},SireCAS::Symbol)
     |  
     |  constantComponents(...)
     |      constantComponents( (System)arg1) -> Values :
     |          Return the values of all constant components of this system
     |      
     |          C++ signature :
     |              SireCAS::Values constantComponents(SireSystem::System {lvalue})
     |  
     |  constantExpression(...)
     |      constantExpression( (System)arg1, (Symbol)symbol) -> Expression :
     |          Return the expression that defines the constant component with
     |          symbol symbol
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              SireCAS::Expression constantExpression(SireSystem::System {lvalue},SireCAS::Symbol)
     |  
     |  constantExpressions(...)
     |      constantExpressions( (System)arg1, (object)symbols) -> object :
     |          Return the expressions that define the constant components
     |          whose symbols are in symbols
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              QHash<SireCAS::Symbol, SireCAS::Expression> constantExpressions(SireSystem::System {lvalue},QSet<SireCAS::Symbol>)
     |      
     |      constantExpressions( (System)arg1) -> object :
     |          Return all of the expressions that define the constant components
     |          of this system
     |      
     |          C++ signature :
     |              QHash<SireCAS::Symbol, SireCAS::Expression> constantExpressions(SireSystem::System {lvalue})
     |  
     |  constantSymbols(...)
     |      constantSymbols( (System)arg1) -> object :
     |          Return the symbols that represent constant components of this system
     |      
     |          C++ signature :
     |              QSet<SireCAS::Symbol> constantSymbols(SireSystem::System {lvalue})
     |  
     |  constants(...)
     |      constants( (System)arg1) -> Values :
     |          Return the values of all constant components in this system
     |      
     |          C++ signature :
     |              SireCAS::Values constants(SireSystem::System {lvalue})
     |      
     |      constants( (System)arg1, (object)components) -> Values :
     |          Return the values of the constant components whose symbols
     |          are in components
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              SireCAS::Values constants(SireSystem::System {lvalue},QSet<SireCAS::Symbol>)
     |  
     |  constraints(...)
     |      constraints( (System)arg1) -> Constraints :
     |          Return all of the contraints that are applied to the system
     |      
     |          C++ signature :
     |              SireSystem::Constraints constraints(SireSystem::System {lvalue})
     |  
     |  constraintsSatisfied(...)
     |      constraintsSatisfied( (System)arg1) -> bool :
     |          Return whether or not the constraints are satisfied
     |      
     |          C++ signature :
     |              bool constraintsSatisfied(SireSystem::System {lvalue})
     |  
     |  containsProperty(...)
     |      containsProperty( (System)arg1, (StringProperty)name) -> bool :
     |          Return whether or not any of the forcefields contain a property called name
     |      
     |          C++ signature :
     |              bool containsProperty(SireSystem::System {lvalue},QString)
     |      
     |      containsProperty( (System)arg1, (FFID)ffid, (StringProperty)name) -> bool :
     |          Return whether or not any of the forcefields identified by the ID ffid
     |          contain a property called name
     |      
     |          C++ signature :
     |              bool containsProperty(SireSystem::System {lvalue},SireFF::FFID,QString)
     |      
     |      containsProperty( (System)arg1, (PropertyName)name) -> bool :
     |          Return whether or not any of the forcefields contain a property called name
     |      
     |          C++ signature :
     |              bool containsProperty(SireSystem::System {lvalue},SireBase::PropertyName)
     |      
     |      containsProperty( (System)arg1, (FFID)ffid, (PropertyName)name) -> bool :
     |          Return whether or not any of the forcefields identified by the ID ffid
     |          contain a property called name
     |      
     |          C++ signature :
     |              bool containsProperty(SireSystem::System {lvalue},SireFF::FFID,SireBase::PropertyName)
     |  
     |  energies(...)
     |      energies( (System)arg1) -> Values :
     |          Return the energies of all energy components in this system
     |      
     |          C++ signature :
     |              SireCAS::Values energies(SireSystem::System {lvalue})
     |      
     |      energies( (System)arg1, (object)components) -> Values :
     |          Return the energies of the energy components of this system whose
     |          symbols are in components
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              SireCAS::Values energies(SireSystem::System {lvalue},QSet<SireCAS::Symbol>)
     |  
     |  energy(...)
     |      energy( (System)arg1) -> object :
     |          Return the total energy of this system.
     |      
     |          C++ signature :
     |              SireUnits::Dimension::PhysUnit<1, 2, -2, 0, 0, -1, 0> energy(SireSystem::System {lvalue})
     |      
     |      energy( (System)arg1, (Symbol)component) -> object :
     |          Return the total energy of the energy component in this system
     |          that is identified by the energy component component
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              SireUnits::Dimension::PhysUnit<1, 2, -2, 0, 0, -1, 0> energy(SireSystem::System {lvalue},SireCAS::Symbol)
     |      
     |      energy( (System)arg1, (EnergyTable)energytable [, (object)scale_energy=1]) -> None :
     |          Return the total energytable in this system
     |          
     |      
     |          C++ signature :
     |              void energy(SireSystem::System {lvalue},SireFF::EnergyTable {lvalue} [,double=1])
     |      
     |      energy( (System)arg1, (EnergyTable)energytable, (Symbol)component [, (object)scale_energy=1]) -> None :
     |          Return the total energytable of the energy component in this system
     |          that is identified by the energy component component
     |          
     |      
     |          C++ signature :
     |              void energy(SireSystem::System {lvalue},SireFF::EnergyTable {lvalue},SireCAS::Symbol [,double=1])
     |  
     |  energyComponents(...)
     |      energyComponents( (System)arg1) -> Values :
     |          Return all of the energy components of this system
     |      
     |          C++ signature :
     |              SireCAS::Values energyComponents(SireSystem::System {lvalue})
     |  
     |  energyExpression(...)
     |      energyExpression( (System)arg1, (Symbol)expression) -> Expression :
     |          Return the energy expression for the energy component component
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              SireCAS::Expression energyExpression(SireSystem::System {lvalue},SireCAS::Symbol)
     |  
     |  energyExpressions(...)
     |      energyExpressions( (System)arg1, (object)symbols) -> object :
     |          Return the energy expressions for the energy components whose
     |          symbols are in symbols
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              QHash<SireCAS::Symbol, SireCAS::Expression> energyExpressions(SireSystem::System {lvalue},QSet<SireCAS::Symbol>)
     |      
     |      energyExpressions( (System)arg1) -> object :
     |          Return all of the energy expressions in this system
     |      
     |          C++ signature :
     |              QHash<SireCAS::Symbol, SireCAS::Expression> energyExpressions(SireSystem::System {lvalue})
     |  
     |  energySymbols(...)
     |      energySymbols( (System)arg1) -> object :
     |          Return the symbols that represent the energy expressions of this system
     |      
     |          C++ signature :
     |              QSet<SireCAS::Symbol> energySymbols(SireSystem::System {lvalue})
     |  
     |  extraGroups(...)
     |      extraGroups( (System)arg1) -> MoleculeGroups :
     |          Return all of the extra non-forcefield molecule groups in this system
     |      
     |          C++ signature :
     |              SireMol::MoleculeGroups extraGroups(SireSystem::System {lvalue})
     |  
     |  ffIdx(...)
     |      ffIdx( (System)arg1, (FFID)ffid) -> FFIdx :
     |          Return the index of the forcefield with ID ffid
     |          Throw: SireFF::missing_forcefield
     |          Throw: SireFF::duplicate_forcefield
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireFF::FFIdx ffIdx(SireSystem::System {lvalue},SireFF::FFID)
     |  
     |  ffName(...)
     |      ffName( (System)arg1, (FFID)ffid) -> FFName :
     |          Return the name of the forcefield with ID ffid
     |          Throw: SireFF::missing_forcefield
     |          Throw: SireFF::duplicate_forcefield
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireFF::FFName ffName(SireSystem::System {lvalue},SireFF::FFID)
     |  
     |  field(...)
     |      field( (System)arg1, (FieldTable)fieldtable [, (object)scale_field=1]) -> None :
     |          Add the fields acting on the molecules in the fieldtable fieldtable
     |          from this system onto this fieldtable, scaled by the optionally
     |          supplied scale_field
     |      
     |          C++ signature :
     |              void field(SireSystem::System {lvalue},SireFF::FieldTable {lvalue} [,double=1])
     |      
     |      field( (System)arg1, (FieldTable)fieldtable, (Symbol)component [, (object)scale_field=1]) -> None :
     |          Add the fields acting on the molecules in the fieldtable fieldtable
     |          from the component of this system identified by component onto
     |          this fieldtable, scaled by the optionally supplied scale_field
     |      
     |          C++ signature :
     |              void field(SireSystem::System {lvalue},SireFF::FieldTable {lvalue},SireCAS::Symbol [,double=1])
     |      
     |      field( (System)arg1, (FieldTable)fieldtable, (Probe)probe [, (object)scale_field=1]) -> None :
     |          Add the fields acting on the molecules in the fieldtable fieldtable
     |          from this system onto this fieldtable, scaled by the optionally
     |          supplied scale_field
     |      
     |          C++ signature :
     |              void field(SireSystem::System {lvalue},SireFF::FieldTable {lvalue},SireFF::Probe [,double=1])
     |      
     |      field( (System)arg1, (FieldTable)fieldtable, (Symbol)component, (Probe)probe [, (object)scale_field=1]) -> None :
     |          Add the fields acting on the molecules in the fieldtable fieldtable
     |          from the component of this system identified by component onto
     |          this fieldtable, scaled by the optionally supplied scale_field
     |      
     |          C++ signature :
     |              void field(SireSystem::System {lvalue},SireFF::FieldTable {lvalue},SireCAS::Symbol,SireFF::Probe [,double=1])
     |  
     |  force(...)
     |      force( (System)arg1, (ForceTable)forcetable [, (object)scale_force=1]) -> None :
     |          Add the forces acting on the molecules in the forcetable forcetable
     |          from this system onto this forcetable, scaled by the optionally
     |          supplied scale_force
     |      
     |          C++ signature :
     |              void force(SireSystem::System {lvalue},SireFF::ForceTable {lvalue} [,double=1])
     |      
     |      force( (System)arg1, (ForceTable)forcetable, (Symbol)component [, (object)scale_force=1]) -> None :
     |          Add the forces acting on the molecules in the forcetable forcetable
     |          from the component of this system identified by component onto
     |          this forcetable, scaled by the optionally supplied scale_force
     |      
     |          C++ signature :
     |              void force(SireSystem::System {lvalue},SireFF::ForceTable {lvalue},SireCAS::Symbol [,double=1])
     |  
     |  forceField(...)
     |      forceField( (System)arg1, (FFID)ffid) -> FF :
     |          Return the forcefield with ID ffid in this system
     |          Throw: SireFF::missing_forcefield
     |          Throw: SireFF::duplicate_forcefield
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireFF::FF forceField(SireSystem::System {lvalue},SireFF::FFID)
     |      
     |      forceField( (System)arg1, (MGID)mgid) -> FF :
     |          Return the forcefield that contains the molecule group
     |          identified by the ID mgid
     |          Throw: SireMol::missing_group
     |          Throw: SireMol::duplicate_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireFF::FF forceField(SireSystem::System {lvalue},SireMol::MGID)
     |  
     |  forceFields(...)
     |      forceFields( (System)arg1) -> ForceFields :
     |          Return an array of all of the forcefields in this system
     |      
     |          C++ signature :
     |              SireFF::ForceFields forceFields(SireSystem::System {lvalue})
     |  
     |  hasComponent(...)
     |      hasComponent( (System)arg1, (Symbol)symbol) -> bool :
     |          Return whether or not this system has a constant or energy
     |          component represented by the symbol symbol
     |      
     |          C++ signature :
     |              bool hasComponent(SireSystem::System {lvalue},SireCAS::Symbol)
     |  
     |  hasConstantComponent(...)
     |      hasConstantComponent( (System)arg1, (Symbol)component) -> bool :
     |          Return whether or not this system has a constant
     |          component with symbol component
     |      
     |          C++ signature :
     |              bool hasConstantComponent(SireSystem::System {lvalue},SireCAS::Symbol)
     |  
     |  hasEnergyComponent(...)
     |      hasEnergyComponent( (System)arg1, (Symbol)component) -> bool :
     |          Return whether or not this system has an energy component component
     |      
     |          C++ signature :
     |              bool hasEnergyComponent(SireSystem::System {lvalue},SireCAS::Symbol)
     |  
     |  isBuiltinProperty(...)
     |      isBuiltinProperty( (System)arg1, (StringProperty)name) -> bool :
     |          Return whether or not the property name exists and is a builtin
     |          property of one of the forcefields in this System
     |      
     |          C++ signature :
     |              bool isBuiltinProperty(SireSystem::System {lvalue},QString)
     |  
     |  isClean(...)
     |      isClean( (System)arg1) -> bool :
     |          Return whether or not all of the forcefields are clean
     |      
     |          C++ signature :
     |              bool isClean(SireSystem::System {lvalue})
     |  
     |  isCompoundProperty(...)
     |      isCompoundProperty( (System)arg1, (StringProperty)name) -> bool :
     |          Return whether or not the property name exists and is a compound
     |          property (either a link or a combined property)
     |      
     |          C++ signature :
     |              bool isCompoundProperty(SireSystem::System {lvalue},QString)
     |  
     |  isConstantComponent(...)
     |      isConstantComponent( (System)arg1, (Symbol)component) -> bool :
     |          Return whether or not the system component component
     |          is a constant component
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              bool isConstantComponent(SireSystem::System {lvalue},SireCAS::Symbol)
     |  
     |  isDirty(...)
     |      isDirty( (System)arg1) -> bool :
     |          Return whether or not any of the forcefields are dirty
     |      
     |          C++ signature :
     |              bool isDirty(SireSystem::System {lvalue})
     |  
     |  isEnergyComponent(...)
     |      isEnergyComponent( (System)arg1, (Symbol)component) -> bool :
     |          Return whether or not the component component is an energy component
     |          Throw: SireFF::missing_component
     |          
     |      
     |          C++ signature :
     |              bool isEnergyComponent(SireSystem::System {lvalue},SireCAS::Symbol)
     |  
     |  isUserProperty(...)
     |      isUserProperty( (System)arg1, (StringProperty)name) -> bool :
     |          Return whether or not the property name exists and is a user
     |          supplied property (either a compound property or an extra
     |          System property)
     |      
     |          C++ signature :
     |              bool isUserProperty(SireSystem::System {lvalue},QString)
     |  
     |  monitor(...)
     |      monitor( (System)arg1, (MonitorID)monid) -> SystemMonitor :
     |          Return the monitor at ID monid
     |          Throw: SireSystem::missing_monitor
     |          Throw: SireSystem::duplicate_monitor
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireSystem::SystemMonitor monitor(SireSystem::System {lvalue},SireSystem::MonitorID)
     |  
     |  monitorName(...)
     |      monitorName( (System)arg1, (MonitorID)monid) -> MonitorName :
     |          Return the name of the monitor at ID monid
     |          Throw: SireSystem::missing_monitor
     |          Throw: SireSystem::duplicate_monitor
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireSystem::MonitorName monitorName(SireSystem::System {lvalue},SireSystem::MonitorID)
     |  
     |  monitors(...)
     |      monitors( (System)arg1, (MonitorID)monid) -> object :
     |          Return the monitors with ID monid
     |          Throw: SireSystem::missing_monitor
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QList<SireBase::PropPtr<SireSystem::SystemMonitor> > monitors(SireSystem::System {lvalue},SireSystem::MonitorID)
     |      
     |      monitors( (System)arg1) -> SystemMonitors :
     |          Return the list of all monitors of this system
     |      
     |          C++ signature :
     |              SireSystem::SystemMonitors monitors(SireSystem::System {lvalue})
     |  
     |  mustNowRecalculateFromScratch(...)
     |      mustNowRecalculateFromScratch( (System)arg1) -> None :
     |          Tell all of the forcefields that they will need to recalculate
     |          their energies from scratch. This can speed up calculations where
     |          you know that the majority (or all) of the molecules will be
     |          changing
     |      
     |          C++ signature :
     |              void mustNowRecalculateFromScratch(SireSystem::System {lvalue})
     |  
     |  nConstraints(...)
     |      nConstraints( (System)arg1) -> int :
     |          Return the number of constraints on the system
     |      
     |          C++ signature :
     |              int nConstraints(SireSystem::System {lvalue})
     |  
     |  nForceFields(...)
     |      nForceFields( (System)arg1) -> int :
     |          Return the number of forcefields in this system
     |      
     |          C++ signature :
     |              int nForceFields(SireSystem::System {lvalue})
     |  
     |  nMonitors(...)
     |      nMonitors( (System)arg1) -> int :
     |          Return the number of monitors in this system
     |      
     |          C++ signature :
     |              int nMonitors(SireSystem::System {lvalue})
     |  
     |  name(...)
     |      name( (System)arg1) -> SysName :
     |      
     |          C++ signature :
     |              SireSystem::SysName name(SireSystem::System {lvalue})
     |  
     |  needsAccepting(...)
     |      needsAccepting( (System)arg1) -> bool :
     |          Return whether or not any part of the forcefield is using temporary
     |          workspaces that need to be accepted
     |      
     |          C++ signature :
     |              bool needsAccepting(SireSystem::System {lvalue})
     |  
     |  potential(...)
     |      potential( (System)arg1, (PotentialTable)pottable, (Probe)probe [, (object)scale_potential=1]) -> None :
     |          Add the potentials acting on the molecules in the potential table pottable
     |          from this system onto this potential table, scaled by the optionally
     |          supplied scale_potential
     |      
     |          C++ signature :
     |              void potential(SireSystem::System {lvalue},SireFF::PotentialTable {lvalue},SireFF::Probe [,double=1])
     |      
     |      potential( (System)arg1, (PotentialTable)pottable, (Symbol)component, (Probe)probe [, (object)scale_potential=1]) -> None :
     |          Add the potentials acting on the molecules in the potential table pottable
     |          from the component of this system identified by component onto
     |          this potential table, scaled by the optionally supplied scale_potential
     |      
     |          C++ signature :
     |              void potential(SireSystem::System {lvalue},SireFF::PotentialTable {lvalue},SireCAS::Symbol,SireFF::Probe [,double=1])
     |      
     |      potential( (System)arg1, (PotentialTable)pottable [, (object)scale_potential=1]) -> None :
     |          Add the potentials acting on the molecules in the potential table pottable
     |          from this system onto this potential table, scaled by the optionally
     |          supplied scale_potential
     |      
     |          C++ signature :
     |              void potential(SireSystem::System {lvalue},SireFF::PotentialTable {lvalue} [,double=1])
     |      
     |      potential( (System)arg1, (PotentialTable)pottable, (Symbol)component [, (object)scale_potential=1]) -> None :
     |          Add the potentials acting on the molecules in the potential table pottable
     |          from the component of this system identified by component onto
     |          this potential table, scaled by the optionally supplied scale_potential
     |      
     |          C++ signature :
     |              void potential(SireSystem::System {lvalue},SireFF::PotentialTable {lvalue},SireCAS::Symbol [,double=1])
     |  
     |  properties(...)
     |      properties( (System)arg1) -> Properties :
     |          Return the values of all of the properties of this system
     |          Throw: SireBase::duplicate_property
     |          
     |      
     |          C++ signature :
     |              SireBase::Properties properties(SireSystem::System {lvalue})
     |      
     |      properties( (System)arg1, (FFID)ffid) -> Properties :
     |          Return the values of all of the properties of this system that
     |          are in the forcefields that match the ID ffid
     |          Throw: SireBase::duplicate_property
     |          Throw: SireFF::missing_forcefield
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireBase::Properties properties(SireSystem::System {lvalue},SireFF::FFID)
     |  
     |  property(...)
     |      property( (System)arg1, (PropertyName)name) -> Property :
     |          Return the values of the property called name in all of the
     |          forcefields that contain this property
     |          Throw: SireBase::missing_property
     |          Throw: SireBase::duplicate_property
     |          
     |      
     |          C++ signature :
     |              SireBase::Property property(SireSystem::System {lvalue},SireBase::PropertyName)
     |      
     |      property( (System)arg1, (FFID)ffid, (PropertyName)name) -> Property :
     |          Return the value of the property name in the forcefield identified
     |          by the ID ffid
     |          Throw: SireBase::duplicate_property
     |          Throw: SireFF::missing_forcefield
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireBase::Property property(SireSystem::System {lvalue},SireFF::FFID,SireBase::PropertyName)
     |  
     |  propertyKeys(...)
     |      propertyKeys( (System)arg1) -> object :
     |          Return the names of all of the properties of this system
     |      
     |          C++ signature :
     |              QStringList propertyKeys(SireSystem::System {lvalue})
     |      
     |      propertyKeys( (System)arg1, (FFID)ffid) -> object :
     |          Return the names of all of the properties of the forcefields in
     |          this system that match the ID ffid
     |          Throw: SireFF::missing_forcefield
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QStringList propertyKeys(SireSystem::System {lvalue},SireFF::FFID)
     |  
     |  remove(...)
     |      remove( (System)arg1, (MonitorID)monid) -> None :
     |          Remove all monitors that match the ID monid
     |          Throw: SireSystem::missing_monitor
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              void remove(SireSystem::System {lvalue},SireSystem::MonitorID)
     |      
     |      remove( (System)arg1, (FFID)ffid) -> None :
     |          Remove the forcefield(s) that match the ID ffid
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              void remove(SireSystem::System {lvalue},SireFF::FFID)
     |      
     |      remove( (System)arg1, (FF)ff) -> None :
     |          Remove the forcefield ff. Note that this removes the forcefield
     |          in this system that has the same name as ff
     |          Throw: SireFF::missing_forcefield
     |          
     |      
     |          C++ signature :
     |              void remove(SireSystem::System {lvalue},SireFF::FF)
     |      
     |      remove( (System)arg1, (MGID)mgid) -> bool :
     |          Remove the molecule group(s) that match the ID mgid.
     |          Note that you cant remove molecule groups that are part
     |          of a forcefield
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_arg
     |          
     |      
     |          C++ signature :
     |              bool remove(SireSystem::System {lvalue},SireMol::MGID)
     |      
     |      remove( (System)arg1, (MoleculeGroup)molgroup) -> bool :
     |          Remove the molecules contained in the molecule group molgroup.
     |          This doesnt remove the molecule group itself though. If you
     |          want to remove the molecule group, use System::remove(molgroup.number())
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              bool remove(SireSystem::System {lvalue},SireMol::MoleculeGroup)
     |      
     |      remove( (System)arg1, (MolID)molid) -> bool :
     |          Remove all molecules from this system that match the ID molid
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              bool remove(SireSystem::System {lvalue},SireMol::MolID)
     |      
     |      remove( (System)arg1, (Constraint)constraint) -> None :
     |          Remove the constraints in constraints from the list of constraints
     |          that are applied to this system
     |      
     |          C++ signature :
     |              void remove(SireSystem::System {lvalue},SireSystem::Constraint)
     |      
     |      remove( (System)arg1, (Constraints)constraints) -> None :
     |          Remove the constraints in constraints from the list of constraints
     |          that are applied to this system
     |      
     |          C++ signature :
     |              void remove(SireSystem::System {lvalue},SireSystem::Constraints)
     |      
     |      remove( (System)arg1, (MoleculeView)molview, (MGID)mgid) -> bool :
     |          Remove the view molview from the specified groups in this
     |          forcefield. Note that this only removes the specific view
     |          (and indeed only the first copy of this view if there
     |          are duplicates) - it does not remove the atoms in this
     |          view from all of the other views
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              bool remove(SireSystem::System {lvalue},SireMol::MoleculeView,SireMol::MGID)
     |      
     |      remove( (System)arg1, (object)molviews, (MGID)mgid) -> bool :
     |          Remove the views in molviews from the specified groups in this
     |          forcefield. Note that this only removes the specific views
     |          (and indeed only the first copy of this view if there
     |          are duplicates) - it does not remove the atoms in this
     |          view from all of the other views
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              bool remove(SireSystem::System {lvalue},SireMol::ViewsOfMol,SireMol::MGID)
     |      
     |      remove( (System)arg1, (Molecules)molecules, (MGID)mgid) -> bool :
     |          Remove them molecules in molecules from the specified groups in this
     |          forcefield. Note that this only removes the specific views
     |          (and indeed only the first copy of this view if there
     |          are duplicates) - it does not remove the atoms in this
     |          view from all of the other views
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              bool remove(SireSystem::System {lvalue},SireMol::Molecules,SireMol::MGID)
     |      
     |      remove( (System)arg1, (MoleculeGroup)molgroup, (MGID)mgid) -> bool :
     |          Remove the views in the molecule group molgroup from the specified
     |          groups in this forcefield. Note that this only removes the specific views
     |          (and indeed only the first copy of this view if there
     |          are duplicates) - it does not remove the atoms in this
     |          view from all of the other views
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              bool remove(SireSystem::System {lvalue},SireMol::MoleculeGroup,SireMol::MGID)
     |      
     |      remove( (System)arg1, (MolNum)molnum, (MGID)mgid) -> bool :
     |          Remove all views of the molecule with number molnum from the molecule
     |          groups identified by mgid
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              bool remove(SireSystem::System {lvalue},SireMol::MolNum,SireMol::MGID)
     |      
     |      remove( (System)arg1, (object)molnums, (MGID)mgid) -> bool :
     |          Remove all of the molecules whose numbers are in molnums from
     |          all of the molecule groups identified by the ID mgid
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              bool remove(SireSystem::System {lvalue},QSet<SireMol::MolNum>,SireMol::MGID)
     |  
     |  removeAll(...)
     |      removeAll( (System)arg1, (MGID)mgid) -> bool :
     |          Remove all molecules from the molecule groups identified by the ID mgid
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              bool removeAll(SireSystem::System {lvalue},SireMol::MGID)
     |      
     |      removeAll( (System)arg1, (MoleculeView)molview, (MGID)mgid) -> bool :
     |          Remove the all copies of the view in molview from the specified
     |          groups in this forcefield. Note that this only removes the specific views
     |          - it does not remove the atoms in this view from all of the other views
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              bool removeAll(SireSystem::System {lvalue},SireMol::MoleculeView,SireMol::MGID)
     |      
     |      removeAll( (System)arg1, (object)molviews, (MGID)mgid) -> bool :
     |          Remove the all copies of the views in molviews from the specified
     |          groups in this forcefield. Note that this only removes the specific views
     |          - it does not remove the atoms in this view from all of the other views
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              bool removeAll(SireSystem::System {lvalue},SireMol::ViewsOfMol,SireMol::MGID)
     |      
     |      removeAll( (System)arg1, (Molecules)molecules, (MGID)mgid) -> bool :
     |          Remove the all copies of the molecules in molecules from the specified
     |          groups in this forcefield. Note that this only removes the specific views
     |          - it does not remove the atoms in this view from all of the other views
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              bool removeAll(SireSystem::System {lvalue},SireMol::Molecules,SireMol::MGID)
     |      
     |      removeAll( (System)arg1, (MoleculeGroup)molgroup, (MGID)mgid) -> bool :
     |          Remove the all copies of the molecules in the molecule group molgroup
     |          from the specified groups in this forcefield. Note that this only removes
     |          the specific views - it does not remove the atoms in this view from all
     |          of the other views
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              bool removeAll(SireSystem::System {lvalue},SireMol::MoleculeGroup,SireMol::MGID)
     |  
     |  removeAllConstraints(...)
     |      removeAllConstraints( (System)arg1) -> None :
     |          Remove all constraints from this system
     |      
     |          C++ signature :
     |              void removeAllConstraints(SireSystem::System {lvalue})
     |  
     |  removeAllForceFields(...)
     |      removeAllForceFields( (System)arg1) -> None :
     |          Completely remove all of the forcefields (and their contained
     |          molecule groups) from this system
     |      
     |          C++ signature :
     |              void removeAllForceFields(SireSystem::System {lvalue})
     |  
     |  removeAllMoleculeGroups(...)
     |      removeAllMoleculeGroups( (System)arg1) -> None :
     |          Completely remove all non-forcefield molecule groups
     |          from this system
     |      
     |          C++ signature :
     |              void removeAllMoleculeGroups(SireSystem::System {lvalue})
     |  
     |  removeAllMolecules(...)
     |      removeAllMolecules( (System)arg1) -> bool :
     |          Completely remove all molecules from this system
     |      
     |          C++ signature :
     |              bool removeAllMolecules(SireSystem::System {lvalue})
     |  
     |  removeAllMonitors(...)
     |      removeAllMonitors( (System)arg1) -> None :
     |          Completely remove all monitors from this system
     |      
     |          C++ signature :
     |              void removeAllMonitors(SireSystem::System {lvalue})
     |  
     |  removeProperty(...)
     |      removeProperty( (System)arg1, (StringProperty)name) -> None :
     |          Remove the property with name name. Note that this can only
     |          remove user-level properties - it cannot remove built-in properties
     |          of the system. This does nothing if there is no user-level
     |          property with this name
     |      
     |          C++ signature :
     |              void removeProperty(SireSystem::System {lvalue},QString)
     |  
     |  setComponent(...)
     |      setComponent( (System)arg1, (Symbol)symbol, (object)value) -> None :
     |          Synonym for System::setConstantComponent(symbol, value)
     |      
     |          C++ signature :
     |              void setComponent(SireSystem::System {lvalue},SireCAS::Symbol,double)
     |      
     |      setComponent( (System)arg1, (Symbol)symbol, (Expression)expression) -> None :
     |          Synonym for System::setEnergyComponent(symbol, expression)
     |      
     |          C++ signature :
     |              void setComponent(SireSystem::System {lvalue},SireCAS::Symbol,SireCAS::Expression)
     |  
     |  setConstant(...)
     |      setConstant( (System)arg1, (Symbol)symbol, (object)value) -> None :
     |      
     |          C++ signature :
     |              void setConstant(SireSystem::System {lvalue},SireCAS::Symbol,double)
     |      
     |      setConstant( (System)arg1, (Symbol)symbol, (Expression)expression) -> None :
     |      
     |          C++ signature :
     |              void setConstant(SireSystem::System {lvalue},SireCAS::Symbol,SireCAS::Expression)
     |  
     |  setConstantComponent(...)
     |      setConstantComponent( (System)arg1, (Symbol)symbol, (object)value) -> None :
     |          Set the constant component symbol to the value value
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setConstantComponent(SireSystem::System {lvalue},SireCAS::Symbol,double)
     |      
     |      setConstantComponent( (System)arg1, (Symbol)symbol, (Expression)expression) -> None :
     |          Set the constant component symbol to the expression
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setConstantComponent(SireSystem::System {lvalue},SireCAS::Symbol,SireCAS::Expression)
     |  
     |  setConstraints(...)
     |      setConstraints( (System)arg1, (Constraints)constraints) -> None :
     |          Set the constraints for the system equal to constraints
     |      
     |          C++ signature :
     |              void setConstraints(SireSystem::System {lvalue},SireSystem::Constraints)
     |  
     |  setContents(...)
     |      setContents( (System)arg1, (MGID)mgid, (MoleculeView)molview, (PropertyMap)map) -> None :
     |          Set the contents of the molecule group(s) identified by the ID mgid
     |          so that they contain just the view of the molecule in molview.
     |          The version of the molecule already present in this set is used if
     |          such a molecule already exists. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setContents(SireSystem::System {lvalue},SireMol::MGID,SireMol::MoleculeView,SireBase::PropertyMap)
     |      
     |      setContents( (System)arg1, (MGID)mgid, (object)molviews, (PropertyMap)map) -> None :
     |          Set the contents of the molecule group(s) identified by the ID mgid
     |          so that they contain just the views of the molecule in molviews.
     |          The version of the molecule already present in this set is used if
     |          such a molecule already exists. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setContents(SireSystem::System {lvalue},SireMol::MGID,SireMol::ViewsOfMol,SireBase::PropertyMap)
     |      
     |      setContents( (System)arg1, (MGID)mgid, (Molecules)molecules, (PropertyMap)map) -> None :
     |          Set the contents of the molecule group(s) identified by the ID mgid
     |          so that they contain just the views of the molecules in molecules.
     |          The version of the molecule already present in this set is used if
     |          such a molecule already exists. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setContents(SireSystem::System {lvalue},SireMol::MGID,SireMol::Molecules,SireBase::PropertyMap)
     |      
     |      setContents( (System)arg1, (MGID)mgid, (MoleculeGroup)molgroup, (PropertyMap)map) -> None :
     |          Set the contents of the molecule group(s) identified by the ID mgid
     |          so that they contain just the molecules in the group molgroup.
     |          The version of the molecule already present in this set is used if
     |          such a molecule already exists. The supplied property map
     |          is used to find the properties required by any forcefields
     |          that this molecule may be added to.
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setContents(SireSystem::System {lvalue},SireMol::MGID,SireMol::MoleculeGroup,SireBase::PropertyMap)
     |      
     |      setContents( (System)arg1, (MGID)mgid, (MoleculeView)molview) -> None :
     |          Convenient overload of System::setContents that uses the default
     |          property locations to find the properties required by the forcefields
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setContents(SireSystem::System {lvalue},SireMol::MGID,SireMol::MoleculeView)
     |      
     |      setContents( (System)arg1, (MGID)mgid, (object)molviews) -> None :
     |          Convenient overload of System::setContents that uses the default
     |          property locations to find the properties required by the forcefields
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setContents(SireSystem::System {lvalue},SireMol::MGID,SireMol::ViewsOfMol)
     |      
     |      setContents( (System)arg1, (MGID)mgid, (Molecules)molecules) -> None :
     |          Convenient overload of System::setContents that uses the default
     |          property locations to find the properties required by the forcefields
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setContents(SireSystem::System {lvalue},SireMol::MGID,SireMol::Molecules)
     |      
     |      setContents( (System)arg1, (MGID)mgid, (MoleculeGroup)molgroup) -> None :
     |          Convenient overload of System::setContents that uses the default
     |          property locations to find the properties required by the forcefields
     |          Throw: SireMol::missing_group
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_index
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setContents(SireSystem::System {lvalue},SireMol::MGID,SireMol::MoleculeGroup)
     |  
     |  setEnergyComponent(...)
     |      setEnergyComponent( (System)arg1, (Symbol)symbol, (Expression)expression) -> None :
     |          Set the energy component symbol equal to the expression expression
     |      
     |          C++ signature :
     |              void setEnergyComponent(SireSystem::System {lvalue},SireCAS::Symbol,SireCAS::Expression)
     |  
     |  setMonitors(...)
     |      setMonitors( (System)arg1, (SystemMonitors)monitors) -> None :
     |          Set the monitors of this system to monitors
     |      
     |          C++ signature :
     |              void setMonitors(SireSystem::System {lvalue},SireSystem::SystemMonitors)
     |      
     |      setMonitors( (System)arg1, (SystemMonitors)monitors, (int)frequency) -> None :
     |          Set the monitors of the system to monitors, and reset the
     |          frequency of all of the monitors so that they are triggered
     |          every frequency steps
     |      
     |          C++ signature :
     |              void setMonitors(SireSystem::System {lvalue},SireSystem::SystemMonitors,int)
     |  
     |  setName(...)
     |      setName( (System)arg1, (StringProperty)newname) -> None :
     |          Set the name of this system
     |      
     |          C++ signature :
     |              void setName(SireSystem::System {lvalue},QString)
     |  
     |  setProperty(...)
     |      setProperty( (System)arg1, (StringProperty)name, (Property)value) -> None :
     |          Set the value of the property called name to the value value in
     |          all forcefields that have this property
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setProperty(SireSystem::System {lvalue},QString,SireBase::Property)
     |      
     |      setProperty( (System)arg1, (FFID)ffid, (StringProperty)name, (Property)value) -> None :
     |          Set the value of the property called name in the forcefields identified
     |          by the ID ffid to the value value
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void setProperty(SireSystem::System {lvalue},SireFF::FFID,QString,SireBase::Property)
     |  
     |  subVersion(...)
     |      subVersion( (System)arg1) -> int :
     |      
     |          C++ signature :
     |              unsigned int subVersion(SireSystem::System {lvalue})
     |  
     |  toString(...)
     |      toString( (System)arg1) -> object :
     |          Return a string representation of this system
     |      
     |          C++ signature :
     |              QString toString(SireSystem::System {lvalue})
     |  
     |  totalComponent(...)
     |      totalComponent( (System)arg1) -> Symbol :
     |          Return the symbol that represents the total energy component
     |          of the system
     |      
     |          C++ signature :
     |              SireCAS::Symbol totalComponent(SireSystem::System {lvalue})
     |  
     |  update(...)
     |      update( (System)arg1, (MoleculeView)moldata [, (bool)auto_commit=True]) -> None :
     |          Update this system so that it uses the version of the molecule
     |          available in moldata
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void update(SireSystem::System {lvalue},SireMol::MoleculeData [,bool=True])
     |      
     |      update( (System)arg1, (Molecules)molecules [, (bool)auto_commit=True]) -> None :
     |          Update this system so that it uses the same version of the molecules
     |          present in molecules
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void update(SireSystem::System {lvalue},SireMol::Molecules [,bool=True])
     |      
     |      update( (System)arg1, (MoleculeGroup)molgroup [, (bool)auto_commit=True]) -> None :
     |          Update this system so that it uses the same version of the molecules
     |          present in the molecule group molgroup
     |          Throw: SireBase::missing_property
     |          Throw: SireError::invalid_cast
     |          Throw: SireError::incompatible_error
     |          
     |      
     |          C++ signature :
     |              void update(SireSystem::System {lvalue},SireMol::MoleculeGroup [,bool=True])
     |  
     |  userProperties(...)
     |      userProperties( (System)arg1) -> Properties :
     |          Return the values of all user-level properties of this
     |          system
     |      
     |          C++ signature :
     |              SireBase::Properties userProperties(SireSystem::System {lvalue})
     |  
     |  userProperty(...)
     |      userProperty( (System)arg1, (StringProperty)name) -> Property :
     |          Return the user-supplied property at name. This raises an
     |          exception if there is no user-supplied property with this name
     |          Throw: SireBase::missing_property
     |          
     |      
     |          C++ signature :
     |              SireBase::Property userProperty(SireSystem::System {lvalue},QString)
     |  
     |  version(...)
     |      version( (System)arg1) -> Version :
     |      
     |          C++ signature :
     |              SireBase::Version version(SireSystem::System {lvalue})
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  null(...)
     |      null() -> System :
     |      
     |          C++ signature :
     |              SireSystem::System null()
     |  
     |  typeName(...)
     |      typeName() -> str :
     |      
     |          C++ signature :
     |              char const* typeName()
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __instance_size__ = 216
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Sire.Mol._Mol.MolGroupsBase:
     |  
     |  assertContains(...)
     |      assertContains( (MolGroupsBase)arg1, (MolNum)molnum) -> None :
     |          Assert that this set contains at least one atom of the
     |          molecule with number molnum
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              void assertContains(SireMol::MolGroupsBase {lvalue},SireMol::MolNum)
     |      
     |      assertContains( (MolGroupsBase)arg1, (MolID)molid) -> None :
     |          Assert that this set contains at least one atom of any
     |          molecule that is identified by the ID molid
     |          Throw: SireMol::missing_molecule
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              void assertContains(SireMol::MolGroupsBase {lvalue},SireMol::MolID)
     |      
     |      assertContains( (MolGroupsBase)arg1, (MGNum)mgnum) -> None :
     |          Assert that this contains the molecule group with number mgnum
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              void assertContains(SireMol::MolGroupsBase {lvalue},SireMol::MGNum)
     |      
     |      assertContains( (MolGroupsBase)arg1, (MGID)mgid) -> None :
     |          Assert that this contains at least one molecule group that
     |          is identified by the ID mgid
     |          Throw: SireMol:missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              void assertContains(SireMol::MolGroupsBase {lvalue},SireMol::MGID)
     |  
     |  atom(...)
     |      atom( (MolGroupsBase)arg1, (AtomID)atomid) -> Atom :
     |          Return the atom that matches the ID atomid
     |          Throw: SireMol::missing_atom
     |          Throw: SireMol::duplicate_atom
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::Atom atom(SireMol::MolGroupsBase {lvalue},SireMol::AtomID)
     |  
     |  atoms(...)
     |      atoms( (MolGroupsBase)arg1, (AtomID)atomid) -> object :
     |          Return all of the atoms from this set that match the ID atomid.
     |          The returned atoms are arranged by molecule, and only one copy
     |          of each atom is returned, regardless of how many times it appears
     |          in this set.
     |          Throw: SireMol::missing_atom
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QHash<SireMol::MolNum, SireMol::Selector<SireMol::Atom> > atoms(SireMol::MolGroupsBase {lvalue},SireMol::AtomID)
     |  
     |  chain(...)
     |      chain( (MolGroupsBase)arg1, (ChainID)chainid) -> Chain :
     |          Return the chain that matches the ID chainid
     |          Throw: SireMol::missing_chain
     |          Throw: SireMol::duplicate_chain
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::Chain chain(SireMol::MolGroupsBase {lvalue},SireMol::ChainID)
     |  
     |  chains(...)
     |      chains( (MolGroupsBase)arg1, (ChainID)chainid) -> object :
     |          Return all of the chains from this set that match the ID chainid.
     |          The returned chains are arranged by molecule, and only one copy
     |          of each chain is returned, regardless of how many times it appears
     |          in this set.
     |          Throw: SireMol::missing_chain
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QHash<SireMol::MolNum, SireMol::Selector<SireMol::Chain> > chains(SireMol::MolGroupsBase {lvalue},SireMol::ChainID)
     |  
     |  contains(...)
     |      contains( (MolGroupsBase)arg1, (MGNum)mgnum) -> bool :
     |          Return whether or not this set contains the group with number mgnum
     |      
     |          C++ signature :
     |              bool contains(SireMol::MolGroupsBase {lvalue},SireMol::MGNum)
     |      
     |      contains( (MolGroupsBase)arg1, (MolNum)molnum) -> bool :
     |          Return whether any of the groups contain any view of the molecule
     |          with number molnum
     |      
     |          C++ signature :
     |              bool contains(SireMol::MolGroupsBase {lvalue},SireMol::MolNum)
     |      
     |      contains( (MolGroupsBase)arg1, (object)molnums) -> bool :
     |          Return whether any of the groups contains any of the molecules whose
     |          numbers are in molnums
     |      
     |          C++ signature :
     |              bool contains(SireMol::MolGroupsBase {lvalue},QList<SireMol::MolNum>)
     |      
     |      contains( (MolGroupsBase)arg1, (MoleculeView)molview) -> bool :
     |          Return whether or not any of the groups contains the view molview
     |      
     |          C++ signature :
     |              bool contains(SireMol::MolGroupsBase {lvalue},SireMol::MoleculeView)
     |      
     |      contains( (MolGroupsBase)arg1, (object)molviews) -> bool :
     |          Return whether or not this set contains all of the views of
     |          the molecule in molviews. The views can be contained in
     |          multiple groups.
     |      
     |          C++ signature :
     |              bool contains(SireMol::MolGroupsBase {lvalue},SireMol::ViewsOfMol)
     |      
     |      contains( (MolGroupsBase)arg1, (Molecules)molecules) -> bool :
     |          Return whether or not this set of groups contains all of the views
     |          of all of the molecules in molecules. These views can be spread
     |          over lots of groups
     |      
     |          C++ signature :
     |              bool contains(SireMol::MolGroupsBase {lvalue},SireMol::Molecules)
     |  
     |  count(...)
     |      count( (MolGroupsBase)arg1) -> int :
     |          Return the total number of groups in this set
     |      
     |          C++ signature :
     |              int count(SireMol::MolGroupsBase {lvalue})
     |  
     |  cutGroup(...)
     |      cutGroup( (MolGroupsBase)arg1, (CGID)cgid) -> CutGroup :
     |          Return the CutGroup that matches the ID cgid
     |          Throw: SireMol::missing_cutgroup
     |          Throw: SireMol::duplicate_cutgroup
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::CutGroup cutGroup(SireMol::MolGroupsBase {lvalue},SireMol::CGID)
     |  
     |  cutGroups(...)
     |      cutGroups( (MolGroupsBase)arg1, (CGID)cgid) -> object :
     |          Return all of the CutGroups from this set that match the ID cgid.
     |          The returned CutGroups are arranged by molecule, and only one copy
     |          of each CutGroup is returned, regardless of how many times it appears
     |          in this set.
     |          Throw: SireMol::missing_cutgroup
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QHash<SireMol::MolNum, SireMol::Selector<SireMol::CutGroup> > cutGroups(SireMol::MolGroupsBase {lvalue},SireMol::CGID)
     |  
     |  getGroupNumber(...)
     |      getGroupNumber( (MolGroupsBase)arg1, (MGNum)mgnum) -> MGNum :
     |          Get the number of the molecule group whose number is mgnum.
     |          This is an obvious function, only provided as a shortcut
     |          to prevent the MGID function being called if an MGNum is passed.
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              SireMol::MGNum getGroupNumber(SireMol::MolGroupsBase {lvalue},SireMol::MGNum)
     |      
     |      getGroupNumber( (MolGroupsBase)arg1, (MGIdx)mgidx) -> MGNum :
     |          Return the number of the group at index mgidx
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::MGNum getGroupNumber(SireMol::MolGroupsBase {lvalue},SireMol::MGIdx)
     |      
     |      getGroupNumber( (MolGroupsBase)arg1, (MGName)mgname) -> MGNum :
     |          Return the number of the molecule group that is called mgname.
     |          Throw: SireMol::missing_group
     |          Throw: SireMol::duplicate_group
     |          
     |      
     |          C++ signature :
     |              SireMol::MGNum getGroupNumber(SireMol::MolGroupsBase {lvalue},SireMol::MGName)
     |      
     |      getGroupNumber( (MolGroupsBase)arg1, (MGID)mgid) -> MGNum :
     |          Return the number of the groups that matches mgid
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::MGNum getGroupNumber(SireMol::MolGroupsBase {lvalue},SireMol::MGID)
     |  
     |  getMoleculeNumber(...)
     |      getMoleculeNumber( (MolGroupsBase)arg1, (MolNum)molnum) -> MolNum :
     |          Simple function that just checks if a molecule with number
     |          molnum is in the set, and returns it. This shortcuts
     |          the getMoleculeNumber(const MolID&) function in the case
     |          of MolNums
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              SireMol::MolNum getMoleculeNumber(SireMol::MolGroupsBase {lvalue},SireMol::MolNum)
     |      
     |      getMoleculeNumber( (MolGroupsBase)arg1, (MolIdx)molidx) -> MolNum :
     |          Return the number of the molecule at index molidx in
     |          this set
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::MolNum getMoleculeNumber(SireMol::MolGroupsBase {lvalue},SireMol::MolIdx)
     |      
     |      getMoleculeNumber( (MolGroupsBase)arg1, (MolName)molname) -> MolNum :
     |          Return the number of the molecule called molname from this set.
     |          Throw: SireMol::missing_molecule
     |          Throw: SireMol::duplicate_molecule
     |          
     |      
     |          C++ signature :
     |              SireMol::MolNum getMoleculeNumber(SireMol::MolGroupsBase {lvalue},SireMol::MolName)
     |      
     |      getMoleculeNumber( (MolGroupsBase)arg1, (MolID)molid) -> MolNum :
     |          Return the number of the molecule that matches the ID molid
     |          Throw: SireMol::missing_molecule
     |          Throw: SireMol::duplicate_molecule
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::MolNum getMoleculeNumber(SireMol::MolGroupsBase {lvalue},SireMol::MolID)
     |  
     |  getMoleculeNumbers(...)
     |      getMoleculeNumbers( (MolGroupsBase)arg1) -> object :
     |          Return the list of molecule numbers in molidx order
     |      
     |          C++ signature :
     |              QList<SireMol::MolNum> getMoleculeNumbers(SireMol::MolGroupsBase {lvalue})
     |  
     |  getMoleculeVersion(...)
     |      getMoleculeVersion( (MolGroupsBase)arg1, (MolNum)molnum) -> int :
     |          Return the version number of the molecule with number molnum
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              unsigned long long getMoleculeVersion(SireMol::MolGroupsBase {lvalue},SireMol::MolNum)
     |      
     |      getMoleculeVersion( (MolGroupsBase)arg1, (MolID)molid) -> int :
     |          Return the version number of the molecule with ID molid
     |          Throw: SireMol::missing_molecule
     |          Throw: SireMol::duplicate_molecule
     |          
     |      
     |          C++ signature :
     |              unsigned long long getMoleculeVersion(SireMol::MolGroupsBase {lvalue},SireMol::MolID)
     |  
     |  group(...)
     |      group( (MolGroupsBase)arg1, (MGNum)mgnum) -> MoleculeGroup :
     |          Return the molecule group that has number mgnum
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              SireMol::MoleculeGroup group(SireMol::MolGroupsBase {lvalue},SireMol::MGNum)
     |      
     |      group( (MolGroupsBase)arg1, (MGName)mgname) -> MoleculeGroup :
     |          Return the molecule group that has name mgname
     |          Throw: SireMol::missing_group
     |          Throw: SireMol::duplicate_group
     |          
     |      
     |          C++ signature :
     |              SireMol::MoleculeGroup group(SireMol::MolGroupsBase {lvalue},SireMol::MGName)
     |      
     |      group( (MolGroupsBase)arg1, (MGIdx)mgidx) -> MoleculeGroup :
     |          Return the molecule group at index mgidx
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::MoleculeGroup group(SireMol::MolGroupsBase {lvalue},SireMol::MGIdx)
     |      
     |      group( (MolGroupsBase)arg1, (MGID)mgid) -> MoleculeGroup :
     |          Return the molecule group that matches the ID mgid
     |          Throw: SireMol::missing_group
     |          Throw: SireMol::duplicate_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::MoleculeGroup group(SireMol::MolGroupsBase {lvalue},SireMol::MGID)
     |  
     |  groupNames(...)
     |      groupNames( (MolGroupsBase)arg1) -> object :
     |          Return a list of the names of all of the groups in this set
     |      
     |          C++ signature :
     |              QList<SireMol::MGName> groupNames(SireMol::MolGroupsBase {lvalue})
     |  
     |  groupNumbers(...)
     |      groupNumbers( (MolGroupsBase)arg1) -> object :
     |          Return a list of the numbers of all of the groups in this set
     |      
     |          C++ signature :
     |              QList<SireMol::MGNum> groupNumbers(SireMol::MolGroupsBase {lvalue})
     |  
     |  groups(...)
     |      groups( (MolGroupsBase)arg1) -> object :
     |          Return a list of all of the molecule groups in this set
     |      
     |          C++ signature :
     |              QList<SireBase::PropPtr<SireMol::MoleculeGroup> > groups(SireMol::MolGroupsBase {lvalue})
     |      
     |      groups( (MolGroupsBase)arg1, (MGNum)mgnum) -> object :
     |          Obvious shortcut for groups(const MGID&)
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              QList<SireBase::PropPtr<SireMol::MoleculeGroup> > groups(SireMol::MolGroupsBase {lvalue},SireMol::MGNum)
     |      
     |      groups( (MolGroupsBase)arg1, (MGIdx)mgidx) -> object :
     |          Obvious shortcut for groups(const MGID&)
     |          Throw: SireMol::invalid_index
     |          
     |      
     |          C++ signature :
     |              QList<SireBase::PropPtr<SireMol::MoleculeGroup> > groups(SireMol::MolGroupsBase {lvalue},SireMol::MGIdx)
     |      
     |      groups( (MolGroupsBase)arg1, (MGName)mgname) -> object :
     |          Return all of the groups called mgname
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              QList<SireBase::PropPtr<SireMol::MoleculeGroup> > groups(SireMol::MolGroupsBase {lvalue},SireMol::MGName)
     |      
     |      groups( (MolGroupsBase)arg1, (MGID)mgid) -> object :
     |          Return all of the groups that match the ID mgid
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              QList<SireBase::PropPtr<SireMol::MoleculeGroup> > groups(SireMol::MolGroupsBase {lvalue},SireMol::MGID)
     |  
     |  groupsContaining(...)
     |      groupsContaining( (MolGroupsBase)arg1, (MolNum)molnum) -> object :
     |          Return the list of molecule groups numbers of groups that
     |          contain at least one atom of the molecule with number molnum
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::MGNum> groupsContaining(SireMol::MolGroupsBase {lvalue},SireMol::MolNum)
     |  
     |  intersects(...)
     |      intersects( (MolGroupsBase)arg1, (MoleculeView)molview) -> bool :
     |          Return whether or not any of the groups in this set contain any
     |          of the atoms of the view of the molecule in molview
     |      
     |          C++ signature :
     |              bool intersects(SireMol::MolGroupsBase {lvalue},SireMol::MoleculeView)
     |      
     |      intersects( (MolGroupsBase)arg1, (Molecules)other) -> bool :
     |          Return whether any of the groups in this set contain any of the
     |          atoms of any of the views of any of the molecules in molecules
     |      
     |          C++ signature :
     |              bool intersects(SireMol::MolGroupsBase {lvalue},SireMol::Molecules)
     |  
     |  isEmpty(...)
     |      isEmpty( (MolGroupsBase)arg1) -> bool :
     |          Return whether or not this set is empty (contains no groups)
     |      
     |          C++ signature :
     |              bool isEmpty(SireMol::MolGroupsBase {lvalue})
     |  
     |  map(...)
     |      map( (MolGroupsBase)arg1, (MGNum)mgnum) -> object :
     |          Return the list of numbers of groups that have the number mgnum.
     |          This is a simple and obvious function that acts as a shortcut
     |          preventing map(const MGID&) being called for an MGNum
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::MGNum> map(SireMol::MolGroupsBase {lvalue},SireMol::MGNum)
     |      
     |      map( (MolGroupsBase)arg1, (MGIdx)mgidx) -> object :
     |          Return the list (of only one) molecule group that is at
     |          index mgidx
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::MGNum> map(SireMol::MolGroupsBase {lvalue},SireMol::MGIdx)
     |      
     |      map( (MolGroupsBase)arg1, (MGName)mgname) -> object :
     |          Return the numbers of all groups in this set that are called
     |          mgname
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::MGNum> map(SireMol::MolGroupsBase {lvalue},SireMol::MGName)
     |      
     |      map( (MolGroupsBase)arg1, (MGID)mgid) -> object :
     |          Map the molecule group ID mgid to the list of molecule
     |          group numbers of the groups that match this ID in this set.
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::MGNum> map(SireMol::MolGroupsBase {lvalue},SireMol::MGID)
     |      
     |      map( (MolGroupsBase)arg1, (MolNum)molnum) -> object :
     |          Simple function that provides a shortcut for map(const MolID&)
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::MolNum> map(SireMol::MolGroupsBase {lvalue},SireMol::MolNum)
     |      
     |      map( (MolGroupsBase)arg1, (MolIdx)molidx) -> object :
     |          Return the number of the molecule at index molidx
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::MolNum> map(SireMol::MolGroupsBase {lvalue},SireMol::MolIdx)
     |      
     |      map( (MolGroupsBase)arg1, (MolName)molname) -> object :
     |          Return the numbers of all of the molecules that have the
     |          name molname
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::MolNum> map(SireMol::MolGroupsBase {lvalue},SireMol::MolName)
     |      
     |      map( (MolGroupsBase)arg1, (MolID)molid) -> object :
     |          Return the numbers of all molecules that match the ID molid
     |          Throw: SireMol::missing_molecule
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::MolNum> map(SireMol::MolGroupsBase {lvalue},SireMol::MolID)
     |  
     |  mgIdx(...)
     |      mgIdx( (MolGroupsBase)arg1, (MGNum)mgnum) -> MGIdx :
     |          Return the index of the group with number mgnum
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              SireMol::MGIdx mgIdx(SireMol::MolGroupsBase {lvalue},SireMol::MGNum)
     |  
     |  mgNames(...)
     |      mgNames( (MolGroupsBase)arg1) -> object :
     |          Return the names of all molecule groups in this set
     |      
     |          C++ signature :
     |              QList<SireMol::MGName> mgNames(SireMol::MolGroupsBase {lvalue})
     |  
     |  mgNums(...)
     |      mgNums( (MolGroupsBase)arg1) -> object :
     |          Return the numbers of all molecule groups in this set
     |      
     |          C++ signature :
     |              QList<SireMol::MGNum> mgNums(SireMol::MolGroupsBase {lvalue})
     |  
     |  molNums(...)
     |      molNums( (MolGroupsBase)arg1) -> object :
     |          Return the list of molecule numbers in molidx order
     |      
     |          C++ signature :
     |              QList<SireMol::MolNum> molNums(SireMol::MolGroupsBase {lvalue})
     |  
     |  molecule(...)
     |      molecule( (MolGroupsBase)arg1, (MolNum)molnum) -> object :
     |          Return all of the views of the molecule that has number molnum
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              SireMol::ViewsOfMol molecule(SireMol::MolGroupsBase {lvalue},SireMol::MolNum)
     |      
     |      molecule( (MolGroupsBase)arg1, (MolID)molid) -> object :
     |          Return all of the views of the molecule that matches molid
     |          Throw: SireMol::missing_molecule
     |          Throw: SireMol::duplicate_molecule
     |          
     |      
     |          C++ signature :
     |              SireMol::ViewsOfMol molecule(SireMol::MolGroupsBase {lvalue},SireMol::MolID)
     |  
     |  molecules(...)
     |      molecules( (MolGroupsBase)arg1, (MolNum)molnum) -> object :
     |          Obvious shortcut for molecules(const MolID&)
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::ViewsOfMol> molecules(SireMol::MolGroupsBase {lvalue},SireMol::MolNum)
     |      
     |      molecules( (MolGroupsBase)arg1, (MolID)molid) -> object :
     |          Return all of the molecules that match the ID molid
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::ViewsOfMol> molecules(SireMol::MolGroupsBase {lvalue},SireMol::MolID)
     |      
     |      molecules( (MolGroupsBase)arg1) -> Molecules :
     |          Return the complete set of all molecules in this group. If a view of a
     |          molecule appears multiple times in this set then multiple copies of
     |          that view will be placed into the returned Molecules object.
     |          Note that this is a potentially very slow operation
     |      
     |          C++ signature :
     |              SireMol::Molecules molecules(SireMol::MolGroupsBase {lvalue})
     |      
     |      molecules( (MolGroupsBase)arg1, (MGID)mgid) -> Molecules :
     |          Return the complete set of all molecules in the group(s) that
     |          match the ID mgid. If a view of a molecule appears multiple times
     |          in this set then multiple copies of that view will be placed into the
     |          returned molecules object.
     |          Note that this is potentially a very slow function
     |          
     |      
     |          C++ signature :
     |              SireMol::Molecules molecules(SireMol::MolGroupsBase {lvalue},SireMol::MGID)
     |  
     |  nGroups(...)
     |      nGroups( (MolGroupsBase)arg1) -> int :
     |          Return the total number of groups in this set
     |      
     |          C++ signature :
     |              int nGroups(SireMol::MolGroupsBase {lvalue})
     |  
     |  nMolecules(...)
     |      nMolecules( (MolGroupsBase)arg1) -> int :
     |          Return the total number of molecules in the groups in this set
     |      
     |          C++ signature :
     |              int nMolecules(SireMol::MolGroupsBase {lvalue})
     |  
     |  nViews(...)
     |      nViews( (MolGroupsBase)arg1) -> int :
     |          Return the total number of views of molecules in the groups in this set.
     |          Note that if a view appears multiple times, then it will be counted
     |          multiple times
     |      
     |          C++ signature :
     |              int nViews(SireMol::MolGroupsBase {lvalue})
     |      
     |      nViews( (MolGroupsBase)arg1, (MolNum)molnum) -> int :
     |          Return the total number of views of the molecule with number
     |          molnum in the groups in this set. If a view appears multiple
     |          times then it will be counted multiple times.
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              int nViews(SireMol::MolGroupsBase {lvalue},SireMol::MolNum)
     |  
     |  residue(...)
     |      residue( (MolGroupsBase)arg1, (ResID)resid) -> Residue :
     |          Return the residue that matches the ID resid
     |          Throw: SireMol::missing_residue
     |          Throw: SireMol::duplicate_residue
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::Residue residue(SireMol::MolGroupsBase {lvalue},SireMol::ResID)
     |  
     |  residues(...)
     |      residues( (MolGroupsBase)arg1, (ResID)resid) -> object :
     |          Return all of the residues from this set that match the ID resid.
     |          The returned residues are arranged by molecule, and only one copy
     |          of each residue is returned, regardless of how many times it appears
     |          in this set.
     |          Throw: SireMol::missing_residue
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QHash<SireMol::MolNum, SireMol::Selector<SireMol::Residue> > residues(SireMol::MolGroupsBase {lvalue},SireMol::ResID)
     |  
     |  segment(...)
     |      segment( (MolGroupsBase)arg1, (SegID)segid) -> Segment :
     |          Return the segment that matches the ID segid
     |          Throw: SireMol::missing_segment
     |          Throw: SireMol::duplicate_segment
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::Segment segment(SireMol::MolGroupsBase {lvalue},SireMol::SegID)
     |  
     |  segments(...)
     |      segments( (MolGroupsBase)arg1, (SegID)segid) -> object :
     |          Return all of the segments from this set that match the ID segid.
     |          The returned segments are arranged by molecule, and only one copy
     |          of each segment is returned, regardless of how many times it appears
     |          in this set.
     |          Throw: SireMol::missing_segment
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QHash<SireMol::MolNum, SireMol::Selector<SireMol::Segment> > segments(SireMol::MolGroupsBase {lvalue},SireMol::SegID)
     |  
     |  select(...)
     |      select( (MolGroupsBase)arg1, (MGID)mgid) -> MoleculeGroup :
     |          Return the MoleculeGroup that matches the ID mgid
     |          Throw: SireMol::missing_group
     |          Throw: SireMol::duplicate_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::MoleculeGroup select(SireMol::MolGroupsBase {lvalue},SireMol::MGID)
     |      
     |      select( (MolGroupsBase)arg1, (MolID)molid) -> object :
     |          Return all of the views of the molecule with number molnum
     |          that are contained in this set of groups. Note that if the
     |          same view appears in multiple groups, then it will be returned
     |          multiple times in the returned set of views
     |          Throw: SireMol::missing_molecule
     |          
     |      
     |          C++ signature :
     |              SireMol::ViewsOfMol select(SireMol::MolGroupsBase {lvalue},SireMol::MolID)
     |      
     |      select( (MolGroupsBase)arg1, (SegID)segid) -> Segment :
     |          Return the segment from this set that matches the ID segid.
     |          This segment must be wholly contained by one of the groups
     |          in this set
     |          Throw: SireMol::missing_segment
     |          Throw: SireMol::duplicate_segment
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::Segment select(SireMol::MolGroupsBase {lvalue},SireMol::SegID)
     |      
     |      select( (MolGroupsBase)arg1, (ChainID)chainid) -> Chain :
     |          Return the chain from this set that matches the ID chainid.
     |          This chain must be wholly contained by one of the groups
     |          in this set
     |          Throw: SireMol::missing_chain
     |          Throw: SireMol::duplicate_chain
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::Chain select(SireMol::MolGroupsBase {lvalue},SireMol::ChainID)
     |      
     |      select( (MolGroupsBase)arg1, (ResID)resid) -> Residue :
     |          Return the residue from this set that matches the ID resid.
     |          This residue must be wholly contained by one of the groups
     |          in this set
     |          Throw: SireMol::missing_residue
     |          Throw: SireMol::duplicate_residue
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::Residue select(SireMol::MolGroupsBase {lvalue},SireMol::ResID)
     |      
     |      select( (MolGroupsBase)arg1, (CGID)cgid) -> CutGroup :
     |          Return the CutGroup from this set that matches the ID cgid.
     |          This CutGroup must be wholly contained by one of the groups
     |          in this set
     |          Throw: SireMol::missing_cutgroup
     |          Throw: SireMol::duplicate_cutgroup
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::CutGroup select(SireMol::MolGroupsBase {lvalue},SireMol::CGID)
     |      
     |      select( (MolGroupsBase)arg1, (AtomID)atomid) -> Atom :
     |          Return the atom from this set that matches the ID atomid.
     |          This atom must be contained in one of the groups in this set.
     |          Throw: SireMol::missing_atom
     |          Throw: SireMol::duplicate_atom
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              SireMol::Atom select(SireMol::MolGroupsBase {lvalue},SireMol::AtomID)
     |  
     |  selectAll(...)
     |      selectAll( (MolGroupsBase)arg1) -> object :
     |          Return a list of all of the molecule groups in this set
     |      
     |          C++ signature :
     |              QList<SireBase::PropPtr<SireMol::MoleculeGroup> > selectAll(SireMol::MolGroupsBase {lvalue})
     |      
     |      selectAll( (MolGroupsBase)arg1, (MGNum)mgnum) -> object :
     |          Obvious shortcut for select(const MGID&)
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              QList<SireBase::PropPtr<SireMol::MoleculeGroup> > selectAll(SireMol::MolGroupsBase {lvalue},SireMol::MGNum)
     |      
     |      selectAll( (MolGroupsBase)arg1, (MGIdx)mgidx) -> object :
     |          Obvious shortcut for select(const MGID&)
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QList<SireBase::PropPtr<SireMol::MoleculeGroup> > selectAll(SireMol::MolGroupsBase {lvalue},SireMol::MGIdx)
     |      
     |      selectAll( (MolGroupsBase)arg1, (MGName)mgname) -> object :
     |          Return all of the molecule groups that are called mgname
     |          Throw: SireMol::missing_group
     |          
     |      
     |          C++ signature :
     |              QList<SireBase::PropPtr<SireMol::MoleculeGroup> > selectAll(SireMol::MolGroupsBase {lvalue},SireMol::MGName)
     |      
     |      selectAll( (MolGroupsBase)arg1, (MGID)mgid) -> object :
     |          Return all of the molecule groups that match the ID mgid
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QList<SireBase::PropPtr<SireMol::MoleculeGroup> > selectAll(SireMol::MolGroupsBase {lvalue},SireMol::MGID)
     |      
     |      selectAll( (MolGroupsBase)arg1, (MolID)molid) -> object :
     |          Return the views of the molecule(s) that match the molecule ID
     |          molid. This returns all views of the molecule in the groups,
     |          and if a view is contained multiple times, then multiple copies
     |          of that view will be returned.
     |          Throw: SireMol::missing_molecule
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QList<SireMol::ViewsOfMol> selectAll(SireMol::MolGroupsBase {lvalue},SireMol::MolID)
     |      
     |      selectAll( (MolGroupsBase)arg1, (SegID)segid) -> object :
     |          Return all of the segments from this set that match the ID segid.
     |          The returned segments are arranged by molecule, and only one copy
     |          of each segment is returned, regardless of how many times it appears
     |          in this set.
     |          Throw: SireMol::missing_segment
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QHash<SireMol::MolNum, SireMol::Selector<SireMol::Segment> > selectAll(SireMol::MolGroupsBase {lvalue},SireMol::SegID)
     |      
     |      selectAll( (MolGroupsBase)arg1, (ChainID)chainid) -> object :
     |          Return all of the chains from this set that match the ID chainid.
     |          The returned chains are arranged by molecule, and only one copy
     |          of each chain is returned, regardless of how many times it appears
     |          in this set.
     |          Throw: SireMol::missing_chain
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QHash<SireMol::MolNum, SireMol::Selector<SireMol::Chain> > selectAll(SireMol::MolGroupsBase {lvalue},SireMol::ChainID)
     |      
     |      selectAll( (MolGroupsBase)arg1, (ResID)resid) -> object :
     |          Return all of the residues from this set that match the ID resid.
     |          The returned residues are arranged by molecule, and only one copy
     |          of each residue is returned, regardless of how many times it appears
     |          in this set.
     |          Throw: SireMol::missing_residue
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QHash<SireMol::MolNum, SireMol::Selector<SireMol::Residue> > selectAll(SireMol::MolGroupsBase {lvalue},SireMol::ResID)
     |      
     |      selectAll( (MolGroupsBase)arg1, (CGID)cgid) -> object :
     |          Return all of the CutGroups from this set that match the ID cgid.
     |          The returned CutGroups are arranged by molecule, and only one copy
     |          of each CutGroup is returned, regardless of how many times it appears
     |          in this set.
     |          Throw: SireMol::missing_cutgroup
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QHash<SireMol::MolNum, SireMol::Selector<SireMol::CutGroup> > selectAll(SireMol::MolGroupsBase {lvalue},SireMol::CGID)
     |      
     |      selectAll( (MolGroupsBase)arg1, (AtomID)atomid) -> object :
     |          Return all of the atoms from this set that match the ID atomid.
     |          The returned atoms are arranged by molecule, and only one copy
     |          of each atom is returned, regardless of how many times it appears
     |          in this set.
     |          Throw: SireMol::missing_atom
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              QHash<SireMol::MolNum, SireMol::Selector<SireMol::Atom> > selectAll(SireMol::MolGroupsBase {lvalue},SireMol::AtomID)
     |  
     |  unite(...)
     |      unite( (MolGroupsBase)arg1, (MoleculeView)molview, (MGID)mgid) -> None :
     |          Synonym for MolGroupsBase::addIfUnique
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              void unite(SireMol::MolGroupsBase {lvalue},SireMol::MoleculeView,SireMol::MGID)
     |      
     |      unite( (MolGroupsBase)arg1, (object)molviews, (MGID)mgid) -> None :
     |          Synonym for MolGroupsBase::addIfUnique
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              void unite(SireMol::MolGroupsBase {lvalue},SireMol::ViewsOfMol,SireMol::MGID)
     |      
     |      unite( (MolGroupsBase)arg1, (Molecules)molecules, (MGID)mgid) -> None :
     |          Synonym for MolGroupsBase::addIfUnique
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              void unite(SireMol::MolGroupsBase {lvalue},SireMol::Molecules,SireMol::MGID)
     |      
     |      unite( (MolGroupsBase)arg1, (MoleculeGroup)molgroup, (MGID)mgid) -> None :
     |          Synonym for MolGroupsBase::addIfUnique
     |          Throw: SireMol::missing_group
     |          Throw: SireError::invalid_index
     |          
     |      
     |          C++ signature :
     |              void unite(SireMol::MolGroupsBase {lvalue},SireMol::MoleculeGroup,SireMol::MGID)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Sire.Base._Base.Property:
     |  
     |  copy(...)
     |      copy( (Property)arg1, (Property)other) -> None :
     |      
     |          C++ signature :
     |              void copy(SireBase::Property {lvalue},SireBase::Property)
     |  
     |  equals(...)
     |      equals( (Property)arg1, (Property)other) -> bool :
     |      
     |          C++ signature :
     |              bool equals(SireBase::Property {lvalue},SireBase::Property)
     |  
     |  load(...)
     |      load( (Property)arg1, (object)ds) -> None :
     |      
     |          C++ signature :
     |              void load(SireBase::Property {lvalue},QDataStream {lvalue})
     |  
     |  save(...)
     |      save( (Property)arg1, (object)ds) -> None :
     |      
     |          C++ signature :
     |              void save(SireBase::Property {lvalue},QDataStream {lvalue})
     |  
     |  what(...)
     |      what( (Property)arg1) -> str :
     |      
     |          C++ signature :
     |              char const* what(SireBase::Property {lvalue})
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Boost.Python.instance:
     |  
     |  __new__(*args, **kwargs) from Boost.Python.class
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Boost.Python.instance:
     |  
     |  __dict__
     |  
     |  __weakref__
    


To extract individual molecules, we need to use the selection tools provided in the molecule library, `Sire.Mol`. To make things easier, we will import everything from this library.


```python
from Sire.Mol import *
```

The selection tools allow you to select molecules by number (`MolNum`), their order (index) as loaded from the file (`MolIdx`), their name (`MolName`) or by the residues that are contained in the molecule (`MolWithResID`). For example, the first molecule loaded from the file can be seen using


```python
first_molecule = system[ MolIdx(0) ]
```


```python
print(first_molecule)
```

    Molecule( 1353 version 20 : nAtoms() = 5817, nResidues() = 387 )



```python

```
