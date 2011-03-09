package com.github.th0ma5w.live-jython-processing;

import org.python.core.*; 
import org.python.util.InteractiveConsole;
import org.python.util.PythonInterpreter; 
import java.util.Properties;
import java.io.*;

public class App 
{
    protected InteractiveConsole interp;

    public App() {
        if (System.getProperty("python.home") == null) {
            System.setProperty("python.home", "");
        }
        InteractiveConsole.initialize(System.getProperties(),
                                      null, new String[0]);
        interp = new InteractiveConsole();
    }

    public static void main( String[] args )
    {
	App con = new App();
        con.startConsole();
    }
    public void startConsole() {
        interp.interact();
    }
}
