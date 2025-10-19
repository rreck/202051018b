```json
{
  "id": "d4a0448e156589c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293076,
  "host_pid": "9e6742732c60:1",
  "hash": "a88d3bc4c1b993cd7568d5f88fb46f210b92ecded668333ae2dfc0588df70598",
  "cid": "QmV1a88d3bc4c1b993cd7568d5f88fb46f210b92ecde",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293076,
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
      "evaluated_at": 1760293076
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
  "sig": "0e511860b0eff1d88b67672a4a44eac62fdb4d3a4ad9fb94b7f7121a4ce9415e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462772191
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 43214699, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': '3cc4f4a3442921e3'}}}