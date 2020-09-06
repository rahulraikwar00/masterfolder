// // // // #include <iostream>
// // // // using namespace std;

// // // // int prime(int b)
// // // // {
// // // //     int j,cnt;
// // // //     cnt=1;
// // // //      for(j=2;j<=b/2;j++)
// // // //      {
// // // //          if(b%j==0)
// // // //          cnt=0;
// // // //      }
// // // //      if(cnt==0)
// // // //      return 1;
// // // //      else
// // // //      return 0;
// // // // }
// // // // int main() 
// // // // {
// // // //  int i,j,n,cnt,a[25],c,sum=0,count=0,k=0;
// // // //  cout<<"Enter a number : "; 
// // // // cin>>n;
// // // //  for(i=2;i<=n;i++)
// // // //  {
// // // //      cnt=1;
// // // //      for(j=2;j<=n/2;j++)
// // // //      {
// // // //          if(i%j==0)
// // // //          cnt=0;
// // // //      }
// // // //      if(cnt==1)
// // // //      {
// // // //         a[k]=i;
// // // //         k++;
// // // //         }
// // // //  }
// // // //  for(i=0;i<k;i++)
// // // //  {
// // // //      sum=sum+a[i];
// // // //     c= prime(sum);
// // // //     if(c==1)
// // // //     count++;
// // // //  }
// // // //  cout<<count;
// // // //  return 0;
// // // // }
// // // // #include <iostream>

// // // // using namespace std;

// // // // class Person {
// // // // public:
// // // //     int age;

// // // //     Person(int initialAge);

// // // //     void amIOld();

// // // //     void yearPasses();
// // // // };

// // // // Person::Person(int initialAge) 
// // // // {
// // // //     // Add some more code to run some checks on initialAge
// // // //     if (initialAge > 0) age = initialAge;
// // // //     else 
// // // // 	{
// // // //         cout << "Age is not valid, setting age to 0." << endl;
// // // //         age = 0;
// // // //     }
// // // // }

// // // // void Person::amIOld() 
// // // // {
// // // //     // Do some computations in here and print out the correct statement to the console
// // // //     if (age < 13) cout << "You are young." << endl;
// // // //     else if (age < 18) cout << "You are a teenager." << endl;
// // // //     else cout << "You are old." << endl;
// // // // }

// // // // void Person::yearPasses() 
// // // // {
// // // //     // Increment the age of the person in here
// // // //     age++;
// // // // }

// // // // int main() 
// // // // {
// // // //     int t;
// // // //     int age;
// // // //     cin >> t;
// // // //     for (int i = 0; i < t; i++) 
// // // // 	{
// // // //         cin >> age;
// // // //         Person p(age);
// // // //         p.amIOld();
// // // //         for (int j = 0; j < 3; j++) 
// // // // 		{
// // // //             p.yearPasses();
// // // //         }
// // // //         p.amIOld();
// // // //         cout << '\n';
// // // //     }

// // // //     return 0;
// // // // }
// // // // #include<bits/stdc++.h>
// // // // using namespace std;

// // // // #define fastio ios_base::sync_with_stdio(0); cin.tie(0)
// // // // #define LL long long 

// // // // int main(){
// // // // fastio;
// // // // int t; cin>>t;
// // // // while(t--){
// // // // LL a[3]; cin>>a[0]>>a[1]>>a[2];
// // // // sort(a,a+3);
// // // // if(a[0]+a[1]>=a[2]){
// // // //    LL ans = a[2] + (a[0]+a[1]-a[2])/2;
// // // //    cout<<ans;
// // // //  }
// // // // else {
// // // //    LL ans = a[1] + min(a[0],a[2]-a[1]);
// // // //    cout<<ans;
// // // //  }
// // // // cout<<"\n";
// // // // }
// // // // }

// // // // #include<iostream>

// // // // using namespace std;

// // // // int bit_score(int n)	{
// // // // 	int a, b, c, largest, smallest;
// // // // 	int score;

// // // // 	a = n%10;	n/=10;
// // // // 	b = n%10;	n/=10;
// // // // 	c = n%10;	n/=10;

// // // // 	largest = (a>b)?a:b;
// // // // 	largest = (c>largest)?c:largest;
// // // // 	smallest = (a<b)?a:b;
// // // // 	smallest = (c<smallest)?c:smallest;

// // // // 	score = largest*11 + smallest*7;

// // // // 	score = score % 100;
// // // // 	return score;
// // // // }

