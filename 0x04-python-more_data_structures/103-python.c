#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 *print_python_list -  print some basic info about Python lists
 *@p: pointer to Pyobject list
 *Return: void
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Error: object is not a Python list\n");
		return;
	}
	printf("Python list: size %zu\n", PyList_Size(p));
	printf("Elements:\n");

	for (Py_ssize_t a = 0; a < PyList_Size(p); a++)
	{
		PyObject *element = PyList_GetItem(p, a);

		printf(" %zd: ", a);
		PyObject_Print(element, stdout, 0);
		printf("\n");
	}
}

/**
 *print_python_bytes -  print some basic info about Python bytes
 *@p: pointer to PyObject list
 *Return: void
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("Error: Invalid Bytes Object\n");
		return;
	}
	printf("Python bytes: size %zu\n", PyBytes_Size(p));
	printf("First 10 bytes: ");
	for (Py_ssize_t a = 0; a < PyBytes_Size(p) && a < 10; a++)
	{
		printf("%02x ", (unsigned char)PyBytes_AsString(p)[a]);
	}
	printf("\n");
}
