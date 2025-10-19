```json
{
  "id": "3423d08bc29b1926",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292233,
  "host_pid": "9e6742732c60:1",
  "hash": "115f3c599ae4119a09727fbfb537b84068515f2c1851e2984542333372d508ab",
  "cid": "QmV1115f3c599ae4119a09727fbfb537b84068515f2c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292233,
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
      "evaluated_at": 1760292233
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
  "sig": "40f2cc8566101b8daabb095bc82dea707d85ce7da0e2f997f2511f2e2c9ba88d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466771941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 71021877, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': 'aa929aac6878f78f'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}