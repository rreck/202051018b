```json
{
  "id": "70e4488c1c05d554",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291459,
  "host_pid": "9e6742732c60:1",
  "hash": "baa1f5edd262f21196d4cd3c2354806e69bffb013c9e791ffc2411a601838308",
  "cid": "QmV1baa1f5edd262f21196d4cd3c2354806e69bffb01",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291459,
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
      "evaluated_at": 1760291459
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
  "sig": "900ecb42e5e3d8ea9c8d1ec3dbf73edf60922ed93e5e3bb3435b894909607829"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590866940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 74374300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285765, 'matching_hash': '66ff896a34603a53'}}}