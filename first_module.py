
print('This always be run!')

def main():
    print("First Module's Name: {}".format(__name__))

if __name__ == '__main__':
    main()
else:
    print('Run From Import')
