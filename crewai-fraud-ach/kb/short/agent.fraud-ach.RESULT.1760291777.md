```json
{
  "id": "befde1dd113c1cbc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291777,
  "host_pid": "9e6742732c60:1",
  "hash": "c7461b7cd556e01850b1c995d4274e60538eb9e4d06023249b9eb39e9c0dea64",
  "cid": "QmV1c7461b7cd556e01850b1c995d4274e60538eb9e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291777,
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
      "evaluated_at": 1760291777
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
  "sig": "e1c14944394b32accff7ed2400e86bfb8fa90113b76f9e10f6043141534feac3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155093747
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 45750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': '733cbbfa8b499b66'}}}