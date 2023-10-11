#include <Python.h>

/**
 *print_python_list_info - C function that prints some basic
 *info about Python lists
 *@p: pointer to PyObject list
 *Return: void
 */
void print_python_list_info(PyObject *p)
{
	int a;

	printf("[*] Size of the Python List = %d\n", Py_SIZE(p));
	printf("[*] Allocated = %d\n", ((PyListsObject *)p)->allocated);
	for (a = 0; a < Py_SIZE(p); a++)
	{
		printf("Element %d: ", a);
		ob = PyList_GetItem(p, a);
		printf("%s\n", Py_Type(ob)->tp_name);
	}
}
