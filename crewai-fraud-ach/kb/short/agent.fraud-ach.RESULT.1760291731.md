```json
{
  "id": "11127c49951d7d4b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291731,
  "host_pid": "9e6742732c60:1",
  "hash": "a91960731c76b9bdbac405f593f3074a6644b83b22dd1e01adf0f8252faee64f",
  "cid": "QmV1a91960731c76b9bdbac405f593f3074a6644b83b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291731,
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
      "evaluated_at": 1760291731
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
  "sig": "44dae725882c06c040a9742c2c712498569aa7c9d12293b3e7f4efc4fb67bebd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244267355
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 27365520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': '9a2cfa03d6a38585'}}}