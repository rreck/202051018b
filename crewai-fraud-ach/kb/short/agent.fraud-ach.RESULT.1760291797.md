```json
{
  "id": "7b7c05f987863583",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291797,
  "host_pid": "9e6742732c60:1",
  "hash": "cf3f755475ff2b946c4ec4824bc64a1381aa179ed18c97f0b8227eba49c9f51e",
  "cid": "QmV1cf3f755475ff2b946c4ec4824bc64a1381aa179e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291797,
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
      "evaluated_at": 1760291797
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
  "sig": "5378433483bc97d74aa1cf884dd8c7d6c1a0830a5978057f1770d45485ef67cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158176118
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 71963835, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285765, 'matching_hash': '15ef7d28467628fb'}}}