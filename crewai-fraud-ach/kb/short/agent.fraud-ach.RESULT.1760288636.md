```json
{
  "id": "da74d5d094878d20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288636,
  "host_pid": "9e6742732c60:1",
  "hash": "1cea1d71da85b7f99ff26daf9e816fc76ea287d67b5806e973b0ebaddd11a873",
  "cid": "QmV11cea1d71da85b7f99ff26daf9e816fc76ea287d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288636,
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
      "evaluated_at": 1760288636
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
  "sig": "4cbb9451895fedd455a47898caaa6dfc41edc2c6913b2c9ccfb6d89508e9dd49"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}