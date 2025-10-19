```json
{
  "id": "0d4bc5bde0efce6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291496,
  "host_pid": "9e6742732c60:1",
  "hash": "a9eadde7b7176c036797f859bf69c091a85967fe84838a014ecdcd42add38a98",
  "cid": "QmV1a9eadde7b7176c036797f859bf69c091a85967fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291496,
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
      "evaluated_at": 1760291496
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
  "sig": "74a3c84e83ec0df2f9aa1397d29d427a524d88903c6d49db0023221b60c89eef"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037157781
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 36066976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285765, 'matching_hash': '7a7c344feaffaca5'}}}maly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.33, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8334426}}}