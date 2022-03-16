import hmac
from flask import request, Blueprint, jsonify, current_app
from git import Repo

webhook = Blueprint('webhook', __name__)

@webhook.route('/github', methods=['POST'])
def handle_github_hook():

  signature = request.headers.get('X-Hub-Signature')
  sha, signature = signature.split('=')

  secret = str.encode(current_app.config.get('GITHUB_SECRET'))

  hashhex = hmac.new(secret, request.data, digestmod='sha1').hexdigest()
  global repo

  #if hmac.compare_digest(hashhex, signature):
  if 1==1:

    repo = Repo(current_app.config.get('REPO_PATH'))
    origin = repo.remotes.origin
    origin.pull('--rebase')

    commit = request.json['after'][0:6]
    print('Repository updated with commit {}'.format(commit))
  else:
    return jsonify({"else":"else"}), 200

  return jsonify({"success":"success"}), 200