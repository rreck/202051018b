```json
{
  "id": "09b3406c93d80f75",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291365,
  "host_pid": "9e6742732c60:1",
  "hash": "fe60d0e1267257c7fd3286190a8a44cd33abeb00da21c05dfa5a280fd8d061b7",
  "cid": "QmV1fe60d0e1267257c7fd3286190a8a44cd33abeb00",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291365,
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
      "evaluated_at": 1760291365
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
  "sig": "fe813e20ed4e4a78316ddc6e788750f92c1b0bf88a7f6549a88f09df1b7fa4de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023458666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 249, 'threshold': 50, 'total_amount': 101605197, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 248, 'first_seen': 1760284979, 'matching_hash': 'a7fb9dc83800d725'}}}