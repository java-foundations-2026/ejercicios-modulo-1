import os
import textwrap

root = os.getcwd()

activity_data = [
    (1, "Corregir un programa que falta un punto y coma.", "Hola mundo", [
        'package actividad01;',
        'public class Actividad01 {',
        '    public static void main(String[] args) {',
        '        System.out.println("Hola mundo")',
        '    }',
        '}',
    ]),
    (2, "Corregir println mal escrito.", "Hola", [
        'package actividad02;',
        'public class Actividad02 {',
        '    public static void main(String[] args) {',
        '        System.out.printn("Hola");',
        '    }',
        '}',
    ]),
    (3, "Corregir un programa que falta comillas.", "Hola mundo", [
        'package actividad03;',
        'public class Actividad03 {',
        '    public static void main(String[] args) {',
        '        System.out.println(Hola mundo);',
        '    }',
        '}',
    ]),
    (4, "Corregir un programa con llaves desbalanceadas.", "Hola", [
        'package actividad04;',
        'public class Actividad04 {',
        '    public static void main(String[] args) {',
        '        System.out.println("Hola");',
        '    ',
        '}',
    ]),
    (5, "Corregir el nombre de la clase pública en el archivo.", "Hola", [
        'package actividad05;',
        'public class ActividadCinco {',
        '    public static void main(String[] args) {',
        '        System.out.println("Hola");',
        '    }',
        '}',
    ]),
    (6, "Crear un programa que imprima Hola.", "Hola", [
        'package actividad06;',
        'public class Actividad06 {',
        '    public static void main(String[] args) {',
        '        // TODO: imprime Hola',
        '    }',
        '}',
    ]),
    (7, "Crear un programa que imprima Hola y Adiós.", "Hola\nAdiós", [
        'package actividad07;',
        'public class Actividad07 {',
        '    public static void main(String[] args) {',
        '        // TODO: imprime Hola',
        '        // TODO: imprime Adiós',
        '    }',
        '}',
    ]),
    (8, "Crear un programa que imprima Java Foundations Oracle.", "Java\nFoundations\nOracle", [
        'package actividad08;',
        'public class Actividad08 {',
        '    public static void main(String[] args) {',
        '        // TODO: imprime Java, Foundations y Oracle en líneas separadas',
        '    }',
        '}',
    ]),
    (9, "Crear un programa que imprima 1 2 3.", "1\n2\n3", [
        'package actividad09;',
        'public class Actividad09 {',
        '    public static void main(String[] args) {',
        '        // TODO: imprime 1, 2 y 3 en líneas separadas',
        '    }',
        '}',
    ]),
    (10, "Crear un programa que imprima Hola, línea en blanco, Mundo.", "Hola\n\nMundo", [
        'package actividad10;',
        'public class Actividad10 {',
        '    public static void main(String[] args) {',
        '        // TODO: imprime Hola, una línea en blanco y Mundo',
        '    }',
        '}',
    ]),
    (11, "Crear un programa que imprima Hola mundo.", "Hola mundo", [
        'package actividad11;',
        'public class Actividad11 {',
        '    public static void main(String[] args) {',
        '        // TODO: imprime Hola mundo',
        '    }',
        '}',
    ]),
    (12, "Crear un programa que imprima Bienvenidos al curso de Java.", "Bienvenidos al curso de Java", [
        'package actividad12;',
        'public class Actividad12 {',
        '    public static void main(String[] args) {',
        '        // TODO: imprime Bienvenidos al curso de Java',
        '    }',
        '}',
    ]),
    (13, "Crear un programa que imprima Línea 1, Línea 2, Línea 3.", "Línea 1\nLínea 2\nLínea 3", [
        'package actividad13;',
        'public class Actividad13 {',
        '    public static void main(String[] args) {',
        '        // TODO: imprime Línea 1, Línea 2 y Línea 3',
        '    }',
        '}',
    ]),
    (14, "Crear un programa que imprima ---.", "---", [
        'package actividad14;',
        'public class Actividad14 {',
        '    public static void main(String[] args) {',
        '        // TODO: imprime tres guiones',
        '    }',
        '}',
    ]),
    (15, "Crear un programa que imprima Nombre: Ana, Ciudad: Madrid, Edad: 20.", "Nombre: Ana\nCiudad: Madrid\nEdad: 20", [
        'package actividad15;',
        'public class Actividad15 {',
        '    public static void main(String[] args) {',
        '        // TODO: imprime la tabla con Nombre, Ciudad y Edad',
        '    }',
        '}',
    ]),
    (16, "Introducir comentarios de una línea.", "Hola\nAdiós", [
        'package actividad16;',
        'public class Actividad16 {',
        '    public static void main(String[] args) {',
        '        // TODO: añade un comentario sobre la siguiente línea',
        '        System.out.println("Hola");',
        '        // TODO: añade otro comentario sobre la siguiente línea',
        '        System.out.println("Adiós");',
        '    }',
        '}',
    ]),
    (17, "Explicar que una línea comentada no se ejecuta.", "Mundo", [
        'package actividad17;',
        'public class Actividad17 {',
        '    public static void main(String[] args) {',
        '        // System.out.println("Hola");',
        '        System.out.println("Mundo");',
        '    }',
        '}',
    ]),
    (18, "Introducir variables String.", "Pedro", [
        'package actividad18;',
        'public class Actividad18 {',
        '    public static void main(String[] args) {',
        '        String nombre = _______;',
        '        System.out.println(nombre);',
        '    }',
        '}',
    ]),
    (19, "Crear String ciudad = \"Madrid\"; y mostrarla por pantalla.", "Madrid", [
        'package actividad19;',
        'public class Actividad19 {',
        '    public static void main(String[] args) {',
        '        // TODO: declara String ciudad con el valor "Madrid" y muéstrala',
        '    }',
        '}',
    ]),
    (20, "Introducir concatenación con +.", "Nombre: Laura\nEdad: 22", [
        'package actividad20;',
        'public class Actividad20 {',
        '    public static void main(String[] args) {',
        '        // Nombre: Laura',
        '        // Edad: 22',
        '        // Explica el operador + usando concatenación en la siguiente línea',
        '        String nombre = "Laura";',
        '        int edad = 22;',
        '        System.out.println("Nombre: " + nombre);',
        '        System.out.println("Edad: " + edad);',
        '    }',
        '}',
    ]),
]

