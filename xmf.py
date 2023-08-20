import sys
import xml.etree.ElementTree as ET      
                              
def main():
	if len(sys.argv) < 3:
		filename = sys.argv[1]
		print("""
██╗  ██╗███╗   ███╗███████╗
╚██╗██╔╝████╗ ████║██╔════╝
 ╚███╔╝ ██╔████╔██║█████╗  
 ██╔██╗ ██║╚██╔╝██║██╔══╝  
██╔╝ ██╗██║ ╚═╝ ██║██║     Version 1.0 - Don't mess with c3Nz!
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     Made by c3Nz (@n0c3Nz)
                           """)
		print(f"Uso: python {filename} archivo.xml nombre_atributo1 nombre_atributo2 ...")
		return
	attribute_names = sys.argv[2:]

	tree = ET.parse(filename)
	root = tree.getroot()

	elements_lists = [root.findall('.//*[@{}]'.format(attr_name)) for attr_name in attribute_names]
	
	if all(elements for elements in elements_lists):
		num_elements = len(elements_lists[0])
		for i in range(num_elements):
			values = [elements[i].get(attribute_names[j]) for j, elements in enumerate(elements_lists)]
			print(" ".join(values))
	else:
		print("No se encontraron elementos para todos los atributos proporcionados.")

if __name__ == "__main__":
	main()
