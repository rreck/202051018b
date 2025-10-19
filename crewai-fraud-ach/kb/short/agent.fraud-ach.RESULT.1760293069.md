```json
{
  "id": "9a9992f3504c7232",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293069,
  "host_pid": "9e6742732c60:1",
  "hash": "877c05fcecbbb19f529e8eba706d1af7eccdd0a5a7c0d82fc4b7b2edab88dbe1",
  "cid": "QmV1877c05fcecbbb19f529e8eba706d1af7eccdd0a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293069,
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
      "evaluated_at": 1760293069
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
  "sig": "2af0005b3057afc5a613ee71bdb27eac5cb4cc9bad1c05faedbed66c8bc441ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024088542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 13697065, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': '45759aa393537ed9'}}}