
# Curso Oracle Java Foundations 2026

Esta colección contiene 20 actividades autocorregibles diseñadas para alumnos que usan Eclipse IDE con Java 21, Maven y Git.

## Estructura de la solución

- Cada actividad es un proyecto Maven independiente.
- Cada proyecto contiene código base, tests JUnit 5 y un workflow de GitHub Actions.
- El nombre de los repositorios debe seguir la convención:
  - `actividad01-nombre-apellido`
  - `actividad02-nombre-apellido`
- La organización de GitHub recomendada es `java-foundations-2026`.

## Cómo usar esto en la organización de GitHub

1. Crea la organización `java-foundations-2026`.
2. Crea un repositorio de plantilla para cada actividad a partir del contenido de los directorios `actividad01` ... `actividad20`.
3. Pide a cada alumno que cree su repositorio a partir de la plantilla correspondiente.
4. Cada alumno debe clonar su repositorio, abrirlo en Eclipse, corregir el código y hacer `git push`.
5. GitHub Actions ejecutará los tests automáticamente y mostrará aprobado / suspenso.

## Convenciones de nombres

- Repositorio de alumno: `actividadNN-nombre-apellido`
- Ejemplo: `actividad01-juan-perez`, `actividad15-maria-garcia`
- Cada repositorio debe contener el mismo contenido que el directorio `actividadNN`.

## Instalación

1. Instala Java 21 (OpenJDK o Temurin).
2. Instala Eclipse IDE para Java Developers.
3. Instala Maven si quieres usarlo desde la línea de comandos.
4. Instala Git.

## Importar un proyecto Maven en Eclipse

1. Abre Eclipse.
2. Ve a `File > Import...`.
3. Selecciona `Maven > Existing Maven Projects` y haz clic en `Next`.
4. Selecciona la carpeta raíz del proyecto (por ejemplo `actividad01`).
5. Marca el proyecto que aparece y haz clic en `Finish`.

## Ejecutar programas Java en Eclipse

1. En el `Package Explorer`, abre `src/main/java` y selecciona la clase `ActividadNN`.
2. Haz clic derecho en la clase.
3. Elige `Run As > Java Application`.

## Ejecutar tests en Eclipse

1. Haz clic derecho en el proyecto o en la clase de test dentro de `src/test/java`.
2. Selecciona `Run As > JUnit Test`.
3. Eclipse mostrará resultados verdes si el test pasa o rojos si falla.

## Commit y push desde Eclipse

1. Abre la vista `Git Staging` (`Window > Show View > Other... > Git > Git Staging`).
2. Arrastra los archivos modificados desde `Unstaged Changes` a `Staged Changes`.
3. Escribe un mensaje de commit.
4. Haz clic en `Commit and Push`.

## Interpretar GitHub Actions

1. En GitHub, entra en el repositorio del alumno.
2. Ve a la pestaña `Actions`.
3. Selecciona el flujo de trabajo `Java CI`.
4. Si el workflow pasa, el ejercicio está aprobado.
5. Si falla, revisa los tests y el mensaje de error.

## Ejemplo de flujo de trabajo para el profesor

- Revisa los repositorios de la organización `java-foundations-2026`.
- En la pestaña `Actions`, cada repositorio muestra la última ejecución.
- Un estado verde significa que el código pasó los tests.
- Un estado rojo significa que el alumno debe corregir el ejercicio.
