```json
{
  "id": "56a9a356422ad739",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285381,
  "host_pid": "9e6742732c60:1",
  "hash": "73dab2094989a7ebbca0929eca28221b0af778ef70ba11c219a9288ced290bb3",
  "cid": "QmV173dab2094989a7ebbca0929eca28221b0af778ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285381,
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
      "evaluated_at": 1760285381
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "cbfa1725084ae0d1812f14af2d5d247c80256caaf98d73b5ae7c655e78af1881"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16855760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}