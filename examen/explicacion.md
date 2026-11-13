## Parte 1 · Comprensión técnica (30 puntos) 

1. Actividad 1. Explicación integrada (20 puntos) 

## Situación: una empresa tiene una aplicación Flask que permite consultar información desde un navegador y calcular el importe de una compra. El empleado captura cantidad y precio, envía el formulario y visualiza el resultado. 

Primero, el empleado entra al navegador desde su computadora, la cual funciona como el **cliente**. En la barra de direcciones escribe la URL para entrar a la app. Esa peticion necesita saber exactamente a donde ir, por lo que busca el **servidor** usando su **dirección IP** y el **puerto** donde esta corriendo la aplicacion (por ejemplo, el puerto 5000 en Flask).
Al presionar Enter, el **cliente** manda una **request** utilizando el protocolo **HTTP**. Esta **request** llega por la red hasta el **servidor**, donde esta la parte del **backend**. En el **backend** tenemos nuestro programa programado en **Python** junto con la libreria **Flask**.
Cuando la **request** entra al **backend, Flask** la analiza y busca la **ruta** que coincide con la URL que se consulto (por ejemplo la **ruta** @app.route('/')). La funcion asociada a esa **ruta** ejecuta una instruccion para renderizar un **template**. El **servidor** toma ese archivo y genera una **response HTTP** con todo el codigo necesario para mostrar la pantalla inicial.
El navegador del **cliente** recibe la **response** y empieza a renderizar el **frontend**. El **frontend** de nuestra app esta construido con la estructura de **HTML** y los estilos de **CSS**, utilizando la libreria de **Bootstrap** para que los botones y las cajas de texto del formulario se vean bien acomodados. En este punto **JavaScript** no interviene, ya que la aplicacion carga directamente la estructura visual estatica sin requerir interactividad dinámica en el navegador antes de enviar los datos.
Una vez que el empleado ve el formulario en pantalla, escribe la cantidad y el precio del producto y le da clic al boton de enviar. El formulario ejecuta una accion y manda una nueva **request HTTP**, pero utilizando el metodo **POST** para enviar los datos de la compra dentro del cuerpo del mensaje de forma segura.
El **servidor** recibe la **request** con el metodo **POST** y la dirige a la **ruta** encargada de hacer las cuentas. Ahi, el **backend** procesa los datos usando **Python**, convirtiendo las entradas del usuario a numeros y calculando el importe total de la compra.
Por ultimo, **Python** le pasa la variable del resultado al template de respuesta, y **Flask** emite una ultima **HTTP**. El **cliente** recibe esta respuesta y el **frontend** muestra en la pantalla del navegador el resultado final de la compra de forma clara para el empleado.

2. Actividad 2. Diagrama explicado (10 puntos) 

## En el mismo explicacion.md incluye un diagrama de flujo de la comunicación navegador → servidor Flask →  respuesta. Puede realizarse con Mermaid en Markdown o como imagen insertada y enlazada desde el archivo.  Acompáñalo con una explicación breve que ubique el cliente, servidor, IP:puerto, la petición POST, el  procesamiento y el retorno del HTML. 

sequenceDiagram
    autonumber
    actor Empleado
    participant Cliente as Navegador (Cliente)
    participant Servidor as Servidor Flask (IP:Puerto)
    participant Backend as Backend (Python / Rutas)
    participant Template as Template (HTML + Bootstrap)

    Empleado->>Cliente: 1. Ingresa datos y envía formulario
    Cliente->>Servidor: 2. Petición POST (HTTP) a IP:Puerto
    Servidor->>Backend: 3. Recibe la request y busca la ruta
    Backend->>Backend: 4. Procesa y calcula importe con Python
    Backend->>Template: 5. Envía resultado al Template
    Template-->>Backend: 6. Renderiza el HTML final
    Backend-->>Servidor: 7. Genera la Response HTTP
    Servidor-->>Cliente: 8. Devuelve la Response HTTP (HTML/CSS)
    Cliente-->>Empleado: 9. Muestra el resultado en pantalla (Frontend)

El diagrama muestra el ciclo de vida de la comunicacion. Inicia en el cliente (navegador del usuario), el cual manda los datos del formulario mediante una peticion POST a la dirección IP y puerto del servidor. Una vez ahi, el servidor pasa la informacion al backend en Python, que ejecuta la ruta asignada para procesar la compra. Despues de hacer el calculo, se insertan los datos en el template, el servidor arma la response con el codigo HTML (con estilos CSS y Bootstrap de frontend) y la envia de vuelta al navegador para ser mostrada al usuario.