// // // // int findPairs (int score_array[], int N)	{
// // // // 	int sig_dig[10], i, pairs = 0, msb;

// // // // 	for(i=0; i<10; i++)	{
// // // // 		sig_dig[i] = 0;
// // // // 	}

// // // // 	for(i=0; i<N; i=i+2)	{
// // // // 		msb = score_array[i] / 10;
// // // //         for(int j =i+2; j<N; j=j+2){
// // // //             if(msb == score_array[j]/10){
// // // //                 if(sig_dig[msb] < 2)	{
// // // // 	        		sig_dig[msb]++;
// // // // 		        }
// // // //             }
// // // //         }
		
// // // // 	}
    
// // // //     for(i=1; i<N; i=i+2)	{
// // // // 		msb = score_array[i] / 10;
// // // // 		for(int j =i+2; j<N; j=j+2){
// // // //             if(msb == score_array[j]/10){
// // // //                 if(sig_dig[msb] < 2)	{
// // // // 	        		sig_dig[msb]++;
// // // // 		        }
// // // //             }
// // // //         }
// // // // 	}

// // // // 	for(i=0; i<10; i++)	{
// // // // 		pairs = pairs + sig_dig[i];
// // // // 	}

// // // // 	return pairs;
// // // // }


// // // // int main()	{

// // // // 	int N, i;
// // // // 	int ip_array[501];
// // // // 	int score_array[501];
// // // // 	int pairs;
// // // // 	cin>>N;

// // // // 	for(i=0; i<N; i++)	{
// // // // 		cin>>ip_array[i];
// // // // 	}

// // // // 	for(i=0; i<N; i++)	{
// // // // 		score_array[i] = bit_score(ip_array[i]);
// // // // 	}

// // // // 	pairs = findPairs(score_array, N);
// // // // 	cout<<pairs;

// // // // 	return 0;
// // // // }

// // // // #include<bits/stdc++.h>
// // // // using namespace std;
// // // // int maxi=INT_MAX;
// // // // int maxx(int a,int b)
// // // // {
// // // // 	return (a>b)?a:b;
// // // // }
// // // // void calTime(int total,int sum,int i,vector<int> v1)
// // // // {
	
// // // // 	if(maxx(sum,total-sum)<maxi)
// // // // 	{
// // // // 		maxi=maxx(sum,total-sum);
// // // // 	}
// // // // 	if(v1[i])
// // // // 	 return;
// // // // 	calTime(total,sum+v1[i],i+1,v1);
// // // // 	calTime(total,sum,i+1,v1);
// // // // 	return;
// // // // }
// // // // int main()
// // // // {
// // // // 	int n,i=1,sum=0;
// // // // 	string s;
// // // // 	vector<int>v1;
// // // // 	getline(cin,s,'\n');
// // // // 	stringstream ss(s);
// // // // 	while(ss>>n)
// // // // 	{
// // // // 		sum+=n;
// // // // 		v1.push_back(n);
// // // // 	}
// // // // 	calTime(sum,0,0,v1);
// // // // 	cout<<maxi;
// // // // }
// // // #include<bits/stdc++.h>

// // // int main()
// // // {
// // //     int n,x,i,j;
// // //     char s[52];
// // //     scanf("%d%d",&n,&x);
// // //     scanf("%s",s);
// // //     for(j=0; j<x; j++)
// // //     {
// // //         for(i=0; i<n-1; i++)
// // //         {
// // //             if(s[i]=='B'&&s[i+1]=='G')
// // //             {
// // //                 s[i]='G';
// // //                 s[i+1]='B';
// // //                 i++;
// // //             }
// // //         }

// // //     }
// // //     printf("%s\n",s);
// // //     return 0;
// // //     int i;
// // // void insertd(){
// // //     printf("entr teh sdfsfs:\n");
// // // }
// // //     for(i=0;i<10;i++){
// // //         scanf("%d",&arrry[i]);
// // //     }
// // // }

// // // #include<iostream>
// // // using namespace std;

// // // int main()
// // // {
// // // 	int i;
// // // 	for(i = 0; i < 91; i++)
// // // 	{
// // // 		if(i%2!=0 && i%3!=0 && i%5!=0){
// // // 			cout<<i <<endl;
// // // 		}
// // // 	}
// // // 	return 0;
// // // }


// // // C++ program to print largest contiguous array sum 
// // // #include<iostream> 
// // // #include<climits> 
// // // using namespace std; 
  
