import input 
import process 
import output 

def main():
    input_text = input
    output_text = process.process_text(input_text)
    output.write_output_text(output_text)
    # output(output_text)

if __name__ == '__main__':
    main()
