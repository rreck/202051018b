```json
{
  "id": "eb3a47a9a790ac7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292830,
  "host_pid": "9e6742732c60:1",
  "hash": "59c75d8c9d1e6c9f27315160c9ce892622e272ca704a7d34711b2c8ccdf3a981",
  "cid": "QmV159c75d8c9d1e6c9f27315160c9ce892622e272ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292830,
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
      "evaluated_at": 1760292830
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
  "sig": "64873bf594c2ae2788ac2098957b29acc345aa87632c8e2c2b1c21c4db2574c4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038197650
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 38741802, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '1b9150809eb731a5'}}}}