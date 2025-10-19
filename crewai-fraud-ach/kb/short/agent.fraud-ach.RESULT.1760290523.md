```json
{
  "id": "c1a25798f444d262",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290523,
  "host_pid": "9e6742732c60:1",
  "hash": "35e092e0498c7c5754b93283fdfb09d14d0800b9651c4b16cf5acee0c2246537",
  "cid": "QmV135e092e0498c7c5754b93283fdfb09d14d0800b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290523,
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
      "evaluated_at": 1760290523
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
  "sig": "c082fb53eb52bca652bf5871327dc7dfe4856f2c7794568041bd77162208367f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035927231
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 70514776, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285765, 'matching_hash': '0aeb814485d84e75'}}}