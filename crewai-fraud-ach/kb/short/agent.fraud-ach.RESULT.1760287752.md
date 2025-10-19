```json
{
  "id": "993d78f92d897b6a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287752,
  "host_pid": "9e6742732c60:1",
  "hash": "c41e19310c94a873012aa37ea32c994b27dad4c83c8bfcf8a84520bd758ce878",
  "cid": "QmV1c41e19310c94a873012aa37ea32c994b27dad4c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287752,
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
      "evaluated_at": 1760287752
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
  "sig": "8aa02908807706cbe0ee269bcd392b70a24528fdb3579e3472a196cc098786c0"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 122105152914121
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 26545835, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285763, 'matching_hash': 'c85c50a0151bc705'}}}}}}