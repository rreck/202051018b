```json
{
  "id": "cf6eb265ca41cf57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292177,
  "host_pid": "9e6742732c60:1",
  "hash": "31cc16781016f152de0080b043501be0935601a49916f458c4c174aa485a2383",
  "cid": "QmV131cc16781016f152de0080b043501be0935601a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292177,
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
      "evaluated_at": 1760292177
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
  "sig": "1233202978a3a7a680d2200ddf59a7f52b16721064949e65f739cb22868e3e1e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462075291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 60660288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': '75f7f0ceec197518'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5035466}}}