pom_template = textwrap.dedent('''
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>org.javafoundations2026</groupId>
    <artifactId>{artifact}</artifactId>
    <version>1.0-SNAPSHOT</version>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <junit.jupiter.version>5.10.0</junit.jupiter.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${{junit.jupiter.version}}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <release>21</release>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.1.2</version>
            </plugin>
        </plugins>
    </build>
</project>
''')

workflow_content = textwrap.dedent('''
name: Java CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '21'
      - name: Build and test
        run: mvn -B test
''')

root_readme = textwrap.dedent('''
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
''')

activity_readme_template = textwrap.dedent('''
# Actividad {num:02d}

{description}

## Objetivo

- Ejecutar el programa y comprobar que la salida coincide con la esperada.
- Utilizar Eclipse IDE para corregir el código.
- Hacer `git add`, `git commit` y `git push`.

## Salida esperada

```text
{expected}
```

## Instrucciones para Eclipse

1. Importa este proyecto en Eclipse como un proyecto Maven.
2. Abre `src/main/java/actividad{num:02d}/Actividad{num:02d}.java`.
3. Corrige el código si es necesario.
4. Ejecuta `Run As > Java Application`.
5. Ejecuta los tests desde `src/test/java/actividad{num:02d}/Actividad{num:02d}Test.java` con `Run As > JUnit Test`.
6. Haz commit y push cuando la actividad funcione.

## GitHub Actions

- El workflow `Java CI` se ejecuta automáticamente en cada `push`.
- Si pasa, el repositorio está aprobado.
- Si falla, revisa los errores de compilación o los tests.
''')

for num, desc, expected, code_lines in activity_data:
    dir_name = f"actividad{num:02d}"
    project_dir = os.path.join(root, dir_name)
    src_main = os.path.join(project_dir, 'src', 'main', 'java', dir_name)
    src_test = os.path.join(project_dir, 'src', 'test', 'java', dir_name)
    os.makedirs(src_main, exist_ok=True)
    os.makedirs(src_test, exist_ok=True)
    class_name = f"Actividad{num:02d}"
    with open(os.path.join(src_main, f"{class_name}.java"), 'w', encoding='utf-8') as f:
        f.write('\n'.join(code_lines) + '\n')
    test_template = textwrap.dedent('''
package {pkg};

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.Test;

public class {class_name}Test {{

    @Test
    void pruebaSalidaEsperada() throws Exception {{
        assertEquals("{expected}", ejecutarMain().trim());
    }}

    private String ejecutarMain() throws Exception {{
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        PrintStream original = System.out;
        System.setOut(new PrintStream(buffer, true, "UTF-8"));
        try {{
            {class_name}.main(new String[0]);
        }} finally {{
            System.setOut(original);
        }}
        return buffer.toString().replace("\r\n", "\n");
    }}
}}
''')
    with open(os.path.join(src_test, f"{class_name}Test.java"), 'w', encoding='utf-8') as f:
        f.write(test_template.format(pkg=dir_name, class_name=class_name, expected=expected))
    with open(os.path.join(project_dir, 'pom.xml'), 'w', encoding='utf-8') as f:
        f.write(pom_template.format(artifact=dir_name))
    with open(os.path.join(project_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(activity_readme_template.format(num=num, description=desc, expected=expected))
    with open(os.path.join(project_dir, '.gitignore'), 'w', encoding='utf-8') as f:
        f.write('/target\n/.classpath\n/.project\n/.settings/\n*.log\n')
    workflow_dir = os.path.join(project_dir, '.github', 'workflows')
    os.makedirs(workflow_dir, exist_ok=True)
    with open(os.path.join(workflow_dir, 'java-ci.yml'), 'w', encoding='utf-8') as f:
        f.write(workflow_content)

with open(os.path.join(root, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(root_readme)
with open(os.path.join(root, 'workflow-template.yml'), 'w', encoding='utf-8') as f:
    f.write(workflow_content)

print('Generated', len(activity_data), 'activity projects in', root)
