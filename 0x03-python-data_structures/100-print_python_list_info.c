#include <Python.h>

/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: PyObject representing a Python list.
 */
void print_python_list_info(PyObject *p)
{
	/* Vérifier si l'entrée est une liste */
	if (!PyList_Check(p))
	{
		printf("[!] Input is not a list\n");
		return;
	}

	/* Obtenir la taille et la mémoire allouée */
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	/* Imprimer les informations */
	printf("[*] Taille de la liste Python = %zd\n", size);
	printf("[*] Alloué = %zd\n", allocated);

	/* Itérer sur les éléments et imprimer leurs types */
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

