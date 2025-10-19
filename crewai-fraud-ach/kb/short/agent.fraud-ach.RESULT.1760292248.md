```json
{
  "id": "1f28175a253f2ae5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292248,
  "host_pid": "9e6742732c60:1",
  "hash": "5956593c8bd46e093ce0b28750ad4d4b98d38ce9ff63bdc8dd207c001079610a",
  "cid": "QmV15956593c8bd46e093ce0b28750ad4d4b98d38ce9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292248,
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
      "evaluated_at": 1760292248
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
  "sig": "1dbf5b10a5ce418ded378cca3d83f66c487f7b40fabb5d18a58cc9739aee9a50"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020807792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 40288943, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285764, 'matching_hash': '8390351bce6e669b'}}}