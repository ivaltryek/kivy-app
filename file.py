from wrcloud.wrcloud import wrCloud
import json


class File:
    def run(self):
        try:
            api = wrCloud(api_key='5bef4651-dc35-42a3-aec4-179a0b0e8741')
            print('API connected!')
        except Exception as ex:
            print('Something went wrorng', str(ex))
        job = api.submit_job(filename="media-yoga.mp4", work_type=["annotated_media", "json"],
                             options={'heads': True, 'est_3d': True, 'resolution_scale': 2}, url=False)
        print(job)
        api.wait_for_processed_job(job, interval=10, timeout=900)
        status = api.get_job_status(job_id=job)
        print(status)
        while status != 'Processed':
            status = api.get_job_status(job_id=job)
            print(status)
        results = api.get_json_result_as_dict(job)
        print(json.dumps(results))


if __name__ == '__main__':
    file = File()
    file.run()
