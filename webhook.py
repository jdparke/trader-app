import hmac
from flask import request, Blueprint, jsonify, current_app
from git import Repo

webhook = Blueprint('webhook', __name__)

@webhook.route('/github', methods=['POST'])
def handle_github_hook():

  signature = request.headers.get('X-Hub-Signature')
  sha, signature = signature.split('=')

  secret = str.encode(current_app.config.get('GITHUB_SECRET'))

  #return jsonify({"secret":secret}), 200

  hashhex = hmac.new(secret, request.data, digestmod='sha1').hexdigest()
  global repo

  #return jsonify({"hashhex":hashhex},
  #               {"signature": signature},
  #              {"secret": secret},
  #               {"compare": hmac.compare_digest(hashhex, signature)}
  #              ), 200


  #if hmac.compare_digest(hashhex, signature):
  if 1==1:
    #return jsonify({"got here":repo}), 200

    repo = Repo(current_app.config.get('REPO_PATH'))

    origin = repo.remotes.origin

    #return jsonify({"got here":"got here"}), 200


    origin.pull('--rebase')

    commit = request.json['after'][0:6]
    print('Repository updated with commit {}'.format(commit))
  else:
    return jsonify({"else":"else"}), 200

  return jsonify({"repo":repo}), 200