// // // int maxSubArraySum(int a[], int size) 
// // // { 
// // //     int max_so_far = INT_MIN, max_ending_here = 0; 
  
// // //     for (int i = 0; i < size; i++) 
// // //     { 
// // //         max_ending_here = max_ending_here + a[i]; 
// // //         if (max_so_far < max_ending_here) 
// // //             max_so_far = max_ending_here; 
  
// // //         if (max_ending_here < 0) 
// // //             max_ending_here = 0; 
// // //     } 
// // //     return max_so_far; 
// // // } 
  
// // // /*Driver program to test maxSubArraySum*/
// // // int main() 
// // // {
// // //     int a[] = {}, q=0;
// // // 	int i =0;
// // // 	cout<<"Enter length of arry\n";
// // // 	cin>>q; 
// // // 	// get input of arry 
	
// // // 	while(q--){
// // // 		cin>>a[i];
// // // 		i++;
// // // // 	} 
// // // //     int n = sizeof(a)/sizeof(a[0]); 
// // // //     int max_sum = maxSubArraySum(a, n); 
// // // //     cout << "Maximum contiguous sum is " << max_sum; 
// // // //     return 0; 
// // // // } 
// // // // CPP program to sort a binary array 
// // // #include <iostream> 
// // // using namespace std; 

// // // void sortBinaryArray(int a[], int n) 
// // // { 
// // //     int j = -1; 
// // //     for (int i = 0; i < n; i++) { 
// // //         // if number is smaller than 1 
// // //         // then swap it with j-th number 
// // //         if (a[i] < 1) { 
// // //             j++; 
// // //             swap(a[i], a[j]); 
// // //         } 
// // //     } 
// // // } 
  
// // // // Driver code 
// // // int main() 
// // // { 
// // //     int a[] = { 1, 0, 0, 1, 0, 1, 0, 1, 1, 1}; 
// // //     int n = sizeof(a) / sizeof(a[0]); 
// // //     sortBinaryArray(a, n); 
// // //     for (int i = 0; i < n; i++) 
// // //         cout << a[i] << " "; 

// // //     return 0;
// // // // } 
// // // #include<bits/stdc++.h>
// // // #define ll long long
// // // using namespace std;
// // // int main(){
// // //     int t;
// // //     cin >> t >>"\n";
// // //     while(t--){
// // //         ll n, k;
// // //         cin >> n >>k;
// // //         ll a[n+1];
// // //         map<ll, ll>mp;
// // //         ll ans = 0, vc =0, t=1;
// // //         for(ll i =0; i<n; i++){
// // //             cin >> a[i];
// // //         }
// // //         ll coll[n + 1][n +1] ={0};
// // //         for (ll i = 0; i < n; i++){
// // //             for (ll j = 0; j < n; i++){
// // //                 coll[i][j] =0;
// // //             }
            
// // //         }
// // //        // cout << " check 1 \n";
// // //         for (ll i = 0; i < n; i++){
// // //             mp.clear();
// // //             for (ll j = i; j < n; j++)
// // //             {
// // //                 coll[i][j] = (j==0)?0:coll[i][j-1];
// // //                 if(mp.count(a[j])){
// // //                     if(mp[a[j]] ==1){
// // //                         coll[i][j]++;
// // //                     }
// // //                     coll[i][j]++;

// // //                 }
// // //                 mp[a[j]]++;
// // //             }
// // //         }
// // //        // cout <<"chek 2 \n";
// // //             ans =1e18;
// // //             ll table =100;
// // //             ll dp[101][1001] ={0};
// // //             for (int i = 0; i <= table; i++)
// // //             {
// // //                 for (ll j = 0; j <= table; j++)
// // //                 {
// // //                     dp[i][j] =0;
// // //                 }
                
// // //             }
// // //          //   cout << "check 4";
// // //             for (ll i = 0; i < n+1; i++)
// // //             {
// // //                 dp[1][i] = coll[0][i-1];
// // //             }
// // //            // cout << "check 5";
// // //             for (ll i = 2; i <= table; i++)
// // //             {
// // //                 dp[i][1] =0;
// // //             }
// // //             //cout << "check 6";
// // //             for (ll i = 2; i <=table ; i++)
// // //             {
// // //                 for (ll j = 2; i <= n; j++)
// // //                 {
// // //                     ll best = 1e18;
// // //                     for(ll p =1; p<j ;p++){
// // //                         best =min(best, dp[i-1][p]+coll[p][j-1]);
// // //                     }
// // //                     dp[i][j] = best;
// // //                 }
                
