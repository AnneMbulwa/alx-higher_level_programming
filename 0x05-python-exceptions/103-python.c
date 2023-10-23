#include <Python.h>
#include <stdio.h>
#define PY_SSIZE_T_MAX ((Py_ssize_t)(((size_t)-1)>>1))

void print_python_list(PyObject *p)
{
    Py_ssize_t a, size;
    PyObject *item;
    size = PyList_GET_SIZE(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (a = 0; a < size; a++)
    {
        item = PyList_GET_ITEM(p, a);
        printf("Element %ld: %s\n", a, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t a, size;
    char *str;
    size = ((PyVarObject *)p)->ob_size;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

    if (size > 10)
        size = 10;

    str = ((PyBytesObject *)p)->ob_sval;
    printf("  first %ld bytes: ", size);
    for (a = 0; a < size; a++)
    {
        printf("%02hhx", str[a]);
        if (a < size - 1)
            printf(" ");
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    double value;
    value = ((PyFloatObject *)p)->ob_fval;
    printf("[.] float object info\n");
    printf("  value: %f\n", value);
}
