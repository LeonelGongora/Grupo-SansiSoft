output_schema = {
  "type": "object",
  "properties": {
    "json": {
      "type": "object",
      "properties": {
        "errors": {
          "type": "array",
          "items": {}
        },
        "data": {
          "type": "object",
          "properties": {
            "things": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "kind": {
                      "type": "string"
                    },
                    "data": {
                      "type": "object",
                      "properties": {
                        "subreddit_id": {
                          "type": "string"
                        },
                        "approved_at_utc": {
                          "type": "null"
                        },
                        "author_is_blocked": {
                          "type": "boolean"
                        },
                        "comment_type": {
                          "type": "null"
                        },
                        "edited": {
                          "type": "boolean"
                        },
                        "mod_reason_by": {
                          "type": "null"
                        },
                        "banned_by": {
                          "type": "null"
                        },
                        "ups": {
                          "type": "integer"
                        },
                        "num_reports": {
                          "type": "null"
                        },
                        "author_flair_type": {
                          "type": "string"
                        },
                        "total_awards_received": {
                          "type": "integer"
                        },
                        "subreddit": {
                          "type": "string"
                        },
                        "author_flair_template_id": {
                          "type": "null"
                        },
                        "likes": {
                          "type": "boolean"
                        },
                        "replies": {
                          "type": "string"
                        },
                        "user_reports": {
                          "type": "array",
                          "items": {}
                        },
                        "saved": {
                          "type": "boolean"
                        },
                        "id": {
                          "type": "string"
                        },
                        "banned_at_utc": {
                          "type": "null"
                        },
                        "mod_reason_title": {
                          "type": "null"
                        },
                        "gilded": {
                          "type": "integer"
                        },
                        "archived": {
                          "type": "boolean"
                        },
                        "collapsed_reason_code": {
                          "type": "null"
                        },
                        "no_follow": {
                          "type": "boolean"
                        },
                        "author": {
                          "type": "string"
                        },
                        "can_mod_post": {
                          "type": "boolean"
                        },
                        "created_utc": {
                          "type": "number"
                        },
                        "send_replies": {
                          "type": "boolean"
                        },
                        "parent_id": {
                          "type": "string"
                        },
                        "score": {
                          "type": "integer"
                        },
                        "author_fullname": {
                          "type": "string"
                        },
                        "report_reasons": {
                          "type": "null"
                        },
                        "approved_by": {
                          "type": "null"
                        },
                        "all_awardings": {
                          "type": "array",
                          "items": {}
                        },
                        "collapsed": {
                          "type": "boolean"
                        },
                        "body": {
                          "type": "string"
                        },
                        "awarders": {
                          "type": "array",
                          "items": {}
                        },
                        "top_awarded_type": {
                          "type": "null"
                        },
                        "author_flair_css_class": {
                          "type": "null"
                        },
                        "author_patreon_flair": {
                          "type": "boolean"
                        },
                        "downs": {
                          "type": "integer"
                        },
                        "author_flair_richtext": {
                          "type": "array",
                          "items": {}
                        },
                        "is_submitter": {
                          "type": "boolean"
                        },
                        "body_html": {
                          "type": "string"
                        },
                        "removal_reason": {
                          "type": "null"
                        },
                        "collapsed_reason": {
                          "type": "null"
                        },
                        "associated_award": {
                          "type": "null"
                        },
                        "stickied": {
                          "type": "boolean"
                        },
                        "author_premium": {
                          "type": "boolean"
                        },
                        "can_gild": {
                          "type": "boolean"
                        },
                        "gildings": {
                          "type": "object"
                        },
                        "unrepliable_reason": {
                          "type": "null"
                        },
                        "author_flair_text_color": {
                          "type": "null"
                        },
                        "score_hidden": {
                          "type": "boolean"
                        },
                        "permalink": {
                          "type": "string"
                        },
                        "subreddit_type": {
                          "type": "string"
                        },
                        "locked": {
                          "type": "boolean"
                        },
                        "name": {
                          "type": "string"
                        },
                        "created": {
                          "type": "number"
                        },
                        "author_flair_text": {
                          "type": "null"
                        },
                        "treatment_tags": {
                          "type": "array",
                          "items": {}
                        },
                        "rte_mode": {
                          "type": "string"
                        },
                        "link_id": {
                          "type": "string"
                        },
                        "subreddit_name_prefixed": {
                          "type": "string"
                        },
                        "controversiality": {
                          "type": "integer"
                        },
                        "author_flair_background_color": {
                          "type": "null"
                        },
                        "collapsed_because_crowd_control": {
                          "type": "null"
                        },
                        "mod_reports": {
                          "type": "array",
                          "items": {}
                        },
                        "mod_note": {
                          "type": "null"
                        },
                        "distinguished": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "subreddit_id",
                        "approved_at_utc",
                        "author_is_blocked",
                        "comment_type",
                        "edited",
                        "mod_reason_by",
                        "banned_by",
                        "ups",
                        "num_reports",
                        "author_flair_type",
                        "total_awards_received",
                        "subreddit",
                        "author_flair_template_id",
                        "likes",
                        "replies",
                        "user_reports",
                        "saved",
                        "id",
                        "banned_at_utc",
                        "mod_reason_title",
                        "gilded",
                        "archived",
                        "collapsed_reason_code",
                        "no_follow",
                        "author",
                        "can_mod_post",
                        "created_utc",
                        "send_replies",
                        "parent_id",
                        "score",
                        "author_fullname",
                        "report_reasons",
                        "approved_by",
                        "all_awardings",
                        "collapsed",
                        "body",
                        "awarders",
                        "top_awarded_type",
                        "author_flair_css_class",
                        "author_patreon_flair",
                        "downs",
                        "author_flair_richtext",
                        "is_submitter",
                        "body_html",
                        "removal_reason",
                        "collapsed_reason",
                        "associated_award",
                        "stickied",
                        "author_premium",
                        "can_gild",
                        "gildings",
                        "unrepliable_reason",
                        "author_flair_text_color",
                        "score_hidden",
                        "permalink",
                        "subreddit_type",
                        "locked",
                        "name",
                        "created",
                        "author_flair_text",
                        "treatment_tags",
                        "rte_mode",
                        "link_id",
                        "subreddit_name_prefixed",
                        "controversiality",
                        "author_flair_background_color",
                        "collapsed_because_crowd_control",
                        "mod_reports",
                        "mod_note",
                        "distinguished"
                      ]
                    }
                  },
                  "required": [
                    "kind",
                    "data"
                  ]
                }
              ]
            }
          },
          "required": [
            "things"
          ]
        }
      },
      "required": [
        "errors",
        "data"
      ]
    }
  },
  "required": [
    "json"
  ]
}