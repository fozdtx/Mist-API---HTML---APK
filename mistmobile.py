# MIST MOBILE apk build processor
# 20190-Build-Code
# Written by ghgltggamer
# Started at 28 feb 2024 at 19:24pm in india / new delhi

import os
import subprocess
import zipfile
import shutil

def delete_file(destination_path):
    # Check if the file exists
    if os.path.isfile(destination_path):
        # Try to delete the file
        try:
            os.remove(destination_path)
            print(f"File {destination_path} has been deleted successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"No file found at {destination_path}")

def copy_file_to_directory(source_file_path, destination_directory):
    # Ensure the destination directory exists, if not, create it
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Define the destination file path
    destination_file_path = os.path.join(destination_directory, os.path.basename(source_file_path))

    # Copy the source file to the destination directory
    shutil.copy2(source_file_path, destination_file_path)
    print(f"File copied to {destination_file_path}")


def move_folder(source_path, destination_path):
    """
    Moves a folder and its contents from the source path to the destination path.

    Args:
        source_path (str): Path of the folder to be moved.
        destination_path (str): Destination path where the folder should be moved.
    """
    try:
        shutil.move(source_path, destination_path)
        print(f"Folder '{source_path}' moved to '{destination_path}' successfully.")
    except Exception as e:
        print(f"Error moving folder: {e}")

def extract_all_files_from_zip(zip_file_path, destination_path):
    """
    Extracts all files from a ZIP file to the specified destination path.

    Args:
        zip_file_path (str): Path to the ZIP file.
        destination_path (str): Path where the extracted files should be saved.
    """
    with zipfile.ZipFile(zip_file_path, 'r') as archive:
        archive.extractall(destination_path)

# Example usage:
# zip_file_path = 'archive.zip'
# destination_path = '/path/to/destination'
# extract_all_files_from_zip(zip_file_path, destination_path)


# asking for file name
f_name = input("Enter the file name which contains all the html css and js file (.zip): ");
p_name = input("Enter the package name's middle character: com.");
p_name_l = input("Enter the package name's lasst string: " + p_name + '.');
icon = input("Enter the icon path (512x512): ");
ver = input("Enter the version of your app (float values): ");
h_name = input("Enter your host name ie(example.com): ");
app_name = input("Enter your App name: ");

# build dir

print("\n\n\n Processing...\n\n");
print("-- Making Build Dir...\n\n");
os.system("mkdir build");
print("-- Done\n\n");

print("-- Copying gradle...\n\n");
os.system("copy a.zip build");
print("-- Done\n\n");

print("-- Opening Build Dir...\n\n");
os.system("cd build");
print("-- Done\n\n");

print("-- Extracting gradle...\n\n");
os.system("tar -xf build/a.zip");
print("-- Done\n\n");

print("-- Moving gradle...\n\n");

print("---- Moving settings of gradle...\n\n");
os.system("move settings.gradle build");
print("---- Done\n\n");

print("---- Moving gredle wrapper batch of gradle...\n\n");
os.system("move gradlew.bat build");
print("---- Done\n\n");

print("---- Moving gradle wrapper config of gradle...\n\n");
os.system("move gradlew build");
print("---- Done\n\n");

print("---- Moving properties of gradle...\n\n");
os.system("move gradle.properties build");
print("---- Done\n\n");

print("---- Moving build of gradle...\n\n");
os.system("move build.gradle build");
print("---- Done\n\n");

print("---- Moving full gradle directory...\n\n");
os.system("move gradle build");
print("---- Done\n\n");

print("-- Done\n\n");



print("-- Making App Dir...\n\n");
os.system("mkdir app");
print("-- Done\n\n");


print("-- Moving App Dir...\n\n");
os.system("move app build");
print("-- Done\n\n");



print("-- Making App Gradle Build...\n\n");

new_app_build_gradle = open("build/app/build.gradle", "x");

app_build_gradle = open("build/app/build.gradle", "w");

app_build_gradle_data = f"""apply plugin: 'com.android.application'

android {{
    compileSdkVersion 31

    defaultConfig {{
        applicationId "com.{p_name}.{p_name_l}"
        minSdkVersion 21
        targetSdkVersion 31
        versionCode 1
        versionName "{ver}"
    }}
    buildTypes {{
        release {{
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }}
    }}
}}

dependencies {{
    implementation fileTree(dir: 'libs', include: ['*.jar'])
}}
""";

app_build_gradle.write(app_build_gradle_data);



print("---- Making Rules build of app...\n\n");

new_pro_build_gradle = open("build/app/proguard-rule.proe", "x");

pro_build_gradle = open("build/app/proguard-rule.proe", "w");

pro_build_gradle_data = """# Add project specific ProGuard rules here.
# By default, the flags in this file are appended to flags specified
# in /Applications/Utilities/sdk/tools/proguard/proguard-android.txt
# You can edit the include path and order by changing the proguardFiles
# directive in build.gradle.
#
# For more details, see
#   http://developer.android.com/guide/developing/tools/proguard.html

# Add any project specific keep options here:

# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}
""";

pro_build_gradle.write(app_build_gradle_data);

print("---- Done\n\n");



print("---- Making source App Dir...\n\n");
os.system("mkdir src");
print("---- Done\n\n");

print("-- Moving source App Dir...\n\n");
os.system("move src build/app");
print("-- Done\n\n");



print("---- Making main App Dir...\n\n");
os.system("mkdir main");
print("---- Done\n\n");

print("-- Moving main App Dir...\n\n");
os.system("move main build/app/src");
print("-- Done\n\n");



print("---- Making Assets App Dir...\n\n");
os.system("mkdir assets");
print("---- Done\n\n");

print("-- Moving Assets App Dir...\n\n");
os.system("move assets build/app/src/main");
print("-- Done\n\n");


print("---- Extracting html files to App Dir...\n\n");

extract_all_files_from_zip(f_name, 'build/app/src/main/assets');

print("---- Done\n\n");




print("---- Making Java Dir to App Dir...\n\n");

os.system("mkdir java");

print("---- Done\n\n");



print("---- Making Java Packages to App Dir...\n\n");

os.system("mkdir com");

print("---- Done\n\n");



print("---- Making Java Packages stage 2 to App Dir...\n\n");

os.system(f"mkdir {p_name}");

print("---- Done\n\n");



print("------ Making Java Packages stage 3 to App Dir...\n\n");

os.system(f"mkdir {p_name_l}");

print("------ Done\n\n");


print("------ Resolving Java Packages stage 1 to App Dir...\n\n");

os.system("move com java");

print("------ Done\n\n");



print("------ Resolving Java Packages stage 1 to App Dir...\n\n");

os.system(f"move {p_name} java/com");

print("------ Done\n\n");


print("------ Resolving Java Packages stage 1 to App Dir...\n\n");

os.system(f"move {p_name_l} java/com/{p_name}/{p_name_l}");

print("------ Done\n\n");




print("------ Making Java Web View Script for App...\n\n");

java_web_view = open(f"java/com/{p_name}/{p_name_l}/MyWebViewClient.java", "x");

print("------ Done\n\n");


print("------ Writting Java Web View Script for App...\n\n");


java_web_view_script = f'''package com.{p_name}.{p_name_l};

import android.content.Intent;
import android.net.Uri;
import android.webkit.WebView;
import android.webkit.WebViewClient;

class MyWebViewClient extends WebViewClient {{

    @Override
    public boolean shouldOverrideUrlLoading(WebView view, String url) {{
        String hostname;

        // YOUR HOSTNAME
        hostname = "{h_name}";

        Uri uri = Uri.parse(url);
        if (url.startsWith("file:") || uri.getHost() != null && uri.getHost().endsWith(hostname)) {{
            return false;
        }}
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
        view.getContext().startActivity(intent);
        return true;
    }}
}}
''';


java_web_view_dat = open(f"java/com/{p_name}/{p_name_l}/MyWebViewClient.java", "w");

java_web_view_dat.write(java_web_view_script);

java_web_view.close();
java_web_view_dat.close();
print("------ Done\n\n");









print("------ Making Java Packages stage 3 to App Dir...\n\n");

os.system(f"mkdir {p_name_l}");

print("------ Done\n\n");


print("------ Making Java Main Activity Script for App...\n\n");

java_main_activity = open(f"java/com/{p_name}/{p_name_l}/MainActivity.java", "x");

print("------ Done\n\n");


print("------ Writting Main Activity Script for App...\n\n");


java_main_activity_script = f'''package com.{p_name}.{p_name_l};

import android.annotation.SuppressLint;
import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;

public class MainActivity extends Activity {{

    private WebView mWebView;

    @Override
    @SuppressLint("SetJavaScriptEnabled")
    protected void onCreate(Bundle savedInstanceState) {{
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mWebView = findViewById(R.id.activity_main_webview);
        WebSettings webSettings = mWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        mWebView.setWebViewClient(new MyWebViewClient());

        // REMOTE RESOURCE
        // mWebView.loadUrl("https://example.com");

        // LOCAL RESOURCE
        // mWebView.loadUrl("file:///android_asset/index.html");
    }}

    @Override
    public void onBackPressed() {{
        if(mWebView.canGoBack()) {{
            mWebView.goBack();
        }} else {{
            super.onBackPressed();
        }}
    }}
}}
''';


java_main_activity_dat = open(f"java/com/{p_name}/{p_name_l}/MainActivity.java", "w");

java_main_activity_dat.write(java_main_activity_script);

java_main_activity.close();
java_main_activity_dat.close();
print("------ Done\n\n");









print("------ Moving Java Packages stage final to App Dir...\n\n");


# os.system('icacls build/app/src/main /grant administrators:F /t');
# os.system("move java build/app/src/main");


move_folder("java", "build/app/src/main");





print("------ Checking all files in root Dir...\n\n");

os.system("dir");
os.system("dir build");
os.system("dir build/app");
os.system("dir build/app/src");
os.system("dir build/app/src/main"); 
os.system("dir build/app/src/main/assets");
os.system("dir build/app/src/main/java");

print("------ Done\n\n");




print("------ Making style resource dir all files in root Dir...\n\n");

os.system("mkdir res");


print("------ Done\n\n");


print("------ Making style resource layout dir all files in root Dir...\n\n");

os.system("mkdir layout");


print("------ Done\n\n");

print("------ Moving style resource layout dir all files in root Dir...\n\n");

os.system("move layout res");


print("------ Done\n\n");





print("------ Making style resource mip maps stage 1 dir all files in root Dir...\n\n");

os.system("mkdir mipmap-hdpi");


print("------ Done\n\n");

print("------ Moving style resource mip map stage 1 dir all files in root Dir...\n\n");

os.system("move mipmap-hdpi res");


print("------ Done\n\n");


print("------ Making style resource mip maps stage 2 dir all files in root Dir...\n\n");

os.system("mkdir mipmap-mdpi");


print("------ Done\n\n");

print("------ Moving style resource mip map stage 2 dir all files in root Dir...\n\n");

os.system("move mipmap-mdpi res");


print("------ Done\n\n");


print("------ Done\n\n");



print("------ Making style resource mip maps stage 3 dir all files in root Dir...\n\n");

os.system("mkdir mipmap-xhdpi");


print("------ Done\n\n");

print("------ Moving style resource mip map stage 3 dir all files in root Dir...\n\n");

os.system("move mipmap-xhdpi res");


print("------ Done\n\n");






print("------ Making style resource mip maps stage 4 dir all files in root Dir...\n\n");

os.system("mkdir mipmap-xxhdpi");


print("------ Done\n\n");

print("------ Moving style resource mip map stage 4 dir all files in root Dir...\n\n");

os.system("move mipmap-xxhdpi res");


print("------ Done\n\n");






print("------ Making style resource mip maps stage 5 dir all files in root Dir...\n\n");

os.system("mkdir mipmap-xxxhdpi");


print("------ Done\n\n");

print("------ Moving style resource mip map stage 5 dir all files in root Dir...\n\n");

os.system("move mipmap-xxxhdpi res");


print("------ Done\n\n");



print("------ Making style resource mip maps stage 1 dir all files in root Dir...\n\n");

os.system("mkdir values");


print("------ Done\n\n");

print("------ Moving style resource mip map stage 1 dir all files in root Dir...\n\n");

os.system("move values res");


print("------ Done\n\n");





print("------ Setting the app icon...\n\n");

os.system(f"ren {icon} ic_launcher-web.png");


print("------ Done\n\n");


print("------ Moving the app icon...\n\n");

copy_file_to_directory('ic_launcher-web.png', 'build/app/src/main');


print("------ Done\n\n");




print("------ Setting the log app 1 icon...\n\n");

os.system(f"ren ic_launcher-web.png ic_launcher.png");


print("------ Done\n\n");

print("------ Moving the log app 1 icon...\n\n");

copy_file_to_directory("ic_launcher.png", "res/mipmap-hdpi");


print("------ Done\n\n");









print("------ Moving the log app 2 icon...\n\n");

copy_file_to_directory("ic_launcher.png", "res/mipmap-mdpi");



print("------ Done\n\n");











print("------ Moving the log app 3 icon...\n\n");

copy_file_to_directory("ic_launcher.png", "res/mipmap-xhdpi");


print("------ Done\n\n");










print("------ Moving the log app 4 icon...\n\n");

copy_file_to_directory("ic_launcher.png", "res/mipmap-xxhdpi");


print("------ Done\n\n");







print("------ Moving the log app 5 icon...\n\n");

copy_file_to_directory("ic_launcher.png", "res/mipmap-xxxhdpi");


print("------ Done\n\n");




print("------ Renaming the log app 5 icon...\n\n");

os.system(f"ren ic_launcher.png {icon}");


print("------ Done\n\n");
#activity_main.xml



print("------ Making layout style with xml...\n\n");

xml_layout = open("res/layout/activity_main.xml", "x");
xml_layout.close();

print("------ Done\n\n");


print("------ Writting layout style with xml...\n\n");

xml_layout_w = open("res/layout/activity_main.xml", "w");


xml_layout_data = '''<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <WebView
        android:id="@+id/activity_main_webview"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</RelativeLayout>''';

xml_layout_w.write(xml_layout_data);


xml_layout_w.close();

print("------ Done\n\n");






print("------ Making App name with xml...\n\n");

xml_app_name = open("res/values/strings.xml", "x");
xml_app_name.close();

print("------ Done\n\n");


print("------ Writting App name with xml...\n\n");

xml_app_name_w = open("res/values/strings.xml", "w");


xml_app_name_data = f'''<?xml version="1.0" encoding="utf-8"?>
<resources>

    <string name="app_name">{app_name}</string>

</resources>
''';

xml_app_name_w.write(xml_app_name_data);


xml_app_name_w.close();

print("------ Done\n\n");








print("------ Making App styles with xml...\n\n");

xml_app_styles = open("res/values/styles.xml", "x");
xml_app_styles.close();

print("------ Done\n\n");


print("------ Writting App name with xml...\n\n");

xml_app_styles_w = open("res/values/styles.xml", "w");


xml_app_styles_data = '''<resources>

    <style name="AppTheme" parent="android:Theme.DeviceDefault.Light">
        <item name="android:statusBarColor">@android:color/black</item>
        <item name="android:windowActionBar">false</item>
        <item name="android:windowNoTitle">true</item>
    </style>

</resources>
''';

xml_app_styles_w.write(xml_app_styles_data);


xml_app_styles_w.close();

print("------ Done\n\n");





print ('------ Moving res into builds');


move_folder('res', 'build/app/src/main');


print ('------ Done');







print("------ Making App Manifest with xml...\n\n");

xml_app_manifest = open("build/app/src/main/AndroidManifest.xml", "x");
xml_app_manifest.close();

print("------ Done\n\n");


print("------ Writting App Manifest with xml...\n\n");

xml_app_manifest_w = open("build/app/src/main/AndroidManifest.xml", "w");


xml_app_manifest_data = f'''<?xml version="1.0" encoding="utf-8"?>
<manifest
    package="com.{p_name}.{p_name_l}"
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">
    <uses-permission android:name="android.permission.INTERNET" />
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/AppTheme"
        tools:ignore="GoogleAppIndexingWarning">
        <activity
            android:configChanges="orientation|screenSize"
            android:name="com.{p_name}.{p_name_l}.MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>''';

xml_app_manifest_w.write(xml_app_manifest_data);


xml_app_manifest_w.close();

print("------ Done\n\n");





print('------Switching to root dir');
print('Done');

print('Removing all un necessssary files');
delete_file('build/a.zip');
print('Done');



print("Checking all files in root Dir...\n\n");

os.system("dir");
os.system("dir build");
os.system("dir build/app");
os.system("dir build/app/src");
os.system("dir build/app/src/main"); 
os.system("dir build/app/src/main/assets");
os.system("dir build/app/src/main/java");
os.system("dir build/app/src/main/res");

print("Done\n\n");




print("-- Done\n\n");







print('Successfully Builded all the APK source files for Android Studio |/ now install Android studio and load this source project in it, Project builded inside the build directory , Status good and nicely finished :)');







# End 1 - ended by ghgltggamer at 22:17pm , same day , same location
# Remaining things :-
# App name
# App style info
# Then the apk build will be finished for emport in android studio



# Restarted at now from editting the icon setup at next day at 12:05pm , By the way tomorrow is my exam of mathematics :(( and i have not studied any thing yet , Still i am feeling good while writting this script 
# Continuation by ghgltggamer 
# Completed at 12:34pm same day and time and location