// // //             }
// // //             //cout << "check 7";
// // //             for(table = 1; table<=100; table++){
// // //                 ans = min(table * k + dp[table][n],ans);
// // //             }
// // //            // cout << "check 8";
// // //             cout << ans << endl;
// // //         }
// // //         return 0;
// // //     }

    

// // // #include<bits/stdc++.h>
// // // #define ll long long
// // // using namespace std;
// // // int main()
// // // {
// // //     int t;
// // //     cin >> t;
// // //     while (t--) {
// // //         ll n, k;
// // //         cin >> n >> k;
// // //         ll a[n + 1];
// // //         map<ll, ll> mp;
// // //         ll ans = 0, vc = 0, t = 1;
// // //         for(ll i = 0; i < n; i++) {
// // //             cin >> a[i];
// // //         }
// // //         ll col[n + 1][n + 1] = {0};
// // //         for(ll i = 0; i < n; i ++) {
// // //             for(ll j = 0; j < n; j++) {
// // //                 col[i][j] = 0;
// // //             }
// // //         }
// // //         for(ll i = 0; i < n; i++) {
// // //             mp.clear();
// // //             for(ll j = i; j < n; j++) {
// // //                 col[i][j] = (j == 0)?0:col[i][j - 1];
// // //                 if (mp.count(a[j])) {
// // //                     if (mp[a[j]] == 1) {
// // //                         col[i][j]++;
// // //                     }
// // //                     col[i][j]++;
// // //                 }
// // //                 mp[a[j]]++;
// // //             }
// // //         }
// // //         ans = 1e18;
// // //         ll table = 100;
// // //         ll dp[101][1001] = {0};
// // //         for(int i = 0; i <= table; i++) {
// // //             for(ll j = 0; j <= table; j++) {
// // //                 dp[i][j] = 0;
// // //             }
// // //         }
// // //         for(ll i = 1; i < n + 1; i++) {
// // //             dp[1][i] = col[0][i - 1];
// // //         }
// // //         for(ll i = 2; i <= table; i++) {
// // //             dp[i][1] = 0;
// // //         }
// // //         for(ll i = 2; i <= table; i++) {
// // //             for(ll j = 2; j <= n; j++) {
// // //                 ll best = 1e18;
// // //                 for(ll p = 1; p < j; p++) {
// // //                     best = min(best, dp[i - 1][p] + col[p][j - 1]);
// // //                 }
// // //                 dp[i][j] = best;
// // //             }
// // //         }
// // //         for(table = 1; table <= 100; table++) {
// // //             ans = min(table * k + dp[table][n], ans);
// // //         }
// // //         cout << ans << endl;
// // //     }
// // //     return 0;
// // // }


// // #include<bits/stdc++.h>
// // using namespace std;
// // int main()
// // {
// //     long int n,k,temp,sum=0;
// //     cin>>n;
// //     cin>>k;
// //     vector<int> v;
// //     for(int i=0;i<n;i++)
// //     {
// //          cin>>temp;
// //          sum=sum + temp;
// //          v.push_back(temp);
// //     }
// //     make_heap(v.begin(),v.end());
// //     long int maxi = 0,res = 0;
// //     for(int i=0;i<k;i++)
// //     {
// //         maxi=v.front();
// //         sum-=maxi;
// //         pop_heap(v.begin(), v.end());
// //         v.pop_back();
// //         res = maxi / 2;
// //         sum+=res;
// //         v.push_back(res);
// //         push_heap(v.begin(),v.end());
// //     }  
// //     cout<<sum;
// // }

// // #include <bits/stdc++.h>
// // using namespace std;
 
