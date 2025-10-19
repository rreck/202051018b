```json
{
  "id": "edcd123d311a97e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289802,
  "host_pid": "9e6742732c60:1",
  "hash": "74405e033638d0f81316ed7dfc22219a008f04b1a82411a5ef1e00c69c4748a2",
  "cid": "QmV174405e033638d0f81316ed7dfc22219a008f04b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289802,
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
      "evaluated_at": 1760289802
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
  "sig": "3bfef0c0eff9ad7d04bf3006a7daa3093d68089f189d550e4f50d6e3e46c6279"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246259253
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 14711662, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285765, 'matching_hash': '5582c4cd79a5b751'}}}