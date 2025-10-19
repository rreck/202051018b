```json
{
  "id": "ca5fbff78497351c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294390,
  "host_pid": "9e6742732c60:1",
  "hash": "4616d2ee976f443d0a4999628c53a52a970f19c70371f0c961f333259f5c6472",
  "cid": "QmV14616d2ee976f443d0a4999628c53a52a970f19c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294390,
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
      "evaluated_at": 1760294390
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
  "sig": "70e4c94eff204f8658f545d2d6f97d28744fcf9786d5e4374e79c49953dec69e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467383207
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 60215301, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': 'cf3979d2ed99750b'}}}}