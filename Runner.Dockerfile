FROM debian

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN mkdir actions-runner && cd actions-runner \
    && curl -o actions-runner-linux-x64-2.314.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.314.1/actions-runner-linux-x64-2.314.1.tar.gz \
    && echo "6c726a118bbe02cd32e222f890e1e476567bf299353a96886ba75b423c1137b5  actions-runner-linux-x64-2.314.1.tar.gz" | shasum -a 256 -c \
    && tar xzf ./actions-runner-linux-x64-2.314.1.tar.gz

COPY config.py /app/config.py

WORKDIR /actions-runner
CMD ["./config.sh", "--url", "https://github.com/AndreyMetelkin85/test-automation-suite", "--git_token_runner", "$(python -c 'from config import git_token_runner; print(git_token_runner)')"]

# Запуск скрипта run.sh
CMD ["./run.sh"]
