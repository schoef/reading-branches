#ifndef __MyClass__
#define __MyClass__

#include<vector>
#include<TMath.h>


class MyClass{
  public:
  Float_t met_pt;
  Int_t nJet;

  Float_t Jet_pt[100];

  void init(){

  met_pt  = TMath::QuietNaN();
  nJet    = -1;

  for(UInt_t i=0;i<100;i++){
    Jet_pt[i] = TMath::QuietNaN();
     }; //End for loop
  }; // End init
}; // End class declaration
#endif
