```json
{
  "id": "5b7b19358d25d21a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292250,
  "host_pid": "9e6742732c60:1",
  "hash": "b49ff2b36a8ae7df07ad242a9558e6c5b75808c799b4a075e6675686eb533686",
  "cid": "QmV1b49ff2b36a8ae7df07ad242a9558e6c5b75808c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292250,
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
      "evaluated_at": 1760292250
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
  "sig": "df19ee6c0642e23dcfc0ce68a293d0af057812b7050d39ca120ac0b48465041d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025341515
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 48490092, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285765, 'matching_hash': '76c6a410184ad94b'}}}