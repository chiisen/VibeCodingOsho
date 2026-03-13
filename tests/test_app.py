import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ["FLASK_SECRET_KEY"] = "test-secret-key-for-testing"


class TestApp:
    @pytest.fixture
    def client(self, app):
        return app.test_client()

    @pytest.fixture
    def app(self):
        from app import create_app

        application = create_app()
        application.config.update({"TESTING": True})
        return application

    def test_index_page(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_draw_endpoint_get(self, client):
        response = client.get("/draw")
        assert response.status_code in (200, 302)

    def test_result_without_draw(self, client):
        response = client.get("/result")
        assert response.status_code in (200, 302)

    def test_history_page(self, client):
        response = client.get("/history")
        assert response.status_code in (200, 302)

    def test_404_error(self, client):
        response = client.get("/nonexistent")
        assert response.status_code == 404
