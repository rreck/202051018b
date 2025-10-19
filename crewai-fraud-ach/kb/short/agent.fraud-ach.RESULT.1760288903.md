```json
{
  "id": "b99e2f51d69d85d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288903,
  "host_pid": "9e6742732c60:1",
  "hash": "f07d0bf462f3f832b9ba1916dc56836bd04d241249a500002cc629682a8210c0",
  "cid": "QmV1f07d0bf462f3f832b9ba1916dc56836bd04d2412",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288903,
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
      "evaluated_at": 1760288903
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
  "sig": "f46d24cb5ed22f60d694004f0006ffc2f9b002f22d48417f837764f2f7727a09"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 34052536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}