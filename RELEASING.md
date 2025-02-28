# Release checklist

- [ ] Get `main` to the appropriate code release state.
      [GitHub Actions](https://github.com/hugovk/norwegianblue/actions) should be
      running cleanly for all merges to `main`.
      [![GitHub Actions status](https://github.com/hugovk/norwegianblue/workflows/Test/badge.svg)](https://github.com/hugovk/norwegianblue/actions)

- [ ] Edit release draft, adjust text if needed:
      https://github.com/hugovk/norwegianblue/releases

- [ ] Check next tag is correct, amend if needed

- [ ] Publish release

- [ ] Check the tagged
      [GitHub Actions build](https://github.com/hugovk/norwegianblue/actions/workflows/deploy.yml)
      has deployed to [PyPI](https://pypi.org/project/norwegianblue/#history)

- [ ] Check installation:

```bash
pip3 uninstall -y norwegianblue && pip3 install -U norwegianblue && norwegianblue --version
```
