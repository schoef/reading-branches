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

# scalar
chain.SetBranchAddress( "met_pt", ROOT.AddressOf(myClass, "met_pt")) 
chain.SetBranchAddress( "nJet",   ROOT.AddressOf(myClass, "nJet")) 
# vector
chain.SetBranchAddress( "Jet_pt", ROOT.AddressOf(myClass, "Jet_pt")) 

# some test output
for i in range(10):
    chain.GetEntry(i)
    print "Event",i,"met_pt", round(myClass.met_pt,2), "Jet_pts: ", [round(myClass.Jet_pt[k],2) for k in range(myClass.nJet)]
