```json
{
  "id": "e989a35721a70e03",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293004,
  "host_pid": "9e6742732c60:1",
  "hash": "fb1c8ab11aabb4ac36947ecc7d8538fb71c89fd1b733526ea4604e1c03dede9a",
  "cid": "QmV1fb1c8ab11aabb4ac36947ecc7d8538fb71c89fd1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293004,
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
      "evaluated_at": 1760293004
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
  "sig": "d839d1fd8ee45de08727b336f9d3a381d85c38618b9eea5116c29e4927c28b11"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027607406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 23155319, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285765, 'matching_hash': '504131d6dff02852'}}}