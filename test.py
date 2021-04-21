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
    from cppyy.ll import cast
    chain.SetBranchAddress( "met_pt", cast['void*'](ROOT.addressof(myClass, "met_pt"))) 
    chain.SetBranchAddress( "nJet",   cast['void*'](ROOT.addressof(myClass, "nJet")))
    # vector
    chain.SetBranchAddress( "Jet_pt", cast['void*'](ROOT.addressof(myClass, "Jet_pt"))) 

    #chain.SetBranchAddress( "Jet_pt", ROOT.AddressOf(myClass, "Jet_pt"))
    # --> TypeError: AddressOf() takes exactly 2 arguments (3 given) 

    #import ctypes
    #chain.SetBranchAddress( "met_pt", ctypes.c_void_p(ROOT.addressof(myClass, "met_pt"))) 
    # -> does not seem to work

# some test output
for i in range(10):
    chain.GetEntry(i)
    print "Event",i,"met_pt", round(myClass.met_pt,2), "Jet_pts: ", [round(myClass.Jet_pt[k],2) for k in range(myClass.nJet)]
