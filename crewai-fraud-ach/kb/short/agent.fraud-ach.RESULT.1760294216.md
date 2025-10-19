```json
{
  "id": "527c8cfc0d5bb0c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294216,
  "host_pid": "9e6742732c60:1",
  "hash": "8652d724400884d750a9bc32084cdfaf2a9ba956e1fa300c60fac35e6c048898",
  "cid": "QmV18652d724400884d750a9bc32084cdfaf2a9ba956",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294216,
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
      "evaluated_at": 1760294216
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
  "sig": "157ccc1dfdbaffdd932bc8cac72edfd17845128728f878dd54d63a00bfa3230f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271879965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 49631166, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '9c4837aa9a8e4a4a'}}}