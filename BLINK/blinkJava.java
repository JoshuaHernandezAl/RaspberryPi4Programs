class blinkJava{
	public static void main(String args[]){
		System.out.println("Ctrl+C");
		try{
			Runtime runTime = Runtime.getRuntime();
			runTime.exec("gpio mode 29 out");
				
			while(true){
				
				runTime.exec("gpio write 29 1");
				Thread.sleep(500);
				runTime.exec("gpio write 29 0");
				Thread.sleep(500);
			}
		}catch (Exception e){
			System.out.println("Exception ocurred: " + e.getMessage());
		}
		
	}
}
