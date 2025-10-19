```json
{
  "id": "7923254ebf336480",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285733,
  "host_pid": "9e6742732c60:1",
  "hash": "1c49ef55dc015372600f5b3bdbf44f55918ab7eb8cfc6841d71ab32632243323",
  "cid": "QmV11c49ef55dc015372600f5b3bdbf44f55918ab7eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285733,
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
      "evaluated_at": 1760285733
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
  "sig": "0029e90c25bbe1a49bf327bed7898aa100be4d78f280d83a1146c8f6a926b280"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 31183156, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}