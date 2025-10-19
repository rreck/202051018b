```json
{
  "id": "ab6309f27167a746",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292405,
  "host_pid": "9e6742732c60:1",
  "hash": "878ffd4d2ea56d797dd93b527054bd4d96997ab53034b9f6872a1822181e5b1e",
  "cid": "QmV1878ffd4d2ea56d797dd93b527054bd4d96997ab5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292405,
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
      "evaluated_at": 1760292405
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
  "sig": "9ee6b130e182df0e7c1b4dddf94283ceed4a22a78ff1906ff5c6e8fcda957857"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022338434
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 88632664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': '4c9dfd860457308a'}}}