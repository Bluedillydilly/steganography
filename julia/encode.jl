# Program to enoce an image with text using a least significant bit algorithm

function main()
    println("Welcome")
    println("Enter F for file input or enter anything else for command line input")
    if( readline(stdin) == "F" )
        fi_mode()
    else
        cli_mode()
    end
end

function fi_mode()
    println("Entered file input mode")
    println("Enter name of file")
    file_name = "encode.jl"
    println(file_name)
end

function cli_mode()
    println("Entered command line input mode")
    println("Enter text to encode into the image.")
end

function image_stuff()
    A = rand( 3, 10, 10 )
    img = colorview( RGB, A )

end

main()
