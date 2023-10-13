#include <python.h>
#include <stdio.h>

/**
 *print_python_list -  print some basic info about Python lists
 *@p: pointer to Pyobject list
 *Return: void
 */
void print_python_list(PyObject *p)
{
	long int size, a;
	PyListObject *list;
	PyObject *ob;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated  = %ld\n", list->allocated);

	for (a = 0; a < size; a++)
	{
		ob = ((PyListObject *)p)->ob_item[a];
		printf("Element %ld: %s\n", a, ((ob)->ob_type)->tp_name);
		if (PyBytes_Check(ob))
			print_python_bytes(ob);
	}
}

/**
 *print_python_bytes -  print some basic info about Python bytes
 *@p: pointer to PyObject list
 *Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int a, max, size;

	printf("[.]bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [Error] Invalid Bytes Objects\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	prinf(" size: %ld\n", size);
	printf(" trying string: %s\n", str);

	if (size >= 10)
		max = 10;
	else
		max = size + 1;

	printf(" first 10 bytes:", max);

	for (a = 0; a < max; a++)
		if (str[a] >= 0)
			printf("%02x", str[a]);
		else
			printf("%02x", 256 + str[a]);
	printf("\n");
}
