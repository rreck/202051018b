```json
{
  "id": "2db5ba6a46c7b50a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294737,
  "host_pid": "9e6742732c60:1",
  "hash": "7fbdff4563c8fbe62b049aa9bd82a5b7ff5ce78dd4a33978b9200f57c419533d",
  "cid": "QmV17fbdff4563c8fbe62b049aa9bd82a5b7ff5ce78d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294737,
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
      "evaluated_at": 1760294737
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
  "sig": "2d013d6612342f13708f78cfe6a0bf053c1068680851f1d04579f6e3702ab259"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276764543
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 79704486, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285765, 'matching_hash': '861ebf9054cc2433'}}}