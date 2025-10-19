```json
{
  "id": "92803f5a70f820d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291847,
  "host_pid": "9e6742732c60:1",
  "hash": "b1a23dd6eaf79e4a20943c20f7833ec173b6c944ff1ed9fedf98dffa91179124",
  "cid": "QmV1b1a23dd6eaf79e4a20943c20f7833ec173b6c944",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291847,
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
      "evaluated_at": 1760291847
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
  "sig": "c08e81939bd536a4af815174b99fef434433ce604af0a62cd7bd2ee93cd3345e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035733360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 60400944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285765, 'matching_hash': '19d9911872be19af'}}}