```json
{
  "id": "043736cceb466096",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293211,
  "host_pid": "9e6742732c60:1",
  "hash": "df0d8b77e3f1252ae8eaf9b0273650b3aaa5238874ae347979e3f70a84a17332",
  "cid": "QmV1df0d8b77e3f1252ae8eaf9b0273650b3aaa52388",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293211,
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
      "evaluated_at": 1760293211
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
  "sig": "5424cdacc7bd4c7bc47c6631447da2c2368db501a9d05b00697144b3c85d707a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029518652
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 16274700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': 'e772ab4f6c2a0903'}}}