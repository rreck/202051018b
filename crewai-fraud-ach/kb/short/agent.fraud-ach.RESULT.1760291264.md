```json
{
  "id": "6e1aa8210b59d0c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291264,
  "host_pid": "9e6742732c60:1",
  "hash": "637b73956c453710f613338d3f285db805df89cd6fa9971e3a910560b4cf27a5",
  "cid": "QmV1637b73956c453710f613338d3f285db805df89cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291264,
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
      "evaluated_at": 1760291264
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
  "sig": "06c105beff6f6f7f5cdfdf7335997e902048c7b321e4d704218fbccd27ab3aa9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154786749
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 75094821, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': '09892425b2f11015'}}}