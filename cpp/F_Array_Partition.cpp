#include<bits/stdc++.h>
using namespace std;
const int INF=0x3f3f3f3f;
int mn,n,t,cnt,tim;
int a[200010],max1[200010],max2[200010];
int main()
{
 cin>>t;
 while(t--){
	 bool flag=0;
	 int n;
	 scanf("%d",&n);
	 for(int i=1;i<=n;i++){
	    scanf("%d",&a[i]);
		max1[i]=a[i];
		max2[i]=a[i];
	 }
	 max1[n+1]=max2[n+1]=0;
	 for(int i=1;i<=n;i++){
	    max1[i] = max(max1[i-1],a[i]);
	 }
	 for(int i=n;i>=1;i--){
	   max2[i] = max(max2[i+1],a[i]);
	 } 	 
     for(int i=1;i<=n-2;i++){
	   mn = INF,cnt=1;
	   for(int j=i+1;j<=n-1;j++,cnt++){
	     tim++;
		 if(tim>1e8){
		   cout<<"NO\n";
		   exit(0);
		 }
		 mn = min(mn,a[j]);
		 if(mn==max1[i]&&mn==max2[j+1]){
		   printf("YES\n");
		   printf("%d %d %d \n",i,cnt,n-i-cnt);
		   flag=1;
		   break;
		 }
		 if(mn<max1[i])break;
	   }
	   if(flag){
	     break;
	   }
	 }
	 if(!flag){
	   cout<<"NO\n";
	 }
 }
}
