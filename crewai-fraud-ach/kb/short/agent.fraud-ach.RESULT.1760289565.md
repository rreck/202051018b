```json
{
  "id": "7d914db86322387d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289565,
  "host_pid": "9e6742732c60:1",
  "hash": "069fef3db84339a1e7dfc6a03cd845dd2c1f4955dd81cff1695aee2adf9cf64e",
  "cid": "QmV1069fef3db84339a1e7dfc6a03cd845dd2c1f4955",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289565,
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
      "evaluated_at": 1760289565
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
  "sig": "26c5d1fb136d6889045ba1c2b06743e240d77abeb1c6e1345c5fc6b8e753630e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027703590
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 45701331, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': '3a097b663e3dde58'}}}