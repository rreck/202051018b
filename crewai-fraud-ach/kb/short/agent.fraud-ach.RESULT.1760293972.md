```json
{
  "id": "ab891778e9c58b10",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293972,
  "host_pid": "9e6742732c60:1",
  "hash": "9ae0855def4bf898caa8b45bfe70cbb0dbadd187f7c9635e1ae4c44504bbff09",
  "cid": "QmV19ae0855def4bf898caa8b45bfe70cbb0dbadd187",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293972,
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
      "evaluated_at": 1760293972
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
  "sig": "b8cf2df853e07c449a0c53bfb4d30831cd365ae9e06332e96672f55dd684e824"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598774484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 45146663, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285764, 'matching_hash': 'dadabb4a69349ebb'}}}