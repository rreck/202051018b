```json
{
  "id": "9f0787fb43e79b01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290275,
  "host_pid": "9e6742732c60:1",
  "hash": "538acc8ae145b677cd5ca29495130627104cf3688baa4d2ddaa0d2873d04256c",
  "cid": "QmV1538acc8ae145b677cd5ca29495130627104cf368",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290275,
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
      "evaluated_at": 1760290275
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
  "sig": "0e01c34142e61dd49d7e88ccc36168f86671fd99a8a8060ca51ad78ed5a02946"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596367142
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 66147052, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': '4f1a5a8d43b99e0b'}}}