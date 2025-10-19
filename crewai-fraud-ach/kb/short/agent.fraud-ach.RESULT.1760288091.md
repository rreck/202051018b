```json
{
  "id": "abf5e1892203d3c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288091,
  "host_pid": "9e6742732c60:1",
  "hash": "052c44eddcfad77239b4caf550cbf1ae0032256a43251c685bef624aa66b0eae",
  "cid": "QmV1052c44eddcfad77239b4caf550cbf1ae0032256a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288091,
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
      "evaluated_at": 1760288091
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
  "sig": "e7409830596eabdceee9e5809b5299ed6aa2d6de745f794d58b57adc695b1fde"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027918613
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285764, 'matching_hash': 'c11d1385920c0a28'}}}