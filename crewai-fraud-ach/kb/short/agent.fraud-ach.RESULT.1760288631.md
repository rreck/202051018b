```json
{
  "id": "d6bf4dedb3c69557",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288631,
  "host_pid": "9e6742732c60:1",
  "hash": "f9790f504964aad909cc077950c227a15a517808a78d56639cb787345a3098ac",
  "cid": "QmV1f9790f504964aad909cc077950c227a15a517808",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288631,
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
      "evaluated_at": 1760288631
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
  "sig": "e636c59bb7d9abab3d655e43d2ba5c10759b1321da95884f0ade4f30e991d578"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024765233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 33764742, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': 'feb1cc4bc40c71bc'}}}