def series_slices(digits,n):
  containerDigits = []
  if n > len(digits):
    raise "error"
  else:
    for index, item in enumerate(digits):
      containerDigits.append(\
      list(\
        map(int,digits[index:(index+n)]))\
      )
      
      if (index+n) >= len(digits):
        break
  return containerDigits  