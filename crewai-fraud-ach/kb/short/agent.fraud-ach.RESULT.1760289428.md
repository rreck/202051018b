```json
{
  "id": "2e62acbdbc1d1218",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289428,
  "host_pid": "9e6742732c60:1",
  "hash": "862c7e8c64f99230d9d62b369e0b7e92f193e5d99666b4e6c9ea22157ae72a92",
  "cid": "QmV1862c7e8c64f99230d9d62b369e0b7e92f193e5d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289428,
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
      "evaluated_at": 1760289428
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
  "sig": "92bc2c74fb6f020fdb7c82863463689fa67a862c7fc5e05fc40bab49307faeeb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032341010
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 13121640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': 'f26a81694d784881'}}}