```json
{
  "id": "8625e413eab01abf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288563,
  "host_pid": "9e6742732c60:1",
  "hash": "4cb783db75716a64b52a0dbbfc85a892561e265697930db1d8ec9e5ab5dd95e3",
  "cid": "QmV14cb783db75716a64b52a0dbbfc85a892561e2656",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288563,
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
      "evaluated_at": 1760288563
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
  "sig": "edf391d88fd81063c21f8daef6e03d5e8cdd742a86d9fde7e85ac7fcf3fdec70"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245693870
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 24948109, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285763, 'matching_hash': '3f6bcdf181d34e46'}}}