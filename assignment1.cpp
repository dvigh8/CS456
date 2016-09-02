#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

using std::string;
using std::vector;
using std::cout;
using std::cin;
using std::getline;
using std::endl;
using std::srand;
using std::rand;
using std::time;

void rem(string & s){ // removes duplicates from string

	bool isin = false;
	string a = "";

	for(int i = 0; i < s.length(); ++i){
		for(int j = 0; j < a.length(); ++j){
			if(a[j] == s[i]){
				isin = true;
			}
		}
		if(!isin){
			a += s[i];
		}
		isin = false;
	}
	s = a;
}
void get_mess(string filename, string & message){
	string line;
	message = "";
	std::ifstream in(filename);
	if(in.is_open()){
		while(getline(in,line)){
			message += line;
		}
		in.close();
	}
	else{
		cout << "file did not open";
	}
}
void write_mess(string filename, string message){

	std::ofstream out(filename);
	if(out.is_open()){

		out << message;
		out.close();
	}
	else{
		cout << "file did not open";
	}
}
void gen(vector<string> & matrix, string & alpha){

	string key = "";
	cout << "Enter your key: ";
	getline(cin,key);
	cout << "your key is " + key + "\n";
	// declaration of all symbols used in encoding any symbols added to this will automatacly be used
	alpha = "pyfgcrlaoeuidhtnsqjkxbmwvz .!?1234567890PYFGCRLAOEUIDHTNSQJKXBMWVZ`~!@#$%^&*(){}[]/=\\+|_-\",<.>;:"; 
	alpha = key + alpha;

	rem(alpha);
	matrix.empty();
	matrix.push_back(alpha);
	int len = alpha.length();
	int back = len - 1;

	//generates the matrix used to make each symbol unique	
	for(int i = 1; i < len; ++i){
		char temp = alpha[back];
		alpha.pop_back();
		alpha = temp + alpha;
		matrix.push_back(alpha);
	}
}
void use_file(string & message){

	cout << "Enter message (e) or read (r) from file? ";
	char input;
	cin >> input;
	cin.ignore(1000, '\n');
	if(input == 'e'){
		cout << "Enter your message: ";
		message = "";
		getline(cin,message);

	}
	else if(input == 'r'){
		string filename;
		cout << "File name: ";
		cin >> filename;
		get_mess(filename,message);
		cout << message << endl;
	}
}

void use_file_2(string m){
	
	cout << "See message (s) or write to file? (w) ";
	char input2;
	cin >> input2;
	if(input2 == 's'){
		cout << m << endl;

	}
	else if(input2 == 'w'){
		string filename;
		cout << "File name: ";
		cin >> filename;
		write_mess(filename,m);
	}	
}

void encrypt(){

	string alpha = "";
	vector<string> matrix;
	gen(matrix,alpha);
	
	string message;
	use_file(message);

	string e_message = "";

	srand(time(NULL));
	
	for(int i = 0; i < message.length(); ++i){

		int index = rand() % alpha.length();
		int k = 0;
		while(matrix[index][k] != message[i]){++k;}
		char one = matrix[index][0];
		char two = matrix[0][k];
		e_message += one;
		e_message += two;
	}
	
	use_file_2(e_message);

}
void decrypt(){

	string alpha = "";
	vector<string> matrix;
	gen(matrix,alpha);

	string message;
	use_file(message);

	string d_message = "";

	for(int i = 0; i < message.length(); i += 2){
		int x = 0;
		while(message[i] != matrix[x][0]){
			++x;
		}
		int k = 0;
		while(message[i+1] != matrix[0][k]){
			++k;
		}
		d_message += matrix[x][k];
	}

	use_file_2(d_message);
}
int main(){
	string input = "";
	cout << "Welcome to Assignment 1 Encryptor/Decryptor. Enter e/d to encrypt/decrypt, or q to quit: ";

	bool done = false;
	while(!done){

		getline(cin,input);
		if(input == "e"){
			encrypt();
		}
		else if(input == "d"){
			decrypt();
		}
		else if(input == "q"){
			done = true;
		}
	}
	return 0;
}