```json
{
  "id": "2af36e2e10df6c24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287702,
  "host_pid": "9e6742732c60:1",
  "hash": "3e9be7e9e4532cff574bc95718e07de2c8b09b9765f5404a1f1e9786e9ec6a8e",
  "cid": "QmV13e9be7e9e4532cff574bc95718e07de2c8b09b97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287702,
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
      "evaluated_at": 1760287702
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
  "sig": "b5440bc9fa13548b32ee0783e40a5a712184e40ea9e2e9b3a0b7fdf509257685"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 111000022318038
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 16592568, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285765, 'matching_hash': 'c47c52aff7a65053'}}}