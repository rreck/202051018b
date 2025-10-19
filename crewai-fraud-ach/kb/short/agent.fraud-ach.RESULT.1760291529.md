```json
{
  "id": "2980ab3e8bf908d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291529,
  "host_pid": "9e6742732c60:1",
  "hash": "52d9abdb79e7618f1c70816e9320a407608e1cb62fe296f8901427c36da4bd33",
  "cid": "QmV152d9abdb79e7618f1c70816e9320a407608e1cb6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291529,
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
      "evaluated_at": 1760291530
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
  "sig": "436a45e2bb86d903d87ae77772f8e81fc37e3f197324a7d6e301c526062a7785"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272056474
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': 'eb54a2a49d3a706d'}}}