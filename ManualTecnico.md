### Clase `Error`

La clase `Error` es una representación de un error léxico que puede ocurrir durante el análisis de un código fuente. Esta clase almacena información sobre el carácter (lexema) que causó el error, así como la fila y columna en las que se encuentra dicho carácter en el código fuente.

#### Constructor `__init__(self, character, line, column)`

El constructor de la clase `Error` toma tres parámetros:
- `character`: El carácter (lexema) que causó el error.
- `line`: El número de línea en el que se encuentra el carácter en el código fuente.
- `column`: La columna en la que se encuentra el carácter en la línea del código fuente.

Estos parámetros se utilizan para inicializar las propiedades de la instancia de la clase.

#### Método `to_json(self)`

El método `to_json` convierte la instancia de la clase `Error` en un diccionario JSON que contiene información sobre el error. El diccionario tiene la siguiente estructura:

```python
{
    "descripcion": {
        "Lexema": self.character,
        "Tipo": "error lexico",
        "fila": self.line,
        "columna": self.column
    }
}
```
### Función `stringt(entrada, i)`

La función `stringt` es una función en Python que se utiliza para analizar cadenas delimitadas por comillas (`"`). Su objetivo es identificar y extraer el contenido de una cadena dentro de una secuencia de caracteres `entrada`. La función toma dos parámetros:

- `entrada`: Es una cadena de caracteres (por ejemplo, un código fuente) en la que se busca una cadena delimitada por comillas.
- `i`: Es un índice que indica la posición actual en la cadena `entrada` desde la cual comenzará la búsqueda de la cadena delimitada por comillas.

#### Funcionamiento

La función `stringt` recorre la cadena `entrada` desde la posición indicada por el índice `i`. A medida que itera a través de los caracteres de la cadena, acumula los caracteres en la variable `token` hasta que encuentra una comilla (`"`).

- Cuando se encuentra la comilla de cierre (`"`), la función crea una lista que contiene dos elementos:
  1. El contenido de la cadena delimitada por comillas (almacenado en `token`).
  2. El índice `i` que indica la posición de la comilla de cierre en la cadena `entrada`.

- Luego, la función devuelve esta lista como resultado.

- Si no se encuentra la comilla de cierre, la función emite un mensaje de error que indica que la cadena no se ha cerrado correctamente y muestra el contenido acumulado en `token`.



### Función `obtener_instruccion`

La función `obtener_instruccion` es una función en Python que se utiliza para analizar una lista de tokens y construir una instrucción o comando en función de los tokens disponibles. Los tokens representan elementos en un lenguaje de programación o de marcado específico. Esta función procesa los tokens de acuerdo con ciertas reglas y retorna una instrucción resultante.

#### Parámetros

- `tokens`: Una lista de tokens que se procesan para construir la instrucción.

#### Variables Locales

- `operacion`: Almacena la operación que se realizará, si se encuentra en los tokens.
- `value1`: Almacena el primer valor que se utilizará en la instrucción, si se encuentra en los tokens.
- `value2`: Almacena el segundo valor que se utilizará en la instrucción, si se encuentra en los tokens.
- `config`: Un diccionario que almacena configuraciones como texto, fondo, fuente y forma, si se encuentran en los tokens.

#### Funcionamiento

La función `obtener_instruccion` recorre la lista de tokens usando un bucle `while` y procesa cada token en función de su tipo. Aquí están las acciones que realiza:

- Si un token es de tipo "operacion", se extrae el operador y se almacena en la variable `operacion`.
- Si un token es de tipo "valor1", se extrae el valor y se almacena en la variable `value1`. Si el valor es un "[" (indicando una instrucción anidada), se llama recursivamente a la función `obtener_instruccion` para obtener la instrucción anidada.
- Si un token es de tipo "valor2", se extrae el valor y se almacena en la variable `value2`. Si el valor es un "[" (indicando una instrucción anidada), se llama recursivamente a la función `obtener_instruccion` para obtener la instrucción anidada.
- Si un token es uno de los tipos ["texto", "fondo", "fuente", "forma"], se extrae el valor correspondiente y se almacena en el diccionario `config`.

Luego, la función verifica si se han recopilado suficientes datos (`operacion`, `value1`, y `value2`) para construir una instrucción. Si es así, se llama a una función externa (`operacionAritmetica` o `operacionTrigonometrica`) para construir y ejecutar la instrucción.

La función continúa procesando tokens hasta que no queden más tokens en la lista `tokens`, momento en el que retorna `None`.

En resumen, la función `obtener_instruccion` analiza tokens en función de su tipo y los utiliza para construir una instrucción o comando. Puede manejar operaciones aritméticas, operaciones trigonométricas y configuraciones de estilo, y llama a funciones externas para ejecutar las operaciones.

### Función `obtener_instruccion`

