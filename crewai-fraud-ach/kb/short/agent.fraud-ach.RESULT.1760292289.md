```json
{
  "id": "12647b4efd400e43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292289,
  "host_pid": "9e6742732c60:1",
  "hash": "b5cae02f207244ab71b50d7127b54bb9a3fd326bc8e8118e3537539fca973c3c",
  "cid": "QmV1b5cae02f207244ab71b50d7127b54bb9a3fd326b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292289,
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
      "evaluated_at": 1760292289
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
  "sig": "0127eead76bc1857e582919ef7a929f606864772afe9ef9cafc6abd01da5541c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460464182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 20492026, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285765, 'matching_hash': '97f231b14306ced8'}}}