```json
{
  "id": "18e8649fd8f6e9f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290916,
  "host_pid": "9e6742732c60:1",
  "hash": "9b61fc08d2ac8fed683933f14c9778bb694ce3b4cb2e11abafdab241b4ce2db6",
  "cid": "QmV19b61fc08d2ac8fed683933f14c9778bb694ce3b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290916,
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
      "evaluated_at": 1760290916
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
  "sig": "39c607d2e467552ee4416026b26ae6022b121ed06d2fa7de63c2e336c6557c87"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023386962
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 16200000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285765, 'matching_hash': '663df3e5258a7a87'}}}