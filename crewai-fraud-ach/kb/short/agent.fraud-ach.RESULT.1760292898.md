```json
{
  "id": "b39278cf43854881",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292898,
  "host_pid": "9e6742732c60:1",
  "hash": "0223bfe05f6509dd36703a25ad88eb03472e7ddc1e3e8a062b0b48bd7a8f4126",
  "cid": "QmV10223bfe05f6509dd36703a25ad88eb03472e7ddc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292898,
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
      "evaluated_at": 1760292898
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
  "sig": "e01334036d968113bdccd059f2abd9103f9cc8dcdda9f63dfb5b12079bb166a5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598290210
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 13261869, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285765, 'matching_hash': '255d3759171e1aec'}}}