```json
{
  "id": "c7a6c8a55ff413c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290943,
  "host_pid": "9e6742732c60:1",
  "hash": "16c14da33af0ca60e3fe15255faa72af689064f5cb4d5ac73fd08497de1da6a7",
  "cid": "QmV116c14da33af0ca60e3fe15255faa72af689064f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290943,
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
      "evaluated_at": 1760290943
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
  "sig": "634731ada36ab456506aabc116b9fd820bee8f4dad220a079e15f828e7723fbf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034056272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 22530186, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': 'aae4e2a94575911d'}}}