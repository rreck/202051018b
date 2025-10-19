```json
{
  "id": "5d05d5923e2b5dd1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294560,
  "host_pid": "9e6742732c60:1",
  "hash": "c5fd5c5ad85b75acf3ff4a365a28b41383124cc285e93c9964984d26d0ee1c28",
  "cid": "QmV1c5fd5c5ad85b75acf3ff4a365a28b41383124cc2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294560,
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
      "evaluated_at": 1760294560
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
  "sig": "8403c78682981451842015351cba0bcd39b8105ee3dee35dbd07f476ddaeba34"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245928241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 82067040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': '062a48cd408462a2'}}}}