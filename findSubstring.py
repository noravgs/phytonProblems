def findSubstringStart(haystack, needle):
    # Check if needle is an empty string
    if not needle:
        return 0
    
    # Find the first occurrence of needle in haystack
    position = haystack.find(needle)
    
    # If the position is -1, it means needle is not found
    return position

# Example usage:
print(findSubstringStart("sadbutsad", "sad"))  # Output: 0
print(findSubstringStart("helloworld", "123"))  # Output: -1
