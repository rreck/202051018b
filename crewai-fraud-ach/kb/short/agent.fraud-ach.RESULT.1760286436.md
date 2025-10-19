```json
{
  "id": "3a0024cb7f6b496b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286436,
  "host_pid": "9e6742732c60:1",
  "hash": "d17e129476e851eb4f9a05c8b70688eb82e37a9c084cf0164369ffb79a1f52c3",
  "cid": "QmV1d17e129476e851eb4f9a05c8b70688eb82e37a9c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286436,
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
      "evaluated_at": 1760286436
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
  "sig": "ffab76a28631c4bdd115db529cd9b73e22c62b5f9f6e1f1bf8222650a93724a3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000036177444
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285764, 'matching_hash': '11850a408d1201a4'}}}