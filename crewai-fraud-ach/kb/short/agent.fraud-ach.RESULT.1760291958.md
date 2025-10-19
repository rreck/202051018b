```json
{
  "id": "646c407fa997d8e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291958,
  "host_pid": "9e6742732c60:1",
  "hash": "4eb04a2e8d6b7ef75c4bb022fb09c65790ea5271e3792da4bb45c4eb2d3d7048",
  "cid": "QmV14eb04a2e8d6b7ef75c4bb022fb09c65790ea5271",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291958,
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
      "evaluated_at": 1760291958
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
  "sig": "44de1a292fcce390a54c836d2ac22c3c8e930ff32a5c4f91d6eaebd869baec8a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021151885
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 45792747, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285764, 'matching_hash': '925ef0ca9f93e495'}}}