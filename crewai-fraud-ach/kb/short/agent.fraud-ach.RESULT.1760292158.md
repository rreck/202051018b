```json
{
  "id": "1643b301ebafd337",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292158,
  "host_pid": "9e6742732c60:1",
  "hash": "3a1ad7be9bd445c430f748a1281b4ba688e53bb54af8e942bec308bbbd86c410",
  "cid": "QmV13a1ad7be9bd445c430f748a1281b4ba688e53bb5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292158,
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
      "evaluated_at": 1760292158
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
  "sig": "227511e9f0c5f1e2a6e059b5a97bc8230bedacb6aa68984858af5f9a39ff6565"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}