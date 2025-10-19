```json
{
  "id": "b767a5880bbc3ec6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293983,
  "host_pid": "9e6742732c60:1",
  "hash": "2234778894dae8a7d1efb046bcf0f5e6d6e0f3de6bcd17916d4a516bb6c5762e",
  "cid": "QmV12234778894dae8a7d1efb046bcf0f5e6d6e0f3de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293983,
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
      "evaluated_at": 1760293983
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
  "sig": "9fcec08988b9393da6dddb91bfa0704bf6be0cb241b680fb3c4ebc0e98f34bfc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026783731
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 94218844, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': 'dea6d8bb62de6c67'}}}