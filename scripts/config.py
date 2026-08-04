from pathlib import Path

CONTENT_TYPES = {

    "posts": {

        "incoming": Path("drafts/incoming/posts"),
        "processed": Path("drafts/processed/posts"),
        "output": Path("_posts"),

        "layout": "post",

        "image_root": "/assets/images/posts",

        "list_fields": [
            "Authors",
            "Projects",
            "Tags"
        ],

        "required_columns": [
            "title",
            "authors",
            "projects",
            "season"
        ],

        "relationships": {
            "authors": "people",
            "projects": "projects"
        },

        "identifier": "title"
    },


    "people": {

        "incoming": Path("drafts/incoming/people"),
        "processed": Path("drafts/processed/people"),
        "output": Path("_people"),

        "layout": "person",

        "image_root": "/assets/images/people",
        
        "list_fields": [
            "Projects"
        ],

        "required_columns": [
            "name"
        ],

        "relationships": {
            "projects": "projects"

        },

        "identifier": "name",
        "body_field": "Biography"
    },


    "projects": {

        "incoming": Path("drafts/incoming/projects"),
        "processed": Path("drafts/processed/projects"),
        "output": Path("_projects"),

        "layout": "project",

        "image_root": "/assets/images/projects",

        "list_fields": [
            "Tags",
            "People"
        ],

        "required_columns": [
            "title",
            "people",
            "season"
        ],
        
        "relationships": {
            "people": "people"
        },

        "identifier": "title",
        "body_field": "Description"
    },


    "seasons": {

        "incoming": Path("drafts/incoming/seasons"),
        "processed": Path("drafts/processed/seasons"),
        "output": Path("_seasons"),

        "layout": "season",

        "image_root": "/assets/images/seasons",

        "required_columns": [
            "title",
            "code"
        ],

        "identifier": "title",
        "body_field": "Overview"
    }

}