
package actividad17;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.Test;

public class Actividad17Test {

    @Test
    void pruebaSalidaEsperada() throws Exception {
        assertEquals("Mundo", ejecutarMain().trim());
    }

    private String ejecutarMain() throws Exception {
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        PrintStream original = System.out;
        System.setOut(new PrintStream(buffer, true, "UTF-8"));
        try {
            Actividad17.main(new String[0]);
        } finally {
            System.setOut(original);
        }
        return buffer.toString().replace("\r\n", "\n");
    }
}
