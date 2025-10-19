```json
{
  "id": "80ecca3b13621979",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294100,
  "host_pid": "9e6742732c60:1",
  "hash": "f422e99e8872130067fa34adf1ba9bfcb8403fc8591f4583f3fff143b74cc971",
  "cid": "QmV1f422e99e8872130067fa34adf1ba9bfcb8403fc8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294100,
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
      "evaluated_at": 1760294100
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
  "sig": "11642edda8ed1436c85744889d1d5b8a170fb0fd9821498aac2a75b504a7120a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 73515288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}