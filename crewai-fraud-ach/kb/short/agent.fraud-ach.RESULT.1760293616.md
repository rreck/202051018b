```json
{
  "id": "b67d58b67502c92c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293616,
  "host_pid": "9e6742732c60:1",
  "hash": "845c254ca95dd9ca957f33de3cd2c50d7db95b27865b4ea4a78d52a80d7d8ba2",
  "cid": "QmV1845c254ca95dd9ca957f33de3cd2c50d7db95b27",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293616,
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
      "evaluated_at": 1760293616
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
  "sig": "8452564efc8d959fa45fa184c9ed53355f04d3ec072590d494bf1133d97441db"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039514582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 70769382, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': 'c5d30db04a2c4cc4'}}}