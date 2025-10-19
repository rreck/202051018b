```json
{
  "id": "9b61f9b3e26a8bc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291707,
  "host_pid": "9e6742732c60:1",
  "hash": "678510d25373741aed3e9698676a69c07680241b640d3ae525de9eac6d113ad5",
  "cid": "QmV1678510d25373741aed3e9698676a69c07680241b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291707,
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
      "evaluated_at": 1760291707
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
  "sig": "58ac48ad879c8ad7e43e881a1465c81f5e7e51a0801de45c8c209f7cc7b91ef1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023367694
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 75910495, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '23afc27b7b9a7115'}}}