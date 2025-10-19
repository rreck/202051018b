```json
{
  "id": "53ed0b3b8a9a453a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292461,
  "host_pid": "9e6742732c60:1",
  "hash": "47b005bfa26a6e25121fd0d8040aae7ded7747ba413807291e54b3e6bd391103",
  "cid": "QmV147b005bfa26a6e25121fd0d8040aae7ded7747ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292461,
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
      "evaluated_at": 1760292461
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
  "sig": "d04f747c429316f2c3a3e41eb7fe4c70b62f6dd80d81fabe9692e986ed2974b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468629827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 17503596, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': 'f998250ed7d87b2f'}}}