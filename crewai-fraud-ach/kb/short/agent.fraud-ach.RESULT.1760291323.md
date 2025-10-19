```json
{
  "id": "1bbdcedcdd27b55a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291323,
  "host_pid": "9e6742732c60:1",
  "hash": "b4a050b3ba71c4d7e75dfe8cc93ce3021d382000bb73dff7ea9d74d627113c62",
  "cid": "QmV1b4a050b3ba71c4d7e75dfe8cc93ce3021d382000",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291323,
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
      "evaluated_at": 1760291323
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
  "sig": "1eaef49864dcbf76bc34a39c6338d967c7c3aa1cc6840d716ea4aa0c9ca3d1d8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154969717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 248, 'threshold': 50, 'total_amount': 98862224, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 247, 'first_seen': 1760284979, 'matching_hash': '5065063b494c04f4'}}}