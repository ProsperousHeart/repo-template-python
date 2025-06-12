from src.tmp import hi_func

def test_hi_func():
    assert hi_func() == "hi"

# def test_hi_func_prints_hi(monkeypatch):
#     import io, sys
#     captured_output = io.StringIO()
#     monkeypatch.setattr(sys, 'stdout', captured_output)
#     hi_func()
#     sys.stdout = sys.__stdout__
#     assert captured_output.getvalue() == "Hi\n"
