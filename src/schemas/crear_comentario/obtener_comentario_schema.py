obtener_comentario_schema = {
  "type": "object",
  "properties": {
    "kind": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "after": {
          "type": "null"
        },
        "dist": {
          "type": "integer"
        },
        "modhash": {
          "type": "null"
        },
        "geo_filter": {
          "type": "string"
        },
        "children": {
          "type": "array",
          "items": {
            
              "type": "object",
              "properties": {
                "kind": {
                  "type": "string"
                },
                "data": {
                  "type": "object",
                  "properties": {
                    "total_awards_received": {
                      "type": "integer"
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
                    "removal_reason": {
                      "type": "null"
                    },
                    "link_id": {
                      "type": "string"
                    },
                    "author_flair_template_id": {
                      "type": "null"
                    },
                    "likes": {
                      "type": "null"
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
                    "approved_by": {
                      "type": "null"
                    },
                    "mod_note": {
                      "type": "null"
                    },
                    "all_awardings": {
                      "type": "array",
                      "items": {}
                    },
                    "subreddit_id": {
                      "type": "string"
                    },
                    "body": {
                      "type": "string"
                    },
                    "awarders": {
                      "type": "array",
                      "items": {}
                    },
                    "author_flair_css_class": {
                      "type": "null"
                    },
                    "name": {
                      "type": "string"
                    },
                    "downs": {
                      "type": "integer"
                    },
                    "is_submitter": {
                      "type": "boolean"
                    },
                    "body_html": {
                      "type": "string"
                    },
                    "gildings": {
                      "type": "object"
                    },
                    "collapsed_reason": {
                      "type": "null"
                    },
                    "distinguished": {
                      "type": "null"
                    },
                    "associated_award": {
                      "type": "null"
                    },
                    "stickied": {
                      "type": "boolean"
                    },
                    "can_gild": {
                      "type": "boolean"
                    },
                    "top_awarded_type": {
                      "type": "null"
                    },
                    "unrepliable_reason": {
                      "type": "null"
                    },
                    "author_flair_text_color": {
                      "type": "string"
                    },
                    "score_hidden": {
                      "type": "boolean"
                    },
                    "permalink": {
                      "type": "string"
                    },
                    "num_reports": {
                      "type": "null"
                    },
                    "locked": {
                      "type": "boolean"
                    },
                    "report_reasons": {
                      "type": "null"
                    },
                    "created": {
                      "type": "number"
                    },
                    "subreddit": {
                      "type": "string"
                    },
                    "author_flair_text": {
                      "type": "null"
                    },
                    "treatment_tags": {
                      "type": "array",
                      "items": {}
                    },
                    "collapsed": {
                      "type": "boolean"
                    },
                    "subreddit_name_prefixed": {
                      "type": "string"
                    },
                    "controversiality": {
                      "type": "integer"
                    },
                    "author_flair_background_color": {
                      "type": "string"
                    },
                    "collapsed_because_crowd_control": {
                      "type": "null"
                    },
                    "mod_reports": {
                      "type": "array",
                      "items": {}
                    },
                    "subreddit_type": {
                      "type": "string"
                    },
                    "ups": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "total_awards_received",
                    "approved_at_utc",
                    "author_is_blocked",
                    "comment_type",
                    "edited",
                    "mod_reason_by",
                    "banned_by",
                    "removal_reason",
                    "link_id",
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
                    "approved_by",
                    "mod_note",
                    "all_awardings",
                    "subreddit_id",
                    "body",
                    "awarders",
                    "author_flair_css_class",
                    "name",
                    "downs",
                    "is_submitter",
                    "body_html",
                    "gildings",
                    "collapsed_reason",
                    "distinguished",
                    "associated_award",
                    "stickied",
                    "can_gild",
                    "top_awarded_type",
                    "unrepliable_reason",
                    "author_flair_text_color",
                    "score_hidden",
                    "permalink",
                    "num_reports",
                    "locked",
                    "report_reasons",
                    "created",
                    "subreddit",
                    "author_flair_text",
                    "treatment_tags",
                    "collapsed",
                    "subreddit_name_prefixed",
                    "controversiality",
                    "author_flair_background_color",
                    "collapsed_because_crowd_control",
                    "mod_reports",
                    "subreddit_type",
                    "ups"
                  ]
                }
              },
              "required": [
                "kind",
                "data"
              ]
            
        }
        },
        "before": {
          "type": "null"
        }
      },
      "required": [
        "after",
        "dist",
        "modhash",
        "geo_filter",
        "children",
        "before"
      ]
    }
  },
  "required": [
    "kind",
    "data"
  ]
}
