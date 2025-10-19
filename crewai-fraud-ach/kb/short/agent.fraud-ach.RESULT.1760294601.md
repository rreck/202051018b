```json
{
  "id": "d07a19bfe52ce5fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294601,
  "host_pid": "9e6742732c60:1",
  "hash": "a3d1f444fff4b77f8d586c70321e1bcedf45f085995cc935f984781658d69cd5",
  "cid": "QmV1a3d1f444fff4b77f8d586c70321e1bcedf45f085",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294601,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760294601
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "404b8b0cc13540ef67b1fe2c0032fa5140082f4424dc8dbe9fa88bb582770012"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274521172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 25691082, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285764, 'matching_hash': 'cfb56b896e519b42'}}}