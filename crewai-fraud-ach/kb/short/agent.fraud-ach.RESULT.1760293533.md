```json
{
  "id": "3ad603690c30d8f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293533,
  "host_pid": "9e6742732c60:1",
  "hash": "2e65f072beb6aa049f95951b3c992635dbab6834149e23ee4ab4a950e7c0496d",
  "cid": "QmV12e65f072beb6aa049f95951b3c992635dbab6834",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293533,
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
      "evaluated_at": 1760293533
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
  "sig": "233968411ac23d678b2696c66883bc0bd6bab080c00e468612a9865cb31ed2b0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152430853
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 18543140, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285764, 'matching_hash': 'fa17beca2cfad33c'}}}