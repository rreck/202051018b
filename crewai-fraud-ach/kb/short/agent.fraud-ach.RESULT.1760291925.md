```json
{
  "id": "57450c8a84ca91de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291925,
  "host_pid": "9e6742732c60:1",
  "hash": "93dc8c6b335c05eba95176d1ed162dadf15b34eea9eca27f74d5b5bcfe62a92c",
  "cid": "QmV193dc8c6b335c05eba95176d1ed162dadf15b34ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291925,
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
      "evaluated_at": 1760291925
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
  "sig": "102e15569a73c7b4ef5c7e938e8db95065975ef7c0242d78cae04b0db134a4b4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030256978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 262, 'threshold': 50, 'total_amount': 99443148, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 261, 'first_seen': 1760284979, 'matching_hash': 'a2caca18f22a9a3d'}}}