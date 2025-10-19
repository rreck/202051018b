```json
{
  "id": "96a101b26f86606d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293424,
  "host_pid": "9e6742732c60:1",
  "hash": "4362fa958715ada8a3b332f51c96a7679ee0b5667f0a5fda89f9bd2ecdcd4813",
  "cid": "QmV14362fa958715ada8a3b332f51c96a7679ee0b566",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293424,
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
      "evaluated_at": 1760293424
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
  "sig": "e46e5f8d46cc01f26edf760edd843ad7598086b3c87892a7be47deac0a715c3a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030330812
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 44189036, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': '72f4f50a1c3c0bfc'}}}