from io import BytesIO

from jawa.cf import ClassFile
from jawa.attributes.source_file import SourceFileAttribute


def test_sourcefile_read(loader):
    """
    Ensure we can read a SourceFileAttribute generated by javac.
    """
    cf = loader['HelloWorldDebug']
    source_file = cf.attributes.find_one(name='SourceFile')
    assert(source_file.source_file.value == 'HelloWorldDebug.java')


def test_sourcefile_write():
    """
    Ensure SourceFileAttribute can be written and read back.
    """
    cf_one = ClassFile.create(u'SourceFileTest')

    sfa = cf_one.attributes.create(SourceFileAttribute)
    sfa.source_file = cf_one.constants.create_utf8(u'SourceFileTest.java')

    fout = BytesIO()
    cf_one.save(fout)

    fin = BytesIO(fout.getvalue())
    cf_two = ClassFile(fin)

    source_file = cf_two.attributes.find_one(name=u'SourceFile')
    assert(source_file.source_file.value == u'SourceFileTest.java')
