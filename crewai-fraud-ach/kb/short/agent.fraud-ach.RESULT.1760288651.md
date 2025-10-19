```json
{
  "id": "9c5f3808b51133d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288651,
  "host_pid": "9e6742732c60:1",
  "hash": "46e68fa2206ad1a431ecf16c2d767486d9dda5319f08c05bfa97764eeb5b9e52",
  "cid": "QmV146e68fa2206ad1a431ecf16c2d767486d9dda531",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288651,
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
      "evaluated_at": 1760288651
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
  "sig": "e1cbc6d663dad66bf8bd2846fad97fa57030352a2175ea14ac8fb61b3f7677da"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462461467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 36970100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285763, 'matching_hash': '257546013422e30a'}}}