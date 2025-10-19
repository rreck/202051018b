```json
{
  "id": "a47496a837119a3c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289514,
  "host_pid": "9e6742732c60:1",
  "hash": "50751dcae33a769c262a29929d224bd0eb8f94a7ccf080b21060a3772a496b6a",
  "cid": "QmV150751dcae33a769c262a29929d224bd0eb8f94a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289514,
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
      "evaluated_at": 1760289514
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
  "sig": "74445388bcc081614ddfd556cca3a5b45f49fd1326650ac140237a32e561e476"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273461392
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 44586500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285765, 'matching_hash': 'ee78248c8d3d65fe'}}}