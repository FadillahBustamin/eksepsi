def main():
    try:
        f = open("dataa.txt", "r")

        try:
            f.write("Pemrograman python")
        finally:
            f.close()
    except IOError:
        print("\nERROR: File tidak dapat " + "dibuka/ditulis")

if __name__ == "__main__":
    main()