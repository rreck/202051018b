```json
{
  "id": "6daf3e18bad03dce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293979,
  "host_pid": "9e6742732c60:1",
  "hash": "6f97ded59318935dd128b6412c611f3a0d8a8e6f45564635207aff3910dc1e4d",
  "cid": "QmV16f97ded59318935dd128b6412c611f3a0d8a8e6f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293979,
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
      "evaluated_at": 1760293979
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
  "sig": "5236f007ded2b3be62b1a167c471babdefdf187f823efcb48ee2c1df16b544c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020288859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 110982789, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': '0e6f21190a149d49'}}}