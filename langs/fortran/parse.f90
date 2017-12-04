program parse
  implicit none
  character(250) :: filepath
  character(20)  :: variable_name
  integer        :: line_number
  integer, parameter :: out_unit=20

  read(*,*) filepath, variable_name, line_number
  write(0,*) filepath, " ", variable_name, " ", line_number
  !open (unit=out_unit,file="results.txt",action="write",status="replace")
  !write (out_unit,*) "file path is ", filepath
  !write (out_unit,*) "variable_name is ", variable_name
  !write (out_unit,*) "line_number is ", line_number
  !close (out_unit)
  !write(*,*) filepath, " ", variable_name, " ", line_number

end program
