#qustion:- https://www.geeksforgeeks.org/replace-all-occurrences-of-pi-with-3-14-in-a-given-string/

def replacePi(n):
    out =""
    for i in range(len(n)):
        if n[i] =="p" and n[i+1] =="i":
            out+="3.14"
            i+=1
        else:
            out +=n[i]
    return out
print(replacePi("2 * pi + 3 * pi = 5 * pi"))

            

