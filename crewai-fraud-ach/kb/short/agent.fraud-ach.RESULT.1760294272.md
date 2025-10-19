```json
{
  "id": "3f81972e1bad493f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294272,
  "host_pid": "9e6742732c60:1",
  "hash": "2985e2aa184c8ff70e87487399a1ddae98fb88ea0c6677c4f4f8e7695420e35d",
  "cid": "QmV12985e2aa184c8ff70e87487399a1ddae98fb88ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294272,
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
      "evaluated_at": 1760294272
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
  "sig": "6e6a050899c5de71c75b7a704d864db9d91acf024d692c8d199176590849f36b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249175658
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 45060310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '6be9977bdc69f166'}}}