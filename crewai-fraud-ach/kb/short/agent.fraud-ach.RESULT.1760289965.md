```json
{
  "id": "dde9b2a538e0f13c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289965,
  "host_pid": "9e6742732c60:1",
  "hash": "4a4a51aa826317c1cbf95c14c3f6be3ca5b4cc13b6ea5295d870aa8f7476fd1c",
  "cid": "QmV14a4a51aa826317c1cbf95c14c3f6be3ca5b4cc13",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289965,
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
      "evaluated_at": 1760289965
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
  "sig": "76cd97e66e7c61ff23e2e009b08891a9c15c2db1cf1aaff88cc9b1d94d2cf218"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154786749
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 60602838, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': '09892425b2f11015'}}}