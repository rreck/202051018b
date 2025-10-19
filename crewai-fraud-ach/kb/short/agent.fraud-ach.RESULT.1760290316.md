```json
{
  "id": "078f980d37056361",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290316,
  "host_pid": "9e6742732c60:1",
  "hash": "d6e5b9ee458996b5a68897d64d4de1923482befd5ba8967cec92a4cd94002624",
  "cid": "QmV1d6e5b9ee458996b5a68897d64d4de1923482befd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290316,
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
      "evaluated_at": 1760290316
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
  "sig": "dd8101dcf3f72380a394761fce8885e59ff609e97c85b4c8bc47a275a192bb2f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036272460
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 49679385, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': '9a32e66a4f8079bf'}}}