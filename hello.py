from prefect import flow


@flow
def main():
    print("Hello from hello-world!")


if __name__ == "__main__":
    main()
