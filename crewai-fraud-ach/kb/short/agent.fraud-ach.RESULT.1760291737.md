```json
{
  "id": "5ffd2eb7b3e946a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291737,
  "host_pid": "9e6742732c60:1",
  "hash": "1d874ebdda226ff892184f0c6dc887849629af41704aabc4f19a04c5191f11a7",
  "cid": "QmV11d874ebdda226ff892184f0c6dc887849629af41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291737,
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
      "evaluated_at": 1760291737
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
  "sig": "9a5c91efb1d26a9eee811f5f6c59d63643b96451a31999cd6072a7b47157e357"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026044300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 69944966, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': '19d391c08a2c00ab'}}}