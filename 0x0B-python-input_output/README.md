0x0B. Python - Input/Output
File - is a contiguous set of bytes.
Data in a computer system is always stored into files. Files can take different forms depending on the user requirements like data files, text files, program executable files etc.

Every file contains three main parts:

1. Header: This contains information about the file i.e. file name, file type, file size etc.
2. Data: This is the actual information/content stored in the file.
3. End of file: This is a special character that marks the end of the file.

Python Open File
we can open files using the built-in open () function.
The open () thats the follwing parametrs:
    .filename
    .access mode
        Mode	Function
        r	    Open a file for reading. This is the default mode.
        w	    Open a file for writing. 
                If the file already exists, overwrite its cotents.
                Create a new file if the file does not exist.
        a	    Open a file for appending. 
                Preserve the file’s contents, add new data to the end of the file.
        r+	    Open a file for reading and writing.
        w+	    Allows to write as well as read from the file.
        a+	    Allows appending as well as reading from the file.
    .encoding = "utf-8"(mode defacto)

Methids to access file objects
a). f.read(size) - This read size number of bytes from the file. If size is not passed, the entire file is read.
    example;
        with open("filename", encoding = "utf-8"):
            read_data = f.read(5)
    Note:
        if the size is ommitted, the system reads and returns the entire content of the file.

b). f.readline(size = -1) - This reads size number of bytes from the line. If we pass no argument value, it reads the entire line.

c). f.readlines() - This function reads all the lines from a file and returns a list of the lines, separating them from one another with commas.

d). f.write(string) - This function takes a string as an argument and writes it into the file. This function returns the number of characters written into the file.

e). f.tell() - returns the current postion of the file

f). f.seek(offset, whence) - The seek method lets you control the position of the file pointer. This method takes two parameters:

a. offset – The number of positions(bytes) to move forward.

b. whence – This is optional. This denotes the position from where you want to move forward. It can take three values:

0: move forward from the start of the file.
1: seek relative to the current position.
2: move backwards from the end of the file


summary
Method	    What it does
close()	            Closes the file.
flush()	            Flushes the internal buffer.
fileno()	        Returns the file descriptor of the file.
next()	            Returns the next line from the file.
read(size)	        Reads size number of bytes from the file. Reads the entire file                     if you don’t pass any argument value.
readline(size)	    Reads one line from a file.
readlines()	        Reads the entire file and returns a list of the lines.
seek(offset, whence)	Lets us control the position of the file pointer.
tell()	            Returns the current position of the file pointer.
truncate(size)	    It truncates the file to the specified size.
writable()	        Returns True if we can write into the file.
