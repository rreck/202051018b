```json
{
  "id": "9ba8843fc0af26f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287383,
  "host_pid": "9e6742732c60:1",
  "hash": "d9b8145c8b5d87a3a1eb1d71214dd14f387a0024d936048627f5ef4a2f2bec8b",
  "cid": "QmV1d9b8145c8b5d87a3a1eb1d71214dd14f387a0024",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287383,
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
      "evaluated_at": 1760287383
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "65c61a4f7d8fc080ae11b1098b7f18b2163f2cbd52ce2173a0b1d748abf06128"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000249337095
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 23073154, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285765, 'matching_hash': '2aad7fe43cc5d34d'}}}