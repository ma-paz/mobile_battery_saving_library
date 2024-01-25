import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.os.PowerManager;
import android.view.MotionEvent;
import android.view.WindowManager;

public class ScreenManagerActivity extends Activity {

    private PowerManager.WakeLock wakeLock;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Turn off the screen
        turnOffScreen();

        // Acquire a wake lock to keep the device awake
        acquireWakeLock();
    }

    private void turnOffScreen() {
        WindowManager.LayoutParams layoutParams = getWindow().getAttributes();
        layoutParams.screenBrightness = 0.0f; // Set brightness to 0
        getWindow().setAttributes(layoutParams);

        // Optionally, you might want to turn off the keyguard
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_DISMISS_KEYGUARD);
    }

    private void acquireWakeLock() {
        PowerManager powerManager = (PowerManager) getSystemService(Context.POWER_SERVICE);
        wakeLock = powerManager.newWakeLock(PowerManager.FULL_WAKE_LOCK, "MyWakeLockTag");
        wakeLock.acquire();
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        // Release the wake lock when the user interacts with the screen
        if (wakeLock != null && wakeLock.isHeld()) {
            wakeLock.release();
        }
        return super.onTouchEvent(event);
    }
}
public class RetryWithBackoffExample {

    // Define a functional interface for the method to be retried
    @FunctionalInterface
    interface RetryableMethod {
        void run() throws Exception;
    }

    // Method A: Retry method B with backoff
    public static void retryWithBackoff(RetryableMethod methodB) {
        int maxAttempts = 3;
        long initialDelayMillis = 1000; // Initial delay in milliseconds

        for (int attempt = 1; attempt <= maxAttempts; attempt++) {
            try {
                methodB.run(); // Execute method B
                return; // If successful, exit the loop
            } catch (Exception e) {
                // Log or handle the exception (you can customize this part)
                System.err.println("Attempt " + attempt + " failed: " + e.getMessage());

                if (attempt < maxAttempts) {
                    // If not the last attempt, apply backoff delay
                    long delayMillis = initialDelayMillis * attempt;
                    try {
                        Thread.sleep(delayMillis);
                    } catch (InterruptedException interruptedException) {
                        Thread.currentThread().interrupt();
                    }
                }
            }
        }

        // Return an error if maxAttempts reached
        System.err.println("All attempts failed. Returning an error.");
    }

    // Method B: An example method that might throw an exception
    public static void methodB() throws Exception {
        // Replace this with the actual implementation of method B
        // For example, this could be an API call, database operation, etc.
        // For simplicity, this example just throws an exception.
        throw new Exception("Method B failed!");
    }

    public static void main(String[] args) {
        // Example usage: Retry methodB with backoff
        retryWithBackoff(() -> methodB());
    }
}
//para el algoritmo de color...
