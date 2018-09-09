#refer to https://github.com/TheAlgorithms/Python
#refer to http://python.jobbole.com/82270/
#O(n^2)

#bubble_sort

def bubble_sort(s):
    
    count = len(s)

    for i in range(count):

        for j in range(count-i-1):
            
            if s[j] > s[j+1] :

                s[j],s[j+1] = s[j+1],s[j]
    return s
    
if __name__ == '__main__':

    use_input = raw_input('please input:').strip()
   
    unsorted = [int(item) for item in use_input.split(',')]
    
    print bubble_sort(unsorted)
