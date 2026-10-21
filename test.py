import unittest

from release_readiness import missing_items, readiness_report


def ready_release():
    return {
        "feature": "Citizen service form status update",
        "owner": "Example product squad",
        "staging_environment": "staging.forms.example",
        "documentation": "Wiki page: status-update-release-notes",
        "audit_note": "Approval trail retained.",
        "code_reviewed": True,
        "tests_passing": True,
        "accessibility_checked": True,
        "security_checked": True,
    }


class ReleaseReadinessTests(unittest.TestCase):
    def test_ready_release_has_no_missing_items(self):
        self.assertEqual(missing_items(ready_release()), [])

    def test_missing_flag_is_reported(self):
        release = ready_release()
        release["security_checked"] = False
        self.assertIn("security_checked", missing_items(release))

    def test_report_marks_incomplete_release_not_ready(self):
        release = ready_release()
        release["documentation"] = ""
        self.assertIn("NOT_READY", readiness_report(release))


if __name__ == "__main__":
    unittest.main()
