#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	PyObject *str, *repr;

	(void)repr;
	printf("[.] string object info\n");

	if (strcmp(p->ob_type_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");

	repr = Pyobject_Repr(p);
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	repr = Pyobject_Repr(p);
	str = PyUnicode_AsEncodeString(p, "utf-8", "~E~");
	printf("  length:%d\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(str));
}

