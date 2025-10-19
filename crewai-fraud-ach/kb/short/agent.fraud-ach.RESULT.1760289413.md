```json
{
  "id": "30e0c196def36203",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289413,
  "host_pid": "9e6742732c60:1",
  "hash": "9da2882b06d8672922cf8c5b459ae21aed76babcb6104a3b6733c8a995965fdc",
  "cid": "QmV19da2882b06d8672922cf8c5b459ae21aed76babc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289413,
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
      "evaluated_at": 1760289413
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
  "sig": "122ebf7b314332e5e91e504777a70720467e93ee70fe75815dac4ca84f805991"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 38826256, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}