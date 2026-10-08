package com.stardopredict.app

import android.app.Activity
import android.os.Bundle
import android.widget.TextView

class MainActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val textView = TextView(this)
        textView.text = "StardoPredict"
        textView.textSize = 28f
        textView.setPadding(40, 80, 40, 40)

        setContentView(textView)
    }
}
