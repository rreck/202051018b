```json
{
  "id": "db926905333ca0e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288727,
  "host_pid": "9e6742732c60:1",
  "hash": "eced707ef2694d773657097aa52b2f32e6dcb22ea0a4599657f8602a3945de8d",
  "cid": "QmV1eced707ef2694d773657097aa52b2f32e6dcb22e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288727,
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
      "evaluated_at": 1760288727
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
  "sig": "b87958f44610f2d26c09a78b7030fcee8e41afdf65b2fe03309423142f17b4d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155364313
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 39404130, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285763, 'matching_hash': 'ab592f5d42fe5ec0'}}}