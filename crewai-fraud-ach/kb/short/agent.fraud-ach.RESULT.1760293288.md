```json
{
  "id": "04e161e9d4f6b51d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293288,
  "host_pid": "9e6742732c60:1",
  "hash": "ac54cebe16b20c4ff2a101491384ba1f5f0bd724f6c79ac976bc3aa4fc6d17e2",
  "cid": "QmV1ac54cebe16b20c4ff2a101491384ba1f5f0bd724",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293288,
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
      "evaluated_at": 1760293288
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
  "sig": "6a185083394108a59cf15ba012a3a0a947cfd375fbb8721736e53b416c1b1531"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467895506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 34634995, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285764, 'matching_hash': 'b02327f98beb6712'}}}