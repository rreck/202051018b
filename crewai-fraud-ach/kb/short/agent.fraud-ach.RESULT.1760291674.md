```json
{
  "id": "b014848847d1c3dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291674,
  "host_pid": "9e6742732c60:1",
  "hash": "afa89e4ecc88b5f8f77ff89a0454ab15bec03efd8ef793bc533c9bd8a1b709b7",
  "cid": "QmV1afa89e4ecc88b5f8f77ff89a0454ab15bec03efd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291674,
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
      "evaluated_at": 1760291674
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
  "sig": "ee20b3b08ac4ccab2d9f3d389d9034e65cc860410ffa9b91fc31430a509b141d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273742232
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 37948860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285765, 'matching_hash': '98264f1e6b5ab805'}}}