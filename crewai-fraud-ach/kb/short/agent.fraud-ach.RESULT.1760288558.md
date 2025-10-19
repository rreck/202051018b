```json
{
  "id": "bb5392c7164dbfe5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288558,
  "host_pid": "9e6742732c60:1",
  "hash": "e730ea7b1d0f65c7f075ea04f9208bb8673c2ba6359e111add5f64d2f033177f",
  "cid": "QmV1e730ea7b1d0f65c7f075ea04f9208bb8673c2ba6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288558,
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
      "evaluated_at": 1760288558
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
  "sig": "51ffe4be6559a3842055a1dc46bbff4d74097dc74f9809cbdee19450e4adbda8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461197823
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 17498315, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285763, 'matching_hash': 'c7e6425f6e43a399'}}}