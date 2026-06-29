
package actividad20;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.Test;

public class Actividad20Test {

    @Test
    void pruebaSalidaEsperada() throws Exception {
        assertEquals("Nombre: Laura
Edad: 22", ejecutarMain().trim());
    }

    private String ejecutarMain() throws Exception {
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        PrintStream original = System.out;
        System.setOut(new PrintStream(buffer, true, "UTF-8"));
        try {
            Actividad20.main(new String[0]);
        } finally {
            System.setOut(original);
        }
        return buffer.toString().replace("
", "
");
    }
}
