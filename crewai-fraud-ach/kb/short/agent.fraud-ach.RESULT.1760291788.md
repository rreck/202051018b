```json
{
  "id": "f3804cdd7c59b54d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291788,
  "host_pid": "9e6742732c60:1",
  "hash": "2429537ba405f13cc4467dc4a2768a4759af7398532608fad0b8b793ed30e5ee",
  "cid": "QmV12429537ba405f13cc4467dc4a2768a4759af7398",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291788,
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
      "evaluated_at": 1760291788
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
  "sig": "e0cb6a11baec394376e12d4e4b143e30f4926d28d6cfa789981de3b1a80d9243"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242647259
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 48140712, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': '186ae6e653ee56a6'}}}