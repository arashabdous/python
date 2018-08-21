def _is_sorted_sample_(sample_list):
    copy_original = sample_list[:]
    sample_list.sort()
    if copy_original == sample_list:
        return True
    else:
        return False
  
x = input("input: ")
x = x.split()
print(_is_sorted_sample_(x))
