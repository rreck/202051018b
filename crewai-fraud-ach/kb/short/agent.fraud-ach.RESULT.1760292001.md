```json
{
  "id": "b1088314bf413465",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292001,
  "host_pid": "9e6742732c60:1",
  "hash": "09ba95cbc929476e8905aae148c86d4e9e19796d8277e7fb627884976832a32f",
  "cid": "QmV109ba95cbc929476e8905aae148c86d4e9e19796d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292001,
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
      "evaluated_at": 1760292001
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
  "sig": "b3524f3c0db257eb3981d975a4a27ca6bacd256c42e795391c4b25c9276cdef9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596116036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 47000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': 'e2bf4d89584c6445'}}}