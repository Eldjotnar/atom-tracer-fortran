program parse
  implicit none
  character(250) :: filepath
  character(20)  :: variable_name
  integer        :: line_number

  read(*,*) filepath, variable_name, line_number
  write(0,*) call execute_command_line("pwd")
  !call execute_command_line("python langs/fortran/fortran_parse.py filePath variable_name line_number")
end program
