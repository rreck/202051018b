```json
{
  "id": "681e6912aa2b6c10",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290893,
  "host_pid": "9e6742732c60:1",
  "hash": "f91f981144d65032311837b4f3c8f9bfc0c23b35141b838e78b5bea1c53f4b09",
  "cid": "QmV1f91f981144d65032311837b4f3c8f9bfc0c23b35",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290893,
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
      "evaluated_at": 1760290893
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
  "sig": "a19a961e51455eb6bbcd4cdca7cee8d9609b883bb47a4d780ffaca96ee8be74e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464768410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 75822804, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': '182aec6491bb83ab'}}}