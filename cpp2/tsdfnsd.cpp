
#include<bits/stdc++.h>
using namespace std;
int cases()
{
    long int num, x ,i = 0, k , p , r, j, z;
    cin >>num >> x;

    long  int arr[num+1];

    for (long long int i = 0; i <num; i++)
    {
        cin >> arr[i];
    }

    for ( k = x; k > 0 && i <num - 1; k--)
    {
        bool flag = 0;
        p = log(arr[i]) / log(2);
        cout<<"p: "<<p<< endl;
        r = 1 << p;
        arr[i] = arr[i] ^ r;

        for (j = i + 1; j <num; j++)
        {
            if ((arr[j] ^ r) < arr[j])
            {
                arr[j] = arr[j] ^ r;
                flag = 1;
                break;
            }
        }

        if (flag == 0)
        {
            arr[num - 1] = arr[num - 1] ^ r;
        }

        while (arr[i] <= 0)
        {
            i++;
        }

        z = k + 1;

        if (z > 0)
        {
            if ((num < 3) && (z % 2 != 0) && z > 0)
            {
                arr[num - 1] = arr[num - 1] ^ 1;
                arr[num - 2] = arr[num - 2] ^ 1;
            }
        }
    }

    for (i = 0; i <num; i++)
    {
        cout << arr[i] << " ";
    }

    cout << endl;
    return 0 ;

}

int main()
{
    int t;
    cin>>t;
    for(int i=1 ; i<=t ;i++)
    {
        cases();
    }
}

// #include <bits/stdc++.h>
using namespace std;

int main()
{
	// your code goes here
	int t;
	cin >> t;
	while (t--)
	{
		long long int n, x;
		cin >> n >> x;

		long long int a[n];
		for (long long int i = 0; i < n; i++)
			cin >> a[i];

		long long int i = 0, z, k, p, r, j;
		for (k = x; k > 0, i < n - 1; k--)
		{
			int flag = 0;
			p = log(a[i]) / log(2);
			r = 1 << p;
			a[i] = a[i] ^ r;

			for (j = i + 1; j < n; j++)
			{
				if (a[j] ^ r < a[j])
				{
					a[j] = a[j] ^ r;
					flag = 1;
					break;
				}
			}
			if (flag == 0)
			{
				a[n - 1] = a[n - 1] ^ r;
			}

			while (a[i] <= 0)
				i++;
			z = k + 1;
		}
		if (z > 0)
		{
			if (n < 3 && z % 2 == 0)
			{
				a[n - 1] = a[n - 1] ^ 1;
				a[n - 2] = a[n - 2] ^ 1;
			}
		}
		for (long long int i = 0; i < n; i++)
			cout << a[i] << " ";
		cout << endl;
	}
	return 0;
}