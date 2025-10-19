```json
{
  "id": "fffec9dffd645a38",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288268,
  "host_pid": "9e6742732c60:1",
  "hash": "03746fc683726b18a66ecad0a7710bea237f8b0d201bfa14ee2930100b4afaa3",
  "cid": "QmV103746fc683726b18a66ecad0a7710bea237f8b0d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288268,
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
      "evaluated_at": 1760288268
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
  "sig": "945d43632c4e40741561f6522b934490ed5aace1261319775013905fb48c2311"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461386979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 29889288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285764, 'matching_hash': '1569de4be841c048'}}}