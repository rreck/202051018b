```json
{
  "id": "3c140c7a9ab6cbd5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288059,
  "host_pid": "9e6742732c60:1",
  "hash": "12bd95b3de2ad34134bfab454230aae3490ae37815f5697fdec9ec599ec77f39",
  "cid": "QmV112bd95b3de2ad34134bfab454230aae3490ae378",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288059,
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
      "evaluated_at": 1760288059
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
  "sig": "6fe938926abe5c3a0c79649fd65fa039b4d6972ea6a75d87bdd6da576e24cc8f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462125361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 14192901, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285764, 'matching_hash': '410e2c6110d1d339'}}}