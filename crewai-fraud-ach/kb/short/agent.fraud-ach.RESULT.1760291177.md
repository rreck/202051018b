```json
{
  "id": "43c4886e4d11ec46",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291177,
  "host_pid": "9e6742732c60:1",
  "hash": "9c5c44ded295860839fbe5a9bb78c86ec7f2e9082ce4ecd1f44d966620e4ee90",
  "cid": "QmV19c5c44ded295860839fbe5a9bb78c86ec7f2e908",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291177,
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
      "evaluated_at": 1760291177
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
  "sig": "f7168aefa89830d772c558a726daeb60b007affb12ace7d7c05942ec75728906"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460250809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 71152042, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': 'b939c4c4097f2f1f'}}}