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
