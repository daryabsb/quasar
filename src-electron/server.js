import { spawn } from "child_process";
import { join } from "node:path";

const backendPath = join(__dirname, "../../backend");

export const startDjangoServer = () => {
  console.log("backendPath", backendPath);
  const djangoBackend = spawn(
    join(backendPath, "\\venv\\Scripts\\python.exe"),

    [join(backendPath, "/manage.py"), "runserver", "--noreload"]
  );
  djangoBackend.stdout.on("data", (data) => {
    console.log(`stdout:\n${data}`);
  });
  djangoBackend.stderr.on("data", (data) => {
    console.log(`stderr: ${data}`);
  });
  djangoBackend.on("error", (error) => {
    console.log(`error: ${error.message}`);
  });
  djangoBackend.on("close", (code) => {
    console.log(`child process exited with code ${code}`);
  });
  djangoBackend.on("message", (message) => {
    console.log(`message:\n${message}`);
  });

  return djangoBackend;
};
