```json
{
  "id": "768156194fba2c1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289720,
  "host_pid": "9e6742732c60:1",
  "hash": "990b6b3507e723d7fbc63d1532b74c609558d6d5cfbfe0359cfa07e98ffb21bc",
  "cid": "QmV1990b6b3507e723d7fbc63d1532b74c609558d6d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289720,
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
      "evaluated_at": 1760289720
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
  "sig": "c899c1ed92e6da9edcb60985ed4c7c72be47fea43ffdd7b8762af8c2a5b626e6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031758687
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 52894132, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285763, 'matching_hash': '8a33e153fff23185'}}}