```json
{
  "id": "056e51e97983bf2a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291702,
  "host_pid": "9e6742732c60:1",
  "hash": "c5e563c500cf9bfcf2cb8d4c1bf3875ea358b83feac457238dac946aa2f386eb",
  "cid": "QmV1c5e563c500cf9bfcf2cb8d4c1bf3875ea358b83f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291702,
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
      "evaluated_at": 1760291702
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
  "sig": "236930b79bb53c0921007c7cf817129e2bf238efbb0dd3ba9e3ea1278992b93c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246221982
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 42120691, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '5c0c0fe7ab2d6845'}}}