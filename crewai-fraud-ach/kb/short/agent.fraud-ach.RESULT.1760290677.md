```json
{
  "id": "b40f81aea7adc204",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290677,
  "host_pid": "9e6742732c60:1",
  "hash": "a49482811636c3bfc7e98fd213b173abeaa565dceaaebe1b5d4e9e6886b45f24",
  "cid": "QmV1a49482811636c3bfc7e98fd213b173abeaa565dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290677,
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
      "evaluated_at": 1760290677
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
  "sig": "4abcf71e49451c3ce6a114217bcd92edbab526f4d53f0ea79e0edb10398b7c4d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466004729
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 44500092, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285765, 'matching_hash': '1e26fed2c08b1370'}}}