package com.github.th0ma5w.live-jython-processing;

import org.python.core.*; 
import org.python.util.PythonInterpreter; 
import java.util.Properties;
import java.io.*;
import processing.core.*;
import java.lang.*;
import processing.opengl.*;

public class Display extends PApplet {

	public PythonInterpreter interp;

	public PVector v;
	
	public void setup() {
		size(screenWidth,screenHeight,OPENGL);
//		size(screenWidth,screenHeight,P3D);
		hint(ENABLE_OPENGL_4X_SMOOTH);
		background(0);
		interp = new PythonInterpreter();
		interp.set("P",this);
		interp.execfile("bootup.py");
	}

	public PVector pvector(float x, float y){
		return new PVector(x,y);
	}
	
	public void draw() {
		interp.set("isMousePressed",new Boolean(mousePressed));
		interp.set("isKeyPressed",new Boolean(keyPressed));
		interp.set("focused",new Boolean(focused));
		interp.set("mouseX",new Integer(mouseX));
		interp.set("mouseY",new Integer(mouseY));
		interp.set("pmouseX",new Integer(pmouseX));
		interp.set("pmouseY",new Integer(pmouseY));
		interp.set("currentFrameRate",new Float(frameRate));
		interp.set("key",new Character(key));
		interp.set("keyCode",new Integer(keyCode));
		jexec("doDraw()");
	}
	
	public boolean jexec(String x){  
		try{
			interp.exec(x);
			return true;
		} catch(Exception e) {
			e.printStackTrace();
			return false;
		}
	}
  
	public static void main(String args[]) {
		PApplet.main(new String[] { "--present", "com.ohioheavydata.jython.Display" });
	}
}
