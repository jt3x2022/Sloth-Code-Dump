def whereIsWaldo(matrix):
  first_value = ""
  second_value = ""
  times_of_first = 0
  times_of_second = 0
  #defines a 4 variables to find out the unique element

  for x in matrix:
      for y in x:
          if first_value == "":  
              first_value = y
              times_of_first += 1
          elif y == first_value: 
              times_of_first += 1
          elif second_value == "":  
              second_value = y
              times_of_second += 1
          elif y == second_value:  
              times_of_second += 1
          else:
            pass

  #checks all elements and updates the variables

  special = first_value if times_of_first < times_of_second else second_value
  #decides which one is the special one

  row_count = 0
  column_count = 0
  row = 0
  column = 0

  for x in matrix:
    row_count +=1
    if special in x:
      row = row_count
      for y in x:
        column_count += 1
        if special == y:
          column = column_count
  #finds the row and column of the special element

  return[row, column]


#bellow is a test (please ignore)
print(whereIsWaldo([
                    ["A", "A", "A"],
                    ["A", "A", "A"],
                    ["A", "B", "A"]
                  ]))
      