import ROOT

# Chain
chain = ROOT.TChain("Events")
chain.Add("file_0.root")

chain.SetBranchStatus("*",0)
chain.SetBranchStatus("met_pt",1)
chain.SetBranchStatus("nJet",1)
chain.SetBranchStatus("Jet_pt",1)

# make object
ROOT.gROOT.ProcessLine('.L MyClass.C' )
myClass = ROOT.MyClass()

myClass.init()

if ROOT.gROOT.GetVersion()<'6.22':
    # scalar
    chain.SetBranchAddress( "met_pt", ROOT.AddressOf(myClass, "met_pt")) 
    chain.SetBranchAddress( "nJet",   ROOT.AddressOf(myClass, "nJet")) 
    # vector
    chain.SetBranchAddress( "Jet_pt", ROOT.AddressOf(myClass, "Jet_pt")) 
else:
    chain.SetBranchAddress( "met_pt", ROOT.addressof(myClass, "met_pt"))
#    --produces this error: Traceback (most recent call last):
#                             File "test.py", line 25, in <module>
#                               chain.SetBranchAddress( "met_pt", ROOT.addressof(myClass, "met_pt"))
#                             File "/cvmfs/cms.cern.ch/slc7_amd64_gcc900/lcg/root/6.22.06/lib/ROOT/pythonization/_ttree.py", line 34, in _SetBranchAddress
#                               res = self._OriginalSetBranchAddress(*args)
#                           TypeError: Template method resolution failed:
#                             none of the 3 overloaded methods succeeded. Full details:
#                             int TChain::SetBranchAddress(const char* bname, void* add, TBranch** ptr = 0) =>
#                               TypeError: could not convert argument 2
#                             int TChain::SetBranchAddress(const char* bname, void* add, TBranch** ptr, TClass* realClass, EDataType datatype, bool isptr) =>
#                               TypeError: takes at least 6 arguments (2 given)
#                             int TChain::SetBranchAddress(const char* bname, void* add, TClass* realClass, EDataType datatype, bool isptr) =>
#                               TypeError: takes at least 5 arguments (2 given)
#                             Failed to instantiate "SetBranchAddress(std::string,long)"


    chain.SetBranchAddress( "nJet",   ROOT.addressof(myClass, "nJet"))
    # vector
    chain.SetBranchAddress( "Jet_pt", ROOT.addressof(myClass, "Jet_pt")) 
    
    #chain.SetBranchAddress( "Jet_pt", (ROOT.AddressOf(myClass, "Jet_pt"))) 
    # --> TypeError: AddressOf() takes exactly 2 arguments (3 given) 

    #import ctypes
    #chain.SetBranchAddress( "met_pt", ctypes.c_void_p(ROOT.addressof(myClass, "met_pt"))) 
    # -> does not seem to work

# some test output
for i in range(10):
    chain.GetEntry(i)
    print "Event",i,"met_pt", round(myClass.met_pt,2), "Jet_pts: ", [round(myClass.Jet_pt[k],2) for k in range(myClass.nJet)]
