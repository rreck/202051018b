```json
{
  "id": "eff2e9541664ad7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287220,
  "host_pid": "9e6742732c60:1",
  "hash": "9e2a6037c4c63451c7346ad1e0fc97a9c82239750f85b38655f174adc0c833a6",
  "cid": "QmV19e2a6037c4c63451c7346ad1e0fc97a9c8223975",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287220,
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
      "evaluated_at": 1760287220
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
  "sig": "62a0793c8c5373ee4ce62c335e8abcd5c5029ad5b9907d8c9161710da6fd345c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000024109289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 18167188, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285765, 'matching_hash': 'ac2c8f9ff893d8ff'}}}