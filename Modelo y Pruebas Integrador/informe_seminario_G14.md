Informe Final
Claudia Banchoff - Viviana Harari
{cbanchoff,vharari}@info.unlp.edu.ar

---

## Índice
1. [Introducción](#introducción)
2. [Marco teórico](#marco-teórico)
3. [Problemas y soluciones surgidas durante el desarrollo](#problemas-y-soluciones-surgidas-durante-el-desarrollo)
4. [Consideraciones Éticas sobre el Desarrollo](#consideraciones-éticas-sobre-el-desarrollo)
5. [Conclusiones y Trabajos Futuros](#conclusiones-y-trabajos-futuros)
6. [Guía de Usuario](#guía-de-usuario)
7. [Guía para el Desarrollador](#guía-para-desarrolladores)

---

# Introducción
En este informe, realizaremos un desarrollo abarcativo acerca del proyecto en general.
Haremos una muestra de temas pilares que no tendrán un enfoque a nivel de código, sino que con una mirada a nivel de estructura.
Por otra parte, se verán plasmados, de manera resumida, los diferentes procesos del trabajo, como los problemas que se presentaron, las consideraciones que se tuvieron para el desempeño general y las conclusiones finales respecto al mismo y la materia.
Por último se encontrará la guía de usuario, que permitirá  manipular el juego y el manejo de usuarios de manera correcta; y la guía para programador que indica cómo se relacionan las partes a nivel código, el funcionamiento de cada una y así poder modificarlas. 

---

# Marco Teórico
Para la realización del proyecto, se utilizaron múltiples librerías para conseguir un mejor producto, y para facilitar el desarrollo del mismo.
Como librería principal para manejar la interfaz del videojuego, se utilizó PySimpleGUI, la cual permite la creación de las diferentes ventanas donde se ejecuta el juego.
Para trabajar con los diferentes conjuntos de datos, se escogió la librería Pandas, la cual simplifica el manejo de datasets,y permitió, no solamente generar todas las estadisticas y graficos que genera el juego a partir de las partidas jugadas, sino que también se utilizo para realizar el funcionamiento principal del juego (elegir las opciones del conjunto de datos, y elegir la respuesta correcta).

Para la realización de una ambientación musical, se utilizó la librería PyGame, especialmente la funcionalidad del mixer, se verá su uso únicamente en la clase Settings.

---

# Problemas y Soluciones surgidas durante el Desarrollo
Limitaciones de PySimpleGUI: no hay diseño responsivo (por las enormes limitaciones de diseño y personalización, habría que utilizar algún resizing de imágenes y elementos, que con el tiempo dado no pudimos corregir), layouts y frames no actualizables, uso de tamaños no muy claro (en nuestro caso casi aleatorio).
Problemas de código repetido: el código se estaba tornando muy denso y repetitivo, por lo que decidimos reorganizar el enfoque imperativo por módulos, para pasar a un enfoque orientado a objetos, en su momento para las clases player y settings.
Separación de las clases: fue uno de las principales preocupaciones en el enfoque, pasamos por diferentes ideas, y al final lo organizamos de acuerdo a los archivos con los que cada clase interactuaba, player y settings tuvieron que compartir un mismo módulo, por errores de importación circular (debido a que compartían utilidades), estas también terminaron por ser completamente estáticas, ya que debido al uso de los datos, la instanciación de objetos era completamente prescindible (y hasta contraproducente, por dificultades en comunicación).
Problemas en el uso manual de archivos: Una de nuestras principales motivaciones fue en torno al uso seguro del programa (sin rupturas) a pesar de la manipulación manual de los archivos. Los efecto antel borrado y/o modificación (con posibles rupturas de las correspondencias entre los datos) de los archivos de datos (para partidas, configuraciones y perfiles) se intenta mitigar de forma constante, evitando el corte de ejecución del programa; aunque no se recomienda la manipulación manual de los mismos ante ningún caso.  

---

# Consideraciones Éticas sobre el Desarrollo
- Por cuestiones de tiempo no pudimos agregar funciones de accesibilidad, nos hubiera gustado tener un modo de contraste alto, o un cambio dinámico de tamaño de fuente***
- Todo lo utilizado es propio o libre, y la licencia del proyecto es libre***
- Elección de cualquier género
- En esta sección podrían mencionar aspectos de accesibilidad, licencias de los recursos, dependencia de un sistema operativo específico (especialmente si se requiere licencia), etc.

---

# Conclusiones y trabajos futuros
- Lo aprendido es completísimo, el mayor valor que le sacamos es para la creación de un proyecto de software, trabajo en grupo para la creación de un proyecto, introduce mucho al mundo práctico de esta carrera.
hablar de git y repositorios
hablar de venv
hablar de estructuras de directorios y usos de direcciones y módulos
- PySimpleGUI es una librería con altísimas limitaciones si se busca hacer un diseño estético; el uso de imágenes y tamaños genera muchísimas complicaciones. El uso de tal vez otra librería, o tal vez una guía que presente estas limitaciones desde antes de comenzar el proyecto hubiera sido muy útil***
Referencias

---

# Guía de Usuario
Acá podrían incluir capturas de pantalla de la aplicación, con una guía de cómo se opera.
La Figura 1 muestra una captura de la pantalla inicial del juego…..

Figura 1. Captura de…..


- Descarga, guía de instalación, instalación de dependencias con requirements y qué ejecutar.
- Advertencia recomendando no tocar archivos.
- Capturas de estilo “how to play”, explicando la interfaz, y cada recomendación (juejo, configuración, perfiles, scores, …).

---

# Guía para Desarrolladores
Comenzando por la estructura de directorios, tendremos una estructura como se muestra en la imagen:

![Main Directory Structure](images/structure_guide_1.png)

Todos los archivos de Lectura/Escritura se ubicarán en “data”, para el acceso a un archivo se recomienda añadir su dirección como una constante en “src > constants > directions”, se recomienda seguir con el orden por subdirectorios, para facilitar la ubicación de cada archivo (una buena práctica sería por ejemplo separar las imágenes por uso, como se vino haciendo hasta el release v3.0 - o “tercer entrega”, como prefieren decirle algunos).
Para el agregado de programas que no sean utilizados en la ejecución del juego y que utilicen los datos (ya sea en forma de lectura o escritura), se hará dentro del directorio “data_management”.
El código del programa se alojará en “src”, la estructura dentro del mismo está también definida, para un mayor orden:

![src Directory Structure](images/structure_guide_2.png)

El funcionamiento se basará en 3 sectores principales: **datos**, **clases** y **ventanas**. La interacción entre estos 3 irá definiendo toda la estructura; clases y ventanas consultarán constantemente las constantes del proyecto y el contenido de lectura de “data”.

La _interacción con los archivos volátiles_ (“matches” con los datos de partidas, “users” con los datos de los usuarios, “loaded_nicks” con todos los nicks en uso y correspondencia de acceso con usuarios en “users”, y “cached_settings”) será principalmente (si no de forma exclusiva) por medio de las **clases**, que _a su vez interactuarán con cada ventana_, y estas con el usuario.
<br>
Las **ventanas** _interactuarán con el usuario y las clases_. Se busca que cada ventana esté contenida en un programa dedicado, el cual tendrá la función creadora del layout, la función creadora de la ventana y el loop de ejecución de la misma, además de cualquier función que se quiera, si es esta exclusiva de esta ventana. En la carpeta window podremos ubicar otras funciones si son exclusivamente para uso de GUI (un ejemplo es “card_creation.py”, con funcionalidades para la creación de botones y tarjetas en la ventana de juego).
<br>
Para el escalado eficiente del programa, cualquier agregado en estilos o direcciones deberá verse reflejado en **constants**, que contendrá todas las _constantes del programa_.

---

Explicar cada ventana se considera innecesario, conociendo la estructura que acaba de mencionarse y el recorrido mencionado en la guía de usuario debería ser más que suficiente. Con las clases, consideramos útil una explicación en profundidad, por lo que procederemos a explicar cada una:

### Match
La instancia de esta clase va a controlar una partida de una forma que consideramos de “bajo nivel”, desde interacción con los archivos hasta el guardado de los datos de la misma. Creará y guardará los eventos en una lista temporal que contendrá un conjunto de los mismos, para luego ante la finalización de la partida guardarlos (si esto es lo que se pide) en el archivo “matches.csv”. Obtiene de “Settings” los datos actuales de configuración, y escribirá en “matches.csv”.

### InGameEvents
Al crear una instancia (que recibirá una referencia para el objeto “Match” referente a la partida en curso, y otra para la ventana siendo usada actualmente), controlaremos la comunicación entre el objeto de la partida y la ventana. Contiene funciones específicas para cada evento producido desde la ventana (como tiempo acabado, respuesta acertada, partida abandonada, etc.), y para la modificación de la ventana en uso (para la actualización en botones y tarjetas de una forma mucho más legible y eficiente). Será un nexo entre la ventana de juego y la instancia de la partida actual.

### Settings
Será completamente estática, no instanciable (al igual que la clase “Player”, por temas de eficiencia y simplicidad, ya que así se cumple mejor con el fin y se descartan errores). Contendrá información sobre la configuración actual de la partida, obteniendo los datos de la ejecución más reciente de “cached_settings.json”, y actualizando el mismo al cerrarse la ventana de menú, preparando los datos para la próxima ejecución.

### Player
Será completamente estática y controlará los datos de los jugadores, ya sean eliminaciones, modificaciones, creaciones, o manejos de problemas de consistencia. Tendrá disponibles los datos modificables del jugador actual (no el nick ni los datos de partidas jugadas), y ante cualquier modificación los actualizará.

---

Como último tema importante a tratar, podemos hablar de las consideraciones hacia los posibles errores por modificación manual de los archivos, que fue una de las preocupaciones principales al momento de llevar a cabo las clases (que llevarán toda interacción con los datos). El fin principal en el que nos centramos fue en evitar la ruptura del programa y/o la muestra de información no válida, por lo que ante cualquier inconsistencia en los datos, error en la estructura del archivo, cargado de datos no válidos, fallo por archivo inexistente, etcétera; se creará un nuevo archivo en blanco y se pisará la dirección en la que este debería existir. Esto es una tarea muy compleja, por lo que seguirán habiendo errores en contadas ocasiones, la guía de uso en “README.txt” deberá advertir en contra de esta práctica, y ante cualquier error a causa de esto, recomendar una reinstalación del paquete completo.



