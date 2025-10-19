```json
{
  "id": "593b440f35916217",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293562,
  "host_pid": "9e6742732c60:1",
  "hash": "e6b24e3f227673953935dae5f3c75297417ee7f18090c4148af47850ad09e81f",
  "cid": "QmV1e6b24e3f227673953935dae5f3c75297417ee7f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293562,
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
      "evaluated_at": 1760293562
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
  "sig": "7f5e8bd03b82be94cef80c59adc4468b1e00af5cbfc1a259984c6f53e7326042"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023973780
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 19394960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'a6cf7acef53d66c2'}}}