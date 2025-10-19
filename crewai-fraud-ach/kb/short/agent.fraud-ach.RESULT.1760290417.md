```json
{
  "id": "3da5134841d08e5b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290417,
  "host_pid": "9e6742732c60:1",
  "hash": "1c3b34d869a96731885afd96f865fad31ca3f2fb3ce784bb7e75c7187078ff7f",
  "cid": "QmV11c3b34d869a96731885afd96f865fad31ca3f2fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290417,
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
      "evaluated_at": 1760290417
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
  "sig": "6553e9325dd4c678dc379df3d5c9a843792850af76cedd3400034fbb3f541e5b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467386779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 37500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': 'cfffbd2ec30a8ce4'}}}