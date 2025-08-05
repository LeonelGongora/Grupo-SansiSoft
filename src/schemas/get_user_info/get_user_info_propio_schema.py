schema_user_input_propio ={
  "type": "object",
  "properties": {
    "kind": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "is_employee": {
          "type": "boolean"
        },
        "has_visited_new_profile": {
          "type": "boolean"
        },
        "is_friend": {
          "type": "boolean"
        },
        "pref_no_profanity": {
          "type": "boolean"
        },
        "has_external_account": {
          "type": "boolean"
        },
        "pref_geopopular": {
          "type": "string"
        },
        "pref_show_trending": {
          "type": "boolean"
        },
        "subreddit": {
          "type": "object",
          "properties": {
            "default_set": {
              "type": "boolean"
            },
            "user_is_contributor": {
              "type": "boolean"
            },
            "banner_img": {
              "type": "string"
            },
            "allowed_media_in_comments": {
              "type": "array",
              "items": {}
            },
            "user_is_banned": {
              "type": "boolean"
            },
            "free_form_reports": {
              "type": "boolean"
            },
            "community_icon": {},
            "show_media": {
              "type": "boolean"
            },
            "icon_color": {
              "type": "string"
            },
            "user_is_muted": {},
            "display_name": {
              "type": "string"
            },
            "header_img": {},
            "title": {
              "type": "string"
            },
            "coins": {
              "type": "number"
            },
            "previous_names": {
              "type": "array",
              "items": {}
            },
            "over_18": {
              "type": "boolean"
            },
            "icon_size": {
              "type": "array",
              "items": {
                "type": "number"
              }
            },
            "primary_color": {
              "type": "string"
            },
            "icon_img": {
              "type": "string"
            },
            "description": {
              "type": "string"
            },
            "submit_link_label": {
              "type": "string"
            },
            "header_size": {},
            "restrict_posting": {
              "type": "boolean"
            },
            "restrict_commenting": {
              "type": "boolean"
            },
            "subscribers": {
              "type": "number"
            },
            "submit_text_label": {
              "type": "string"
            },
            "is_default_icon": {
              "type": "boolean"
            },
            "link_flair_position": {
              "type": "string"
            },
            "display_name_prefixed": {
              "type": "string"
            },
            "key_color": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "is_default_banner": {
              "type": "boolean"
            },
            "url": {
              "type": "string"
            },
            "quarantine": {
              "type": "boolean"
            },
            "banner_size": {},
            "user_is_moderator": {
              "type": "boolean"
            },
            "accept_followers": {
              "type": "boolean"
            },
            "public_description": {
              "type": "string"
            },
            "link_flair_enabled": {
              "type": "boolean"
            },
            "disable_contributor_requests": {
              "type": "boolean"
            },
            "subreddit_type": {
              "type": "string"
            },
            "user_is_subscriber": {
              "type": "boolean"
            }
          },
          "required": [
            "default_set",
            "user_is_contributor",
            "banner_img",
            "allowed_media_in_comments",
            "user_is_banned",
            "free_form_reports",
            "community_icon",
            "show_media",
            "icon_color",
            "user_is_muted",
            "display_name",
            "header_img",
            "title",
            "coins",
            "previous_names",
            "over_18",
            "icon_size",
            "primary_color",
            "icon_img",
            "description",
            "submit_link_label",
            "header_size",
            "restrict_posting",
            "restrict_commenting",
            "subscribers",
            "submit_text_label",
            "is_default_icon",
            "link_flair_position",
            "display_name_prefixed",
            "key_color",
            "name",
            "is_default_banner",
            "url",
            "quarantine",
            "banner_size",
            "user_is_moderator",
            "accept_followers",
            "public_description",
            "link_flair_enabled",
            "disable_contributor_requests",
            "subreddit_type",
            "user_is_subscriber"
          ]
        },
        "pref_show_presence": {
          "type": "boolean"
        },
        "snoovatar_img": {
          "type": "string"
        },
        "snoovatar_size": {},
        "gold_expiration": {},
        "has_gold_subscription": {
          "type": "boolean"
        },
        "is_sponsor": {
          "type": "boolean"
        },
        "num_friends": {
          "type": "number"
        },
        "features": {
          "type": "object",
          "properties": {
            "modmail_harassment_filter": {
              "type": "boolean"
            },
            "mod_service_mute_writes": {
              "type": "boolean"
            },
            "promoted_trend_blanks": {
              "type": "boolean"
            },
            "show_amp_link": {
              "type": "boolean"
            },
            "chat": {
              "type": "boolean"
            },
            "is_email_permission_required": {
              "type": "boolean"
            },
            "mod_awards": {
              "type": "boolean"
            },
            "expensive_coins_package": {
              "type": "boolean"
            },
            "chat_subreddit": {
              "type": "boolean"
            },
            "awards_on_streams": {
              "type": "boolean"
            },
            "mweb_xpromo_modal_listing_click_daily_dismissible_ios": {
              "type": "boolean"
            },
            "cookie_consent_banner": {
              "type": "boolean"
            },
            "modlog_copyright_removal": {
              "type": "boolean"
            },
            "show_nps_survey": {
              "type": "boolean"
            },
            "do_not_track": {
              "type": "boolean"
            },
            "images_in_comments": {
              "type": "boolean"
            },
            "mod_service_mute_reads": {
              "type": "boolean"
            },
            "chat_user_settings": {
              "type": "boolean"
            },
            "use_pref_account_deployment": {
              "type": "boolean"
            },
            "mweb_xpromo_interstitial_comments_ios": {
              "type": "boolean"
            },
            "mweb_xpromo_modal_listing_click_daily_dismissible_android": {
              "type": "boolean"
            },
            "premium_subscriptions_table": {
              "type": "boolean"
            },
            "mweb_xpromo_interstitial_comments_android": {
              "type": "boolean"
            },
            "crowd_control_for_post": {
              "type": "boolean"
            },
            "chat_group_rollout": {
              "type": "boolean"
            },
            "resized_styles_images": {
              "type": "boolean"
            },
            "noreferrer_to_noopener": {
              "type": "boolean"
            }
          },
          "required": [
            "modmail_harassment_filter",
            "mod_service_mute_writes",
            "promoted_trend_blanks",
            "show_amp_link",
            "chat",
            "is_email_permission_required",
            "mod_awards",
            "expensive_coins_package",
            "chat_subreddit",
            "awards_on_streams",
            "mweb_xpromo_modal_listing_click_daily_dismissible_ios",
            "cookie_consent_banner",
            "modlog_copyright_removal",
            "show_nps_survey",
            "do_not_track",
            "images_in_comments",
            "mod_service_mute_reads",
            "chat_user_settings",
            "use_pref_account_deployment",
            "mweb_xpromo_interstitial_comments_ios",
            "mweb_xpromo_modal_listing_click_daily_dismissible_android",
            "premium_subscriptions_table",
            "mweb_xpromo_interstitial_comments_android",
            "crowd_control_for_post",
            "chat_group_rollout",
            "resized_styles_images",
            "noreferrer_to_noopener"
          ]
        },
        "can_edit_name": {
          "type": "boolean"
        },
        "is_blocked": {
          "type": "boolean"
        },
        "verified": {
          "type": "boolean"
        },
        "new_modmail_exists": {
          "type": "boolean"
        },
        "pref_autoplay": {
          "type": "boolean"
        },
        "coins": {
          "type": "number"
        },
        "has_paypal_subscription": {
          "type": "boolean"
        },
        "has_subscribed_to_premium": {
          "type": "boolean"
        },
        "id": {
          "type": "string"
        },
        "can_create_subreddit": {
          "type": "boolean"
        },
        "over_18": {
          "type": "boolean"
        },
        "is_gold": {
          "type": "boolean"
        },
        "is_mod": {
          "type": "boolean"
        },
        "awarder_karma": {
          "type": "number"
        },
        "suspension_expiration_utc": {},
        "has_stripe_subscription": {
          "type": "boolean"
        },
        "is_suspended": {
          "type": "boolean"
        },
        "pref_video_autoplay": {
          "type": "boolean"
        },
        "in_chat": {
          "type": "boolean"
        },
        "has_android_subscription": {
          "type": "boolean"
        },
        "in_redesign_beta": {
          "type": "boolean"
        },
        "icon_img": {
          "type": "string"
        },
        "has_mod_mail": {
          "type": "boolean"
        },
        "pref_nightmode": {
          "type": "boolean"
        },
        "awardee_karma": {
          "type": "number"
        },
        "hide_from_robots": {
          "type": "boolean"
        },
        "password_set": {
          "type": "boolean"
        },
        "modhash": {},
        "link_karma": {
          "type": "number"
        },
        "force_password_reset": {
          "type": "boolean"
        },
        "total_karma": {
          "type": "number"
        },
        "inbox_count": {
          "type": "number"
        },
        "pref_top_karma_subreddits": {
          "type": "boolean"
        },
        "has_mail": {
          "type": "boolean"
        },
        "pref_show_snoovatar": {
          "type": "boolean"
        },
        "name": {
          "type": "string"
        },
        "pref_clickgadget": {
          "type": "number"
        },
        "created": {
          "type": "number"
        },
        "has_verified_email": {
          "type": "boolean"
        },
        "gold_creddits": {
          "type": "number"
        },
        "created_utc": {
          "type": "number"
        },
        "has_ios_subscription": {
          "type": "boolean"
        },
        "pref_show_twitter": {
          "type": "boolean"
        },
        "in_beta": {
          "type": "boolean"
        },
        "comment_karma": {
          "type": "number"
        },
        "accept_followers": {
          "type": "boolean"
        },
        "has_subscribed": {
          "type": "boolean"
        }
      },
      "required": [
        "is_employee",
        "has_visited_new_profile",
        "is_friend",
        "pref_no_profanity",
        "has_external_account",
        "pref_geopopular",
        "pref_show_trending",
        "subreddit",
        "pref_show_presence",
        "snoovatar_img",
        "snoovatar_size",
        "gold_expiration",
        "has_gold_subscription",
        "is_sponsor",
        "num_friends",
        "features",
        "can_edit_name",
        "is_blocked",
        "verified",
        "new_modmail_exists",
        "pref_autoplay",
        "coins",
        "has_paypal_subscription",
        "has_subscribed_to_premium",
        "id",
        "can_create_subreddit",
        "over_18",
        "is_gold",
        "is_mod",
        "awarder_karma",
        "suspension_expiration_utc",
        "has_stripe_subscription",
        "is_suspended",
        "pref_video_autoplay",
        "in_chat",
        "has_android_subscription",
        "in_redesign_beta",
        "icon_img",
        "has_mod_mail",
        "pref_nightmode",
        "awardee_karma",
        "hide_from_robots",
        "password_set",
        "modhash",
        "link_karma",
        "force_password_reset",
        "total_karma",
        "inbox_count",
        "pref_top_karma_subreddits",
        "has_mail",
        "pref_show_snoovatar",
        "name",
        "pref_clickgadget",
        "created",
        "has_verified_email",
        "gold_creddits",
        "created_utc",
        "has_ios_subscription",
        "pref_show_twitter",
        "in_beta",
        "comment_karma",
        "accept_followers",
        "has_subscribed"
      ]
    }
  },
  "required": [
    "kind",
    "data"
  ]
}