```json
{
  "id": "1cb6a92df1d2e029",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288665,
  "host_pid": "9e6742732c60:1",
  "hash": "e3e60c03f8ca39f0feb0202528d69dae8a11518831adc0702cde76b0a82380dd",
  "cid": "QmV1e3e60c03f8ca39f0feb0202528d69dae8a115188",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288665,
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
      "evaluated_at": 1760288665
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
  "sig": "37f7d0a72505c65e7440c62a1a74230a44b855f16a9b2370e9bd9c4565d78240"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021053905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 25447000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285764, 'matching_hash': '608646e34fdf4d5c'}}}