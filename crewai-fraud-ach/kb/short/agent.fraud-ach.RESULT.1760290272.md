```json
{
  "id": "f8c1e4e64aef2825",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290272,
  "host_pid": "9e6742732c60:1",
  "hash": "ce4260aa1a7d4d74db45e7fabf3421a11d3631f310f6e55e68127ed81e80ca8d",
  "cid": "QmV1ce4260aa1a7d4d74db45e7fabf3421a11d3631f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290272,
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
      "evaluated_at": 1760290272
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
  "sig": "1ae892d2f401ae83964d0058f3bab9be385dbd0c587eea66de486824a6727a5d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153135421
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 55718856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': '4394c86a949e27d6'}}}