La función `obtener_instruccion` es una función en Python que se utiliza para analizar una lista de tokens y construir una instrucción o comando en función de los tokens disponibles. Los tokens representan elementos en un lenguaje de programación o de marcado específico. Esta función procesa los tokens de acuerdo con ciertas reglas y retorna una instrucción resultante.

#### Parámetros

- `tokens`: Una lista de tokens que se procesan para construir la instrucción.

#### Variables Locales

- `operacion`: Almacena la operación que se realizará, si se encuentra en los tokens.
- `value1`: Almacena el primer valor que se utilizará en la instrucción, si se encuentra en los tokens.
- `value2`: Almacena el segundo valor que se utilizará en la instrucción, si se encuentra en los tokens.
- `config`: Un diccionario que almacena configuraciones como texto, fondo, fuente y forma, si se encuentran en los tokens.

#### Funcionamiento

La función `obtener_instruccion` recorre la lista de tokens usando un bucle `while` y procesa cada token en función de su tipo. Aquí están las acciones que realiza:

- Si un token es de tipo "operacion", se extrae el operador y se almacena en la variable `operacion`.
- Si un token es de tipo "valor1", se extrae el valor y se almacena en la variable `value1`. Si el valor es un "[" (indicando una instrucción anidada), se llama recursivamente a la función `obtener_instruccion` para obtener la instrucción anidada.
- Si un token es de tipo "valor2", se extrae el valor y se almacena en la variable `value2`. Si el valor es un "[" (indicando una instrucción anidada), se llama recursivamente a la función `obtener_instruccion` para obtener la instrucción anidada.
- Si un token es uno de los tipos ["texto", "fondo", "fuente", "forma"], se extrae el valor correspondiente y se almacena en el diccionario `config`.

Luego, la función verifica si se han recopilado suficientes datos (`operacion`, `value1`, y `value2`) para construir una instrucción. Si es así, se llama a una función externa (`operacionAritmetica` o `operacionTrigonometrica`) para construir y ejecutar la instrucción.

La función continúa procesando tokens hasta que no queden más tokens en la lista `tokens`, momento en el que retorna `None`.

En resumen, la función `obtener_instruccion` analiza tokens en función de su tipo y los utiliza para construir una instrucción o comando. Puede manejar operaciones aritméticas, operaciones trigonométricas y configuraciones de estilo, y llama a funciones externas para ejecutar las operaciones.

### Clase `Diagrama`

La clase `Diagrama` es una clase en Python que se utiliza para crear y manipular diagramas utilizando la biblioteca Graphviz. Esta clase facilita la construcción y representación gráfica de grafos y diagramas.

#### Constructor `__init__(self)`

El constructor de la clase `Diagrama` se encarga de inicializar una instancia del diagrama. Realiza las siguientes acciones:

- Genera una marca de tiempo (`timestr`) para asegurarse de que los nombres de los diagramas sean únicos en cada ejecución del programa.
- Crea un objeto `dot` de Graphviz llamado `Digraph` y establece un comentario que incluye la marca de tiempo para identificar el diagrama.

#### Método `aggconfiguracion(self, confg)`

Este método se utiliza para agregar configuraciones visuales a los nodos del diagrama. Toma un diccionario `confg` como parámetro, que contiene información sobre el estilo visual de los nodos, como el color de fondo, el color de fuente y la forma. Luego, aplica estas configuraciones a los nodos del diagrama.

#### Método `agregar(self, valor)`

El método `agregar` se utiliza para agregar un nuevo nodo al diagrama. Toma un valor como parámetro que se mostrará en el nodo. Cada nodo se nombra de manera única (por ejemplo, "nodo0", "nodo1", etc.) y se agrega al diagrama.

#### Método `agregar_arista(self, nodo1: str, nodo2: str)`

Este método se utiliza para agregar una arista entre dos nodos del diagrama. Toma dos nombres de nodos como parámetros, `nodo1` y `nodo2`, y crea una arista que conecta estos dos nodos en el diagrama.

#### Método `generarGrafica(self)`

El método `generarGrafica` se utiliza para generar y guardar la representación gráfica del diagrama en formato DOT y renderizarla como un archivo de imagen (por ejemplo, en formato PDF) para su visualización. El método guarda tanto el archivo DOT como el archivo de imagen en una ubicación específica.

#### Método `obtener_ultimo_nodo(self)`

Este método devuelve el nombre del último nodo agregado al diagrama, que se genera de manera única para cada nodo.

### Clase `Expresion` y Método Abstracto `interpretar`

El código proporcionado define una clase abstracta llamada `Expresion` que hereda de la clase `ABC` (Abstract Base Class) de Python. Dentro de la clase `Expresion`, se define un método abstracto llamado `interpretar`.

#### Clase Abstracta `Expresion`

- La clase `Expresion` es una clase abstracta, lo que significa que no se puede crear una instancia directa de esta clase. En su lugar, se espera que otras clases que hereden de `Expresion` proporcionen una implementación concreta del método abstracto `interpretar`.

#### Método Abstracto `interpretar`

