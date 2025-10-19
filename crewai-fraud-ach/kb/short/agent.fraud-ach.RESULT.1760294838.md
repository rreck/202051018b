```json
{
  "id": "95e04faf889a0487",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294838,
  "host_pid": "9e6742732c60:1",
  "hash": "7cae59f370d2aa28accac678ec8365d0b71268405567b7cca6b6db7cce71f4b2",
  "cid": "QmV17cae59f370d2aa28accac678ec8365d0b7126840",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294838,
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
      "evaluated_at": 1760294838
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
  "sig": "2b214887a9c11c234870dae25c58d97484932863a4aa96ef221735b3e30c4005"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020141329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 115750250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285764, 'matching_hash': '1e11ace6091d7a38'}}}