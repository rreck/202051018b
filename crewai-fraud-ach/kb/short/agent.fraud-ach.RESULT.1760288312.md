```json
{
  "id": "9a3bba91e8fa9b14",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288312,
  "host_pid": "9e6742732c60:1",
  "hash": "ccef9e91c63553bd7b3f29d6f83a75d0a69574c01a70048fe00bcb2d77b299d4",
  "cid": "QmV1ccef9e91c63553bd7b3f29d6f83a75d0a69574c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288312,
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
      "evaluated_at": 1760288312
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
  "sig": "bc67af15983d4b3cfcbbe07b42bdc77c0e8ff2287882911935b13c8fe743ba00"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}