- El método `interpretar` se define como abstracto mediante el decorador `@abstractmethod`. Un método abstracto es un método que se declara en una clase base pero no se implementa en esa clase. En su lugar, se espera que las clases derivadas proporcionen su propia implementación.

- El método `interpretar` no tiene una implementación concreta en la clase `Expresion`, ya que se espera que las clases derivadas (subclases) de `Expresion` proporcionen su propia lógica de interpretación.

- La presencia de este método en la clase base `Expresion` define una interfaz que las clases derivadas deben seguir; es decir, deben implementar el método `interpretar` de acuerdo con sus necesidades específicas.

### Clase `operacionTrigonometrica`

La clase `operacionTrigonometrica` es una subclase de la clase abstracta `Expresion`, lo que significa que hereda de `Expresion` y, por lo tanto, debe proporcionar una implementación del método abstracto `interpretar`. Esta clase se utiliza para representar operaciones trigonométricas, como seno, coseno y tangente, en una expresión.

#### Constructor `__init__`

- El constructor `__init__` se utiliza para inicializar una instancia de la clase `operacionTrigonometrica`. Toma los siguientes parámetros:
  - `tipo`: El tipo de operación trigonométrica, como "seno", "coseno" o "tangente".
  - `valor`: El valor (expresión o número) al que se aplicará la operación trigonométrica.
  - `fila` y `columna`: Las coordenadas de fila y columna en el código fuente donde se encuentra esta operación.

- Los valores pasados a través de los parámetros se almacenan en las propiedades correspondientes de la instancia.

#### Método `interpretar`

- El método `interpretar` es una implementación concreta del método abstracto `interpretar` definido en la clase base `Expresion`. Este método realiza la interpretación de la operación trigonométrica y devuelve el resultado.

- En la implementación, se evalúa si el valor pasado a través de `self.valor` es una instancia de la clase `Expresion` (posiblemente una expresión anidada). Si es así, se llama al método `interpretar` del valor para obtener su resultado y se almacena en la variable `valor`.

- Luego, se crea un nodo en el diagrama que representa el valor de la operación actual utilizando el método `agregar` de la instancia de `Diagrama`. El nodo se nombra con el valor y se almacena en la variable `nodo`.

- Se realiza la operación trigonométrica (seno, coseno o tangente) en función del tipo de operación (`self.tipo`) y el valor obtenido anteriormente.

- Se agrega un nodo adicional al diagrama para representar el resultado de la operación trigonométrica, incluyendo el tipo de operación y el resultado redondeado. Se crea una arista que conecta este nodo con el nodo anterior.

- Finalmente, se devuelve el resultado de la operación trigonométrica redondeado a tres decimales.

### Clase `operacionAritmetica`

La clase `operacionAritmetica` es una subclase de la clase abstracta `Expresion`. Esta clase se utiliza para representar operaciones aritméticas, como suma, resta, multiplicación, división, etc., en una expresión.

#### Constructor `__init__`

- El constructor `__init__` se utiliza para inicializar una instancia de la clase `operacionAritmetica`. Toma los siguientes parámetros:
  - `tipo`: El tipo de operación aritmética, como "suma", "resta", "multiplicación", etc.
  - `v1` y `v2`: Los dos valores (expresiones o números) sobre los cuales se realizará la operación.
  - `linea` y `columna`: Las coordenadas de fila y columna en el código fuente donde se encuentra esta operación.

- Los valores pasados a través de los parámetros se almacenan en las propiedades correspondientes de la instancia.

#### Método `interpretar`

- El método `interpretar` es una implementación concreta del método abstracto `interpretar` definido en la clase base `Expresion`. Este método realiza la interpretación de la operación aritmética y devuelve el resultado.

- En la implementación, se evalúa si los valores `self.v1` y `self.v2` son instancias de la clase `Expresion` (posiblemente expresiones anidadas). Si son instancias de `Expresion`, se llama al método `interpretar` de cada valor para obtener sus resultados respectivos y se almacenan en las variables `v1` y `v2`.

- Se crean dos nodos en el diagrama que representan los valores de `v1` y `v2` utilizando el método `agregar` de la instancia de `Diagrama`. Estos nodos se nombran con los valores y se almacenan en las variables `nodo1` y `nodo2`.

- Se realiza la operación aritmética en función del tipo de operación (`self.tipo`) y los valores `v1` y `v2`.

- Se agrega un nodo adicional al diagrama para representar el resultado de la operación aritmética, incluyendo el tipo de operación y el resultado redondeado. Se crean aristas que conectan este nodo con los nodos de los valores `v1` y `v2` en el diagrama.

- Finalmente, se devuelve el resultado de la operación aritmética redondeado a dos decimales.

#### Método `__str__`

- El método `__str__` se utiliza para obtener una representación en forma de cadena de la instancia de la clase `operacionAritmetica`. Esta representación incluye información sobre el tipo de operación y los valores `v1` y `v2`.




