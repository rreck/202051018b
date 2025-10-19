```json
{
  "id": "c57ac21edef712e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290706,
  "host_pid": "9e6742732c60:1",
  "hash": "4362c9659c207a0c44781ff3fcb55adf25759ffc1d9365e61ce8f1eebac14c49",
  "cid": "QmV14362c9659c207a0c44781ff3fcb55adf25759ffc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290706,
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
      "evaluated_at": 1760290706
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
  "sig": "759a719792981ab28d0cebfcb0efb1fbbc35a1bc3b5ab868a8c7709681dbf628"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030656036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 66302713, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760284979, 'matching_hash': '54d3add09935598e'}}}