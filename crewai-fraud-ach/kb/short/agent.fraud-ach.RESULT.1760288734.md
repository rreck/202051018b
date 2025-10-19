```json
{
  "id": "11a50bacb02f5bf3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288734,
  "host_pid": "9e6742732c60:1",
  "hash": "681e65f720baafd9db1700196a18890689d1601f2efb63efb20273a96acf8c76",
  "cid": "QmV1681e65f720baafd9db1700196a18890689d1601f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288734,
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
      "evaluated_at": 1760288734
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
  "sig": "c3c05fe3d8c92444cec0032e40b48b9432e4ccc2dd80986db98f390d63764115"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025839448
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 38599554, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285765, 'matching_hash': 'a0edb6bd92ae1076'}}}