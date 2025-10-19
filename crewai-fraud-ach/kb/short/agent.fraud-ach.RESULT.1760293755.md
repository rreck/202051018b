```json
{
  "id": "6f4c73b63be58899",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293755,
  "host_pid": "9e6742732c60:1",
  "hash": "ae2702157792d2e9895f2c6acf4068e0b4cb0b5e164705350fffdd16799b58d6",
  "cid": "QmV1ae2702157792d2e9895f2c6acf4068e0b4cb0b5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293755,
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
      "evaluated_at": 1760293755
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
  "sig": "c910b5517e0e59d168b9bf26c8334ecd2bf70e7a7b4d4054411132c4690f48ed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247065619
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 89970075, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '73a93f9011d99735'}}}}