```json
{
  "id": "a5a5ae1a375ca280",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289205,
  "host_pid": "9e6742732c60:1",
  "hash": "ffd5190e8c7ad6d8f4410f87e81ccfaa43ad15c281001ff6e068ac408918a604",
  "cid": "QmV1ffd5190e8c7ad6d8f4410f87e81ccfaa43ad15c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289205,
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
      "evaluated_at": 1760289205
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
  "sig": "9e86d3ba90680b8a80a082cf1fbb29629b3d85c3f4b23078fbe45ec8be1ad04d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241355402
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 18897908, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285765, 'matching_hash': '58524718dce63a85'}}}