```json
{
  "id": "d7e47b9c9709242d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289897,
  "host_pid": "9e6742732c60:1",
  "hash": "aa23ab7a7b4c5f31af709c745110c1e445317bccf221ff7b5dc643ff9ec9c088",
  "cid": "QmV1aa23ab7a7b4c5f31af709c745110c1e445317bcc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289897,
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
      "evaluated_at": 1760289897
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
  "sig": "c0b2f969bf0021568600409f7310a58317b14d3037f368c1f21799c3c24dcc96"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029744317
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 37404896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285764, 'matching_hash': '20edeb4e835a4770'}}}