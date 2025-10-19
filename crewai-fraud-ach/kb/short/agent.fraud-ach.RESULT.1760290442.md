```json
{
  "id": "dcb93d1fc4b9a335",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290442,
  "host_pid": "9e6742732c60:1",
  "hash": "242da682bd4a9077d9a57af8d4c83903842862fabb93912a8070d09ee0a06249",
  "cid": "QmV1242da682bd4a9077d9a57af8d4c83903842862fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290442,
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
      "evaluated_at": 1760290442
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
  "sig": "57b2fb8d8be98b3d36d88a24707caac8c681ce59698d0eb8d6963cd2d2ecd9a5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152525323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 55206600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285765, 'matching_hash': '867ad08c0d495d7b'}}}