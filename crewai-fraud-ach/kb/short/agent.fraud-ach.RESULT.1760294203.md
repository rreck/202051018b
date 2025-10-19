```json
{
  "id": "844f16296562a0db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294203,
  "host_pid": "9e6742732c60:1",
  "hash": "771f5acc9932bd3d7390b934235d65c7a8a172cf5ecb5bb16d1b759776ccb942",
  "cid": "QmV1771f5acc9932bd3d7390b934235d65c7a8a172cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294203,
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
      "evaluated_at": 1760294203
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
  "sig": "4c32974d57a0b0e2e9694b63e7eda4c384e899dfb4ebdefabfb3d2e395cd1d65"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025329406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 112848191, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285765, 'matching_hash': '4bb9b304f38123bb'}}}