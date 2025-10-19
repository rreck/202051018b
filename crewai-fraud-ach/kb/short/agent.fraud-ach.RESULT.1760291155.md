```json
{
  "id": "def2dce7b0c2c3e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291155,
  "host_pid": "9e6742732c60:1",
  "hash": "a40bdfabed62fe26e72204ffec5c39f321fbcfd11535addcf23544715309aaad",
  "cid": "QmV1a40bdfabed62fe26e72204ffec5c39f321fbcfd1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291155,
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
      "evaluated_at": 1760291155
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
  "sig": "383209249dfbdc81f0ec183b2a17425ea7fe9f4a94a8c50b5663b6679e999f5c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027165618
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 43914024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': '01e7bf5fcf2bbeec'}}}