```json
{
  "id": "a4f3ab4da12dd012",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288921,
  "host_pid": "9e6742732c60:1",
  "hash": "391a9cedb6ab7137ccc281af3775c09066614722a0752199b6e85750c2c2e88c",
  "cid": "QmV1391a9cedb6ab7137ccc281af3775c09066614722",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288921,
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
      "evaluated_at": 1760288921
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
  "sig": "376de5d2e524730ffdc077b00a5a09eba50534b09cc6b4a3d0e6cec56ea5b1b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590136300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 53506116, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285764, 'matching_hash': '2d6fc2065b3c1287'}}}