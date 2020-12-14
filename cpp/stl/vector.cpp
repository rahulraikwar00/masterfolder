#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int main(){
	int a;

	vector<int> v; //define a vector with all elemets of zero

	v.push_back(10); // push a number at the end 
	v.push_back(20); // push a number at the end 
	v.push_back(12); // push a number at the end 
	v.push_back(23); // push a number at the end 
	v.push_back(35); // push a number at the end 
	// v.push_back(9); // push a number at the end 
	// v.push_back(12); // push a number at the end 
	vector<int>::iterator it = v.begin();


	cout<< "BEFOUR"<<endl;	
	for(auto it: v){
		cout << it<< "  ";
	}

	// erase element from vector
	v.erase(v.begin());

	//erase a range of elements 

	v.erase(v.begin()+2, v.begin()+4);
	cout<<endl<< " AFTER "<< endl;
	for(auto it: v){
		cout << it<< "  ";
	}


	vector<int> v2(2,100); // {100, 100}
	
	vector<int>::iterator it2 = v.begin();
	v.insert(v.begin() , 200);

	for( auto it2 : v2){
		cout << it << " ";
	}



	// insert fucntion


	cout  <<" "<< endl;
//	cout << "hello ji";
	return 0;
	
}