```json
{
  "id": "01ea8f4f8cf656ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288379,
  "host_pid": "9e6742732c60:1",
  "hash": "496ffdc0238eb83686d8a6f2f2c09acc758a6897ec599aac77a056c49110e580",
  "cid": "QmV1496ffdc0238eb83686d8a6f2f2c09acc758a6897",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288379,
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
      "evaluated_at": 1760288379
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
  "sig": "56f5b41cdb2981b3a291b9c894fd9c6df90c280fafcdaebc71e64e21109fd308"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 28960568, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}