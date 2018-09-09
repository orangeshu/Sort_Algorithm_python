#refer to https://github.com/TheAlgorithms/Python
#refer to http://python.jobbole.com/82270/
#O(n^2)

def insertion(s):

    count = len(s)

    for i in range(1,count):

        j = i-1

        while j >=0:

            if s[j+1] < s[j]:

                s[j+1],s[j] = s[j],s[j+1]

            j-=1

    return s

if __name__ == '__main__':

    user_input = raw_input('please input:').strip()

    unsorted = [ int(item) for item in user_input.split(',')]

    print insertion(unsorted)

            
