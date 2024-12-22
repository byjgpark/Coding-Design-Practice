from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a regular dictionary to store lists of anagrams
        anagrams_dict = {}
        print("Initial anagrams_dict:", anagrams_dict)  # Debug: Initial state of the dictionary
        
        # Iterate through each string in the input list
        for original_string in strs:
            print("\nProcessing string:", original_string)  # Debug: Current string being processed
            
            
            # Sort the characters of the string to generate the key
            sorted_string = ''.join(sorted(original_string))
            print("Sorted string:", sorted_string)  # Debug: Key for grouping
            
            # Check if the sorted string is already a key in the dictionary
            if sorted_string not in anagrams_dict:
                print(f"Key '{sorted_string}' not found in anagrams_dict. Initializing new list.")  # Debug
                anagrams_dict[sorted_string] = []
            
            # Append the original string to the corresponding list
            print(f"Appending '{original_string}' to anagrams_dict['{sorted_string}']")  # Debug
            anagrams_dict[sorted_string].append(original_string)
            print("Current anagrams_dict:", anagrams_dict)  # Debug: State after appending
        
        # Convert the dictionary values to a list and return the result
        grouped_anagrams = list(anagrams_dict.values())
        print("\nFinal grouped anagrams:", grouped_anagrams)  # Debug: Final output
        return grouped_anagrams

if __name__ == "__main__":
    sol = Solution()
    print("Input:", ["eat", "tea", "tan", "ate", "nat", "bat"])  # Debug: Input list
    result = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print("Output:", result)  # Debug: Final output
