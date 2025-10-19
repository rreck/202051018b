```json
{
  "id": "ce35ca7d9c5d9cfd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291450,
  "host_pid": "9e6742732c60:1",
  "hash": "833fca2934c670221d0520434cb89bd8efdd57974c74d7f3258ec3d6c7801c9f",
  "cid": "QmV1833fca2934c670221d0520434cb89bd8efdd5797",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291450,
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
      "evaluated_at": 1760291450
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
  "sig": "5b20e25a672b61f5b345d2bc9f96c3f93ce2b530245eb45bd5c751c8cf6f2aa7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249454336
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 25989075, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '6b4cd9d1923f5d4e'}}}