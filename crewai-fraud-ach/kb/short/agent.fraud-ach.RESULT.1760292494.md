```json
{
  "id": "d6702186d08589ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292494,
  "host_pid": "9e6742732c60:1",
  "hash": "1874b8990ef01d84ac75420a38cf081081c9b1f6df35a53fd0868af1ae772e09",
  "cid": "QmV11874b8990ef01d84ac75420a38cf081081c9b1f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292494,
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
      "evaluated_at": 1760292494
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
  "sig": "4fa55c1648dcfd9dc4df583f2cae839a35ae07ef3c07bcf5a76be24a32baf599"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591682020
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 57909995, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': '594333c81206e179'}}}