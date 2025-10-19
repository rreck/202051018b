```json
{
  "id": "6ac81bd2be0021fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287910,
  "host_pid": "9e6742732c60:1",
  "hash": "5b1b737daf882b2a0b92bcfb0855ae02190d7481a423a9ff772bbef54f548d85",
  "cid": "QmV15b1b737daf882b2a0b92bcfb0855ae02190d7481",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287910,
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
      "evaluated_at": 1760287910
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
  "sig": "ccf2240c2ae7a8849311516751d1b81c5bfec34c805011b49289bac08f87cdd0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}