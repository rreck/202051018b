```json
{
  "id": "b3f8566fbf1f3114",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294559,
  "host_pid": "9e6742732c60:1",
  "hash": "4373eaff420511cd54986be0de535ab3894d340567d5a63d04b8addb5bc166eb",
  "cid": "QmV14373eaff420511cd54986be0de535ab3894d3405",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294559,
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
      "evaluated_at": 1760294559
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
  "sig": "b9020192588e83e79ef3f2cd4d7aa8ac5449ebaeaafb6b9e1197a0d537b11312"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155376461
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 72213840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285765, 'matching_hash': 'ed3a1cd9da35e724'}}}}