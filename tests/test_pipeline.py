from traffic_ai.integration.pipeline import PipelineController


def test_pipeline():

    pipe = PipelineController()

    pipe.start()

    print(pipe.status())

    pipe.stop()

    print(pipe.status())


if __name__ == "__main__":

    test_pipeline()