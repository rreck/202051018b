```json
{
  "id": "eb1e0cd6b4f6b48a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288063,
  "host_pid": "9e6742732c60:1",
  "hash": "b2bc7ba5677914b97517dfd1bcabb218afc7e4bc02db8e7baf262aa96fb73924",
  "cid": "QmV1b2bc7ba5677914b97517dfd1bcabb218afc7e4bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288063,
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
      "evaluated_at": 1760288063
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
  "sig": "7454e533b74df0fd26304a847b02bf97a109d43ff5a39b7ec1342549756c98ff"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274578801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 14226840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285765, 'matching_hash': 'c58645b7bcecdbfd'}}}