// // #define ull       unsigned long long int
// // #define ll        long long int
// // #define loop(i,s,e)     for(ll i=(s);i<(e);i++)
// // #define rloop(i,s,e)    for(ll i=(s);i>=(e);i--)
// // #define scan(any)       for(auto &i:any) cin>>i;
// // #define print(any)      for(auto i:any) cout<<i<<" "; nl;
// // #define nl              cout<<'\n'
// //  #define pi 3.141592654
// // #define hell 1000000007
// // #define io ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
// // #define fix(n) cout << fixed << setprecision(n)
// // #define input1(n) int n;cin>>n
// // #define input2(a, b) int a,b;cin>>a>>b
// // #define Max(a,b) ((a)>(b)?(a):(b))
// // #define Min(a,b) ((a)<(b)?(a):(b))
// // #define rep(i,a,b) for (__typeof((b)) i=(a);i<(b);i++)
// // #define ren(i,a,b) for(__typeof((a)) i=(a);i>=(b);i--)
// // #define mp make_pair
// // #define pb push_back
// // #define fi first
// // #define se second
// // #define vi vector<int>
// // #define pii pair<int,int>
// // #define piii pair<pair<int,int>,int>
// // #define all(v) (v).begin(), (v).end()
// // #define sz(x) (int)x.size()
// // #define set(a,n) memset(a,n,sizeof(a))
// // void calc(int i,vi &v1,int siz,int s,int &tot)
// // {
// // if(i==siz)
// // {
// // if(s==0)
// // tot++;
// // return;
// // }

// // calc(i+1,v1,siz,s+v1[i],tot);
// // calc(i+1,v1,siz,s,tot);
// // }


// // int main()
// // {
// // int n;
// // cin>>n;
// // vi v(n);
// // scan(v);
// // int m=0;

// // for(int i=0;i<n;i++)
// // {
// // if(v[i]>m)
// // m=v[i];
// // }
// // int count=0;
// // while(m)
// // {
// // count++;
// // m=m>>1;
// // }
// // vi v1(n,0);
// // for(int i=0;i<n;i++)
// // {
// // while(v[i])
// // {
// // if(v[i]&1)
// // v1[i]++;
// // v[i]=v[i]>>1;
// // }
// // }
// // int j=0;
// // for(int i=0;i<n;i++)
// // {
// // v1[j]=count-2*v1[i];
// // if(v1[j]==0)
// // continue;
// // else
// // j++;
// // }
// // int tot=0;
// // calc(0,v1,j,0,tot);
// // tot-=1;
// // tot=tot*(1+n-j)+(1<<(n-j))-1;
// //     vi bin(count,0); 
// //     int i=0;
// //     while (tot > 0) { 
  
// //         bin[i] = tot &1; 
// //         tot = tot>>1; 
// //     i++;
// //     } 
// //     for (int j = count - 1; j >= 0; j--) 
// //         cout << bin[j]; 
// // return 0;
// // }

// // #include
// // using namespace std;
// // int main(){
// // long long int n,h=-1,k,c=0,sx=0,sy=0,z=0;
// // cin>>n;
// // long long int a[n]={0},x[n]={0},y[n]={0},i,j,c0=0,c1=0,r,f=0;
// // for(i=0;i>a[i];;i++0{
// // if(a[i]>h){
// // h=a[i];
// // }}
// // i=0; //INPUT 2 7 10, n=3
// // while(1){
// // if((long long int)pow(2,i)<=h){
// // i++;
// // else{
// // break;
// // }}
// // for(j=0;j0){
// // r=a[j]%2;
// // if(r==0)
// // c0++;
// // else if(r==1)
// // c1++;
// // a[j]=a[j]/2;
// // }
// // x[j]=i -(c0+c1)+c0;
// // y[j]=c1;
// // c0=0;
// // c1=0;
// // }
// // for(j=0;j<=(long long int)pow(2,n);j++)
// // {
// // sx=0;
// // sy=0;
// // for(k=0;k0){
// // n++;
// // z=z/2;
// // }
// // for(k=0;k (c).to_string();

// // const auto loc1 = s.find('1');

// // if(loc1 != string::npos)
// // s = s.substr(loc1);
// // else
// // s='0' ;
// // if(s=="0")
// // {}
// // else{
// // cout<<s;
// // }
// // }
// // }

// #include <iostream>
// using namespace std;
// int main() {
//     int t;
//     cin>>t;
    
//     while(t--)
//     {
//         int c=0;
//         int n;
//         cin>>n;
//         int t[100];
//         for(int i=0;i<n;i++)
//         {
//             cin>>t[i];
//         }
//         if(n==1)
//         {
//             cout<<0<<endl;
//         }
//         else
//         // 
//             for(int i=0;i<n;i++)
//             {
//                 for(int j=i+1;j<n;j++)
//                 {
//                     if(i<j)
//                     {
//                     if(t[i]&t[j]==t[i])
//                     {
//                         c++;
//                     }
//                         }
//             }
//             }
//             cout<<c<<endl;
//         }
    
//     }
// }
