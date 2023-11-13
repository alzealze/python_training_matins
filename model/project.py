from sys import maxsize


class Project:
    def __init__(self, ProjectName=None):
        self.id = None
        self.ProjectName = ProjectName

    def __repr__(self):
        return "%s" % (self.ProjectName)

    def __eq__(self, other):
        return self.ProjectName == other.ProjectName

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
