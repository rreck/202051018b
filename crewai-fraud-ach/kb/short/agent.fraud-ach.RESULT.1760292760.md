```json
{
  "id": "720337b42f86b5e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292760,
  "host_pid": "9e6742732c60:1",
  "hash": "9d027b5fa546ca5d449c8d76bd03a25bc3af06ea8fe1b2db5d9124c421d65ec7",
  "cid": "QmV19d027b5fa546ca5d449c8d76bd03a25bc3af06ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292760,
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
      "evaluated_at": 1760292760
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "fac8370b5fd09287394b2c63dcf058f15abd644bdb8894f68e8ed084e10edae5"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 121000249844926
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 1071734808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285765, 'matching_hash': '4f8c06dc9d4c212b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5253602}}}