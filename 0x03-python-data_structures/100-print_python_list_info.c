#include <python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, assign, c;
	PyObject *obj;

	size = Py_SIZE(d);
	assign = ((PyListObject *)d)->allocated;

	printf("[*] The size of Python List is: %d\n", size);
	printf("[*] Assigned = %d\n", assign);

	for (c = 0; c < size; c++)
	{
		printf("Element %d: ", c);

		obj = PyList_GetItem(d, c);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
