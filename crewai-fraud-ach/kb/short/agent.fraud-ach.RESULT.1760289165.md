```json
{
  "id": "c39a96f149df7a20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289165,
  "host_pid": "9e6742732c60:1",
  "hash": "c1d1fb8deb4d9cdf85db109bd29f4016db11df38d6361669b8f1d4bf4b1d00dd",
  "cid": "QmV1c1d1fb8deb4d9cdf85db109bd29f4016db11df38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289165,
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
      "evaluated_at": 1760289165
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
  "sig": "de24ebad24e2e5ba2c3113d2ed34b782cb11491d8c04755346c314e0715f1642"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029964192
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 34891575, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285764, 'matching_hash': '3fa9c762fe00e5a2'}}}