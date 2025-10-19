```json
{
  "id": "78eb2cdbdc9ffaca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290197,
  "host_pid": "9e6742732c60:1",
  "hash": "83cd317c85f8b5e818e2f4bb027d0731dba904a164ee56442f9ca28386ba2a69",
  "cid": "QmV183cd317c85f8b5e818e2f4bb027d0731dba904a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290197,
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
      "evaluated_at": 1760290197
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
  "sig": "3bf73162e25575677a7b7b1932c2954849402df88a9bc0a3deb48fc1bfa311bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460526260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 51458400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': '4d7dea8b6c0fe79e'}}}