```json
{
  "id": "8f6f8882bbc59bc3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288389,
  "host_pid": "9e6742732c60:1",
  "hash": "35caf9b856040deccd550d1ada6299f9daa8bd6395c2559305615ae43a14ed61",
  "cid": "QmV135caf9b856040deccd550d1ada6299f9daa8bd63",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288389,
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
      "evaluated_at": 1760288389
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
  "sig": "67edacc7d7fc355c0ba5ebd1f9f6f27141131f411fc37b2711a3d05f1851b506"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244267355
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 13833120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285763, 'matching_hash': '9a2cfa03d6a38585'}}}