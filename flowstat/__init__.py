import sys
import tensorflow as tf

def main():
    if len(sys.argv) < 2:
        print("Usage: flowstat <model path>")
        exit(1)
    
    model_path = sys.argv[1]
    interpreter = tf.lite.Interpreter(model_path)
    signature = interpreter.get_signature_runner()
    