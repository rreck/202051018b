```json
{
  "id": "cee41af73a82ac1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294233,
  "host_pid": "9e6742732c60:1",
  "hash": "3662a32fce4c3c696a4a54f7a5b60385ba3759a6d8eb7b99c26c3d0dacbad70c",
  "cid": "QmV13662a32fce4c3c696a4a54f7a5b60385ba3759a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294233,
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
      "evaluated_at": 1760294233
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
  "sig": "91ac1c7f912c4a8aadddb87310c9786122fb42cd487ce69855548721e9079e23"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272525723
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 21451248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '7f6b158faad48b99'}}}}