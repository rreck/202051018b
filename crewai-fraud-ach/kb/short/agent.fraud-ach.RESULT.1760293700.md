```json
{
  "id": "d81c56ffb8c4b95c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293700,
  "host_pid": "9e6742732c60:1",
  "hash": "e00165e84adf5086470fe63fb78574202665e1af34897e646239a6926a45b016",
  "cid": "QmV1e00165e84adf5086470fe63fb78574202665e1af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293700,
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
      "evaluated_at": 1760293700
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
  "sig": "dc28ee36ee08e4a4a038efe2da7e9e15a64d610a639e22678946345b342f922f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035593386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 26735520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': '6253d15ae41563d2'}}}