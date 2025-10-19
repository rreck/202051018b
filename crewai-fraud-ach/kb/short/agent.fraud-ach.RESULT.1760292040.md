```json
{
  "id": "e9454a1d62ad49d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292040,
  "host_pid": "9e6742732c60:1",
  "hash": "330431e7a275cbee76eeb5613ee7120044376c90feee8a41dae01236ecc799a2",
  "cid": "QmV1330431e7a275cbee76eeb5613ee7120044376c90",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292040,
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
      "evaluated_at": 1760292040
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
  "sig": "4360b139cec7a921db324f9c096b7aa3f1cf42529c1782cc69d39c40be11b8db"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469258561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 49091049, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': 'c5dbb685e09199e5'}}}