```json
{
  "id": "0e5ab1a07464c3a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293665,
  "host_pid": "9e6742732c60:1",
  "hash": "af0de349cbf5ae85a956f4824a5cf540462e4d46fcf569baa640ec31c7457bfc",
  "cid": "QmV1af0de349cbf5ae85a956f4824a5cf540462e4d46",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293665,
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
      "evaluated_at": 1760293666
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
  "sig": "da27b52c5f5297806d60add58d4c52901b61111b6884a54728328f673ca63df2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156493582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 28663082, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': '28d5522bb9de7370'}}}