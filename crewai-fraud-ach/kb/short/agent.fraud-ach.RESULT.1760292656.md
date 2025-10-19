```json
{
  "id": "e021a277502ed924",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292656,
  "host_pid": "9e6742732c60:1",
  "hash": "28b67898130af2e0a67e077c73fed9623f217273bd54d98ee77ea37014023e05",
  "cid": "QmV128b67898130af2e0a67e077c73fed9623f217273",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292656,
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
      "evaluated_at": 1760292656
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
  "sig": "7a668822039704a10b0b85ac28fb17ee4429c95f6d45745cc15d002485cad069"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596811195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 44549686, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285765, 'matching_hash': '0f37bc2cbfa5aec6'}}}}