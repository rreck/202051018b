```json
{
  "id": "dcf83ea46830f975",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288797,
  "host_pid": "9e6742732c60:1",
  "hash": "c6ca6de61f8247f1a5ffe1a18835b586b24a92f2e8fd71863684af9f22a9aee8",
  "cid": "QmV1c6ca6de61f8247f1a5ffe1a18835b586b24a92f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288797,
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
      "evaluated_at": 1760288797
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
  "sig": "ee4957d79c093a83eecf48481d53e2de6abec94ef7c7bcbd3a6ed395c80fc307"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243187094
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 46633080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285764, 'matching_hash': '46900333a68fa7ba'}}}