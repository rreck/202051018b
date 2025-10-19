```json
{
  "id": "9b49517a30a5e4d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291940,
  "host_pid": "9e6742732c60:1",
  "hash": "cbdbc207f661ac32a05800da26e6d1ceb7ee92ddebae8f6bcb1e24d44c628b02",
  "cid": "QmV1cbdbc207f661ac32a05800da26e6d1ceb7ee92dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291940,
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
      "evaluated_at": 1760291940
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
  "sig": "900b2990733aa4148431ab13a3bcf09fd020b3639f5125b63dc5582b0f793a55"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 59194128, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}