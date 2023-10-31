#!/usr/bin/python3

import sys

def compute_stats(lab_ratio,source_file: str, stats_file:str):
  data =open(source_file,'r')
  lines=data.readlines()
  lab_ratio_int=int(lab_ratio)

  
  grade_lines=[]
  for line in lines[1:]:
     if len(line)>0 and line[0] != '#' :
        grade_lines.append(line)

  grades={}
  for grade in grade_lines:
      if len(grade.strip())> 0 :
         parts=grade.split(',')
         grades[parts[0].strip()]=(lab_ratio_int/100)*int(parts[2].strip()) + ((100-lab_ratio_int)/100)*int(parts[1].strip())

  grade_values=list(grades.values())

  grade_min=100
  for grade_value in grade_values:
     if grade_value < grade_min :
        grade_min=grade_value

  grade_max=0
  for grade_value in grade_values:
     if grade_value > grade_max :
        grade_max=grade_value

  average=0
  for grade_value in grade_values:
        average=average+grade_value
  average = int(average / len(grade_values))

  tops=[]
  gradeIds=grades.keys()
  for grade_id in gradeIds :
     if grades[grade_id] == grade_max :
         tops.append(grade_id)

  grade_values.sort()
  median=0;
  number_of_students=len(grade_values)
  if number_of_students % 2 == 1 :
     median=grade_values[int(number_of_students/2)]
  else:
     median=(grade_values[int(number_of_students/2)-1]+grade_values[int(number_of_students/2)])/2

  output=open(stats_file,'w')
  output.write('Minimum Grade:'+str(grade_min)+'\n')
  output.write('Maximum Grade:'+str(grade_max)+'\n')
  output.write('Average Grade:'+str(average)+'\n')
  output.write('Top Students:'+(", ".join(tops))+'\n')
  output.write('Median Grade:'+str(median)+'\n')


  final=open(source_file+'.finals','w') 
  gradeIds=grades.keys()
  final.write('Student ID, Grade\n')
  for grade_id in gradeIds :
       final.write(grade_id+','+str(grades[grade_id])+'\n')

  final.close()
  data.close()
  output.close()


def compute_median(grades: list) -> int:
  return 0
  
def compute_min(grades: list) -> int:
  return 0
  
def compute_max(grades: list) -> int:
  return 0
  
def compute_top_students(grades: dict, grade_max) -> list:
  return []
         
def compute_average(grades: list) -> float:
  return 0
  
def read_grades(source_file: str) -> dict:
  return {}
     
def write_stats(min: int, max: int, med: int, avg: int, tops: list, stats_file:str):
    return None

def write_finals(grades: dict):
     return None

if __name__ == '__main__' :  
  compute_stats(sys.argv[1],sys.argv[2],sys.argv[3])
