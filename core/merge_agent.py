class MergeAgent:

    def merge(self, task_outputs):

        report = {
            "success": True,
            "issues": []
        }

        generated_files = []

        for task_name, output in task_outputs.items():

            if not output:

                report["success"] = False

                report["issues"].append(
                    f"{task_name} produced no output"
                )

                continue

            generated_files.append(task_name)

        report["generated_files"] = generated_files

        return report