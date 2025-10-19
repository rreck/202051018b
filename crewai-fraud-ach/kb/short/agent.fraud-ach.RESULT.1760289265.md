```json
{
  "id": "66755981d29b7d63",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289265,
  "host_pid": "9e6742732c60:1",
  "hash": "1175d4b64dd50785114435ca3f8c0b467e5965d41e12fb20b2984c8276cd4346",
  "cid": "QmV11175d4b64dd50785114435ca3f8c0b467e5965d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289265,
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
      "evaluated_at": 1760289265
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
  "sig": "412a1768f9c7cf9e4d1dc6d2ac59a0849171166dcf422f4d531e71a3fac58913"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469927048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 35154914, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': '982ed2d64f96a5b2'}}}