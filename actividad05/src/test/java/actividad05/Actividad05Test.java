
package actividad05;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.Test;

public class Actividad05Test {

    @Test
    void pruebaSalidaEsperada() throws Exception {
        assertEquals("Hola", ejecutarMain().trim());
    }

    private String ejecutarMain() throws Exception {
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        PrintStream original = System.out;
        System.setOut(new PrintStream(buffer, true, "UTF-8"));
        try {
            Actividad05.main(new String[0]);
        } finally {
            System.setOut(original);
        }
        return buffer.toString().replace("\r\n", "\n");